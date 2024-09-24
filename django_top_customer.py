from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

def top_customers():
    six_months_ago = timezone.now() - timedelta(days=180)
    top_customers = Order.objects.filter(order_date__gte=six_months_ago) \
                                 .values('customer') \
                                 .annotate(total_spent=Sum('total_amount')) \
                                 .order_by('-total_spent')[:5]
    return top_customers

# Example of how to use it in a Django view:
def top_customers_view(request):
    top_customers_list = top_customers()
    return render(request, 'top_customers.html', {'customers': top_customers_list})
