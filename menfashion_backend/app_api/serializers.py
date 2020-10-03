from rest_framework import serializers

from app_api.models import Category,Shop,Adv,ShopItem,FavItems , ShopOwner


class Cat_Serializer(serializers.ModelSerializer):
    """Serializer for category objects"""

    class Meta:
        model = Category
        fields = ('id', 'name')
        read_only_fields = ('id',)



class Items_Serializer(serializers.ModelSerializer):
        """Serializer for Shop items"""

        class Meta:
            model = ShopItem
            fields = ('name','price','description','image_url','category_item')




class Shop_Serializer(serializers.ModelSerializer):
    """Serializer for Shops"""
    items = Items_Serializer(many=True,)
    class Meta:
        model = Shop
        fields = ('id', 'name','categories','address','image_url','description','items')
        read_only_fields = ('id',)



class Ad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ('id', 'title', 'image_url')
        read_only_fields = ('id',)


class FavItems_Serializer(serializers.ModelSerializer):
    # shops = Shop_Serializer()
    class Meta:
        model = FavItems
        fields = ('id','user', 'shops')
        read_only_fields = ('id',)


class ShopOwner_Serializer(serializers.ModelSerializer):
    # shops = Shop_Serializer()
    class Meta:
        model = FavItems
        fields = '__all__'
        read_only_fields = ('id',)
