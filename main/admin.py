from django.contrib import admin
from .models import Contacts, Product, Billing_detail, Order, Feedback
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["id", "name", "description", "price", "show_image"]
    list_editable = ("price",)
    search_fields = ["name", "description", "manufacturer"]
    list_filter = ["expiration_date", "name"]

    
    def show_image(self, img_obj):
        if img_obj.image:
            return mark_safe("<img width='60' src='{}'>".format(img_obj.image.url))
        return None
    show_image.__name__ = 'Изображение'


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    model = Contacts
    list_display = [field.name for field in Contacts._meta.get_fields()]
    search_fields = ["first_name", "last_name", "message"]
    list_filter = ["sent_at", ]




@admin.register(Billing_detail)
class Billing_detailAdmin(admin.ModelAdmin):
    model = Billing_detail
    list_display = [id, 'first_name', 'last_name', 'number', 'email', 'country', 'city', 'sent_at', 'note_message']
    search_fields = ["first_name", "last_name", "note_message"]
    list_filter = ["sent_at", ]  


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = [field.name for field in Order._meta.get_fields()]
    search_fields = ["product", "p_price", "customer"]
    list_filter = ["customer", ]



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = [field.name for field in Feedback._meta.get_fields()]
    search_fields = ["review", "firstLastName"]
    list_filter = ["firstLastName"]
