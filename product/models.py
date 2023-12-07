from django.db import models, IntegrityError
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from store.models import Store
# Create your models here.
class Product(models.Model):
	item = models.CharField(max_length=255,null=False)
	description = models.TextField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	store_name = models.ForeignKey(Store, on_delete=models.CASCADE,to_field='name',related_name='item',default=None,null=False)

	# 可以有重複的store_name和item ，但某個商店的某個商品是唯一的，一個商店不能有重複商品出現
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['store_name', 'item'], name='unique_store_item')
		]
	def __str__(self):
		return self.item


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
	list_display = ['item','price','store_name','description','update_time']
	list_filter = (PriceFilter,)
	search_fields = ('item','price','store_name')
	ordering = ('item','price',)