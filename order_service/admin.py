from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from order_service.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'company', 'first_name', 'last_name','is_active', 'is_staff')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',)
    pass


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'model',)
    # pass


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'parameter', 'value',)
    # pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


# @admin.register(ConfirmEmailToken)
# class ConfirmEmailTokenAdmin(admin.ModelAdmin):
#     list_display = ('user', 'key', 'created_at',)
