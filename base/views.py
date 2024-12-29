from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import MenuCategory,MenuItem,Order,Waiter,Reception,Bill
from .serializers import MenuCategorySerializer,MenuItemSerializer,OrderSerializer,WaiterSerializer,ReceptionSerializer,UserSerializer,BillSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissions
from django.contrib.auth.models import Group 
from rest_framework import generics

# Create your views here.

class MenuCategoryApiView(ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    filterset_fields = ['name']
    search_fields = ['name']

class MenuItemApiView(GenericAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    search_fields = ['name','price']

    def get(self,request):
       menu_item_objs = self.get_queryset()
       serializer = self.get_serializer(menu_item_objs,many =True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class MenuItemDetailApiView(GenericAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    def get(self ,request,pk):
        menu_item_obj = self.get_object()
        serializer = self.get_serializer(menu_item_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        menu_item_obj = self.get_object()
        serializer = self.get_serializer(menu_item_obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        menu_item_obj = self.get_object()
        menu_item_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderApiView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]
    search_fields = ['name','quantity','waiter']


    def get(self,request):
       order_objs = self.get_queryset()
       serializer = self.get_serializer(order_objs,many =True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class OrderDetailApiView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    def get(self ,request,pk):
        order_obj = self.get_object()
        serializer = self.get_serializer(order_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        order_obj = self.get_object()
        serializer = self.get_serializer(order_obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        order_obj = self.get_object()
        order_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class WaiterApiView(GenericAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    def get(self,request):
       waiter_objs = self.get_queryset()
       serializer = self.get_serializer(waiter_objs,many =True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class WaiterDetailApiView(GenericAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    def get(self ,request,pk):
        waiter_obj = self.get_object()
        serializer = self.get_serializer(waiter_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        waiter_obj = self.get_object()
        serializer = self.get_serializer(waiter_obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        waiter_obj = self.get_object()
        waiter_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReceptionApiView(GenericAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    def get(self,request):
       reception_objs = self.get_queryset()
       serializer = self.get_serializer(reception_objs,many =True)
       return Response(serializer.data)
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class ReceptionDetailApiView(GenericAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsAuthenticated,DjangoModelPermissions]

    def get(self ,request,pk):
        reception_obj = self.get_object()
        serializer = self.get_serializer(reception_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        reception_obj = self.get_object()
        serializer = self.get_serializer(reception_obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        reception_obj = self.get_object()
        reception_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
    
@api_view(['POST'])
def register_employee(request):
    if request.user.groups.name == 'Management':
        try:
            employee_group = Group.objects.get(name = 'Employee')
        except:
            return Response('No Employee Group Found',status=status.HTTP_404_NOT_FOUND)
        
        password = request.data.get('password')
        hash_password = make_password(password)
        data = request.data.copy()
        data['password']= hash_password
        data['groups'] = employee_group
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response('You are not authorized to perform this action',status=status.HTTP_403_FORBIDDEN)
    
@api_view(['POST'])
@permission_classes([IsAdminUser])
def register_management(request):
    try:
        management_group = Group.objects.get(name = 'Management')
    except:
        return Response('No Management Group Found',status=status.HTTP_404_NOT_FOUND)
    
    password = request.data.get('password')
    hash_password = make_password(password)
    data = request.data.copy()
    data['password']= hash_password
    data['groups'] = management_group.id
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username,password=password)
    if user == None:
        return Response('Username or Password invalid!!',status=status.HTTP_400_BAD_REQUEST)
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key,status=status.HTTP_200_OK)
    







