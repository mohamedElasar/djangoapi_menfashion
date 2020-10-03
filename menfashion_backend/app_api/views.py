
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status

from app_api.models import Category,Shop,Adv,ShopItem,FavItems,ShopItem

from app_api import serializers
from rest_framework.permissions import IsAuthenticated  # <-- Here


# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import UpdateModelMixin





class Cat_ViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage categories in the database"""
    queryset = Category.objects.all()
    serializer_class = serializers.Cat_Serializer



class Favs_ViewSet(viewsets.ModelViewSet,):
    """Manage favorits in the database"""
    queryset = FavItems.objects.all()
    serializer_class = serializers.FavItems_Serializer
    permission_classes = (IsAuthenticated,)             # <-- And here


    # def _params_to_int(self,qs):
    #     return [int(str_id) for str_id in qs.split(',')]
    #
    def get_queryset(self):
        """return shops filtered by user"""
        return self.queryset.filter(user=self.request.user)
    #     cats = self.request.query_params.get('user')
    #     queryset = self.queryset
    #     if cats:
    #         f_user_id = self._params_to_int(cats)
    #         queryset = queryset.filter(user__id__in=f_user_id)
    #
        # return queryset
    # def perform_create(self,serializer):
    #     serializer.save(user=self.request.user)


    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.request.user
    #     serializer = serializers.FavItems_Serializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    #







class Shop_ViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage shops in the database"""
    queryset = Shop.objects.all()
    serializer_class = serializers.Shop_Serializer

    def _params_to_int(self,qs):
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """return shops filtered by categories"""
        cats = self.request.query_params.get('category')
        ids = self.request.query_params.get('id')
        queryset = self.queryset
        if cats:
            cat_id = self._params_to_int(cats)
            queryset = queryset.filter(categories__id__in=cat_id)
        if ids:
            shop_id = self._params_to_int(ids)
            queryset = queryset.filter(id__in=shop_id)

        return queryset



class Adv_ViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage categories in the database"""
    queryset = Adv.objects.all()
    serializer_class = serializers.Ad_Serializer



class AddShop_ViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    """Manage shop adding and updating in the database"""
    serializer_class = serializers.ShopAdd_Serializer
    permission_classes = (IsAuthenticated,)             # <-- And here

    queryset = Shop.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class AddItem_ViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    """Manage shop adding and updating in the database"""
    serializer_class = serializers.CreateItems_Serializer
    permission_classes = (IsAuthenticated,)             # <-- And here

    queryset = ShopItem.objects.all()

    def perform_create(self, serializer):
        myshop = Shop.objects.filter(owner=self.request.user).first()
        serializer.save(shop=myshop)
