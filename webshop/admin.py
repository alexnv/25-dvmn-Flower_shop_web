from django.contrib import admin
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.utils.http import url_has_allowed_host_and_scheme

from .models import Reason, CategoryPrice, FlowersBunch, Order, Lead


class FlowersBunchTabularInline(admin.TabularInline):
    model = FlowersBunch
    extra = 0
    fields = ['name', 'price', 'preview', ]
    ordering = ['price']
    readonly_fields = ['preview']

    def preview(self, obj):
        if not obj.image:
            return 'нет картинки'
        return format_html('<img src="{url}" style="max-height: 100px;"/>',
                           url=obj.image.url)


# @admin.register(Reason)
# class ReasonAdmin(admin.ModelAdmin):
#     inlines = [FlowersBunchTabularInline, ]


# @admin.register(CategoryPrice)
# class CategoryPriceAdmin(admin.ModelAdmin):
#     inlines = [FlowersBunchTabularInline, ]


@admin.register(Order)
class OrderPriceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'firstname',
        'phonenumber',
        'address',
        'order_status'
    ]
    ordering = ['id']

    def response_post_save_change(self, request, obj):
        res = super().response_post_save_change(request, obj)
        if "next" in request.GET:
            if url_has_allowed_host_and_scheme(request.GET['next'], None):
                return HttpResponseRedirect(request.GET['next'])
        else:
            return res


@admin.register(FlowersBunch)
class FlowersBunchAdmin(admin.ModelAdmin):
    model = FlowersBunch
    list_display = ['name', 'preview', 'price', 'recommended']

    readonly_fields = ['preview']

    def preview(self, obj):
        if not obj.image:
            return 'нет картинки'
        return format_html('<img src="{url}" style="max-height: 100px;"/>',
                           url=obj.image.url)

    def reason(self, obj):
        return obj.reason.name

    def category(self, obj):
        return obj.category.name


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    model = Lead
    list_display = ['name', 'phonenumber']
