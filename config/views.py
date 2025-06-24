import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ai.models import AIResult
from config.metrics import (
    get_daily_sales_data,
    get_daily_sales_quantity_data,
    get_product_brand,
    get_product_category,
    get_product_metrics,
    get_sales_metrics,
)


@login_required(login_url="login")
def home(request):
    product_metrics = get_product_metrics()
    sales_metrics = get_sales_metrics()
    daily_sales_data = get_daily_sales_data()
    daily_sales_quantity = get_daily_sales_quantity_data()
    product_category_metric = get_product_category()
    product_brand_metric = get_product_brand()
    ai_result = AIResult.objects.first()

    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
        "daily_sales_data": json.dumps(daily_sales_data),
        "daily_sales_quantity_data": json.dumps(daily_sales_quantity),
        "product_count_by_category": json.dumps(product_category_metric),
        "product_count_by_brand": json.dumps(product_brand_metric),
        "ai_result": ai_result.result if ai_result else None,
    }

    return render(request, "home.html", context)
