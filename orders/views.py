from rest_framework import viewsets
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
import stripe

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # The order is created here, but payment status is not yet known
        serializer.save()

    def update(self, request, *args, **kwargs):
        # Check if the order is being marked as successful
        instance = self.get_object()
        is_successful = request.data.get('is_successful', None)

        if is_successful is not None and instance.is_successful != is_successful:
            instance.is_successful = is_successful
            instance.save()

            if instance.is_successful:
                # Send confirmation email when the order is marked as successful
                subject = 'Order Confirmation'
                message = f'Dear {instance.fullName},\n\n' \
                          f'Your order with ID {instance.id} has been confirmed. Thank you for your purchase.\n' \
                          f'Your order details:\n'
                for item in instance.items.all():
                    message += f' - {item.product_name} (Quantity: {item.quantity}, Price: {item.price})\n'

                send_mail(
                    subject=subject,
                    message=message,
                    from_email='your@example.com',  # Replace this with your email
                    recipient_list=[instance.email],
                    fail_silently=True,
                )

        return super().update(request, *args, **kwargs)

def create_payment_intent(request):
    if request.method == 'POST':
        try:
            # Retrieve the total price from the request data
            total_price = request.POST.get('total_price', None)
            if not total_price:
                return JsonResponse({'error': 'Total price is missing.'}, status=400)

            # Convert the total price to cents (Stripe uses cents)
            total_price_cents = int(float(total_price) * 100)

            # Replace 'sk_test_your_secret_key' with your Stripe secret key
            stripe.api_key = 'sk_test_your_secret_key'

            # Create a PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=total_price_cents,
                currency='usd',  # Replace with your desired currency code
            )

            return JsonResponse({'clientSecret': intent.client_secret})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
