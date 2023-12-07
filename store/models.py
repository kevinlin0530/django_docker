from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255,null=False)
    location = models.CharField(max_length=255,null=False)
    products = models.ManyToManyField('product.Product', related_name='stores', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_store_name')
        ]
    def __str__(self):
        return self.name
class LocationFilter(admin.SimpleListFilter):
    title = _('Location')
    parameter_name = 'location'

    def lookups(self, request, model_admin):
        # Define the list of tuples for the filter options
        return (
            ('taipei', _('Taipei')),
            ('new_taipei', _('New Taipei')),
            ('taichung', _('Taichung')),
            ('keelung', _('Keelung')),
            # Add other counties as needed
        )

    def queryset(self, request, queryset):
        # Apply the filtering based on the selected option
        if self.value() == 'taipei':
            return queryset.filter(location='Taipei')
        elif self.value() == 'new_taipei':
            return queryset.filter(location='New Taipei')
        elif self.value() == 'taichung':
            return queryset.filter(location='Taichung')
        elif self.value() == 'keelung':
            return queryset.filter(location='Keelung')
        # Add other counties as needed
        else:
            return queryset


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Store._meta.fields] 
    search_fields = ('name','location')
    list_filter = (LocationFilter,)