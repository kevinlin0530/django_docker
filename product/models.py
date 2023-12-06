from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
class Product(models.Model):
    item = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class PriceFilter(admin.SimpleListFilter):

	title = _('price')
	parameter_name = 'compareprice' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>50',_('>50')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			('<=50',_('<=50')),
			('>=100',_('>=100')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>50':
			return queryset.filter(price__gt=50)
		if self.value() == '<=50':
			return queryset.filter(price__lte=50)
		if self.value() == '>=100':
			return queryset.filter(price__gte=100)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Product._meta.fields]
	list_filter = (PriceFilter,)
	search_fields = ('item','price')
	ordering = ('item','price',)