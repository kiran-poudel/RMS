from rest_framework import serializers
from .models import MenuCategory,MenuItem,Order,Waiter,Reception,User,Bill


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password','contact','groups','image','address']


class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'  # or specify fields individually

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'  # or specify fields individually

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'  # or specify fields individually

class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'  # or specify fields individually

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'  # or specify fields individually

class BillSerializer(serializers.ModelSerializer):
    order_details = OrderSerializer(source='order', read_only=True)
    menu_item_details = MenuItemSerializer(source='price', read_only=True)

    class Meta:
        model = Bill
        fields = ['id', 'order', 'order_details', 'price', 'menu_item_details', 'updated_at', 'created_at']

    total_amount = 0

    def create(self, validated_data):
        order = validated_data.get('order')
        price = validated_data.get('price')
        quantity = order.quantity if order else 0

        # Calculate the total amount (price * quantity)
        total_amount = price.price * quantity if price else 0

        bill = Bill.objects.create(order=order, price=price,total_amount= total_amount)
        return bill