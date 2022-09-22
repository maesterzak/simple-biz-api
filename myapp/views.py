from http.client import HTTPException
from wsgiref import validate
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *


# Create your views here.


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args,  **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "username": UserSerializer(user).data['username'],
            "message": "User Created Successfully.  Now perform Login to get your token",
        }, status=status.HTTP_201_CREATED)


        

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def orders(request):

    user = request.user
    
    if request.method == 'GET':
        # try:
        orders = Orders.objects.filter(user = user)
       
        serializer = OrderSerializer(orders, many = True)
        if len(orders) == 0:
            return Response(
                        {'message':'user has no order history'},
                        status = status.HTTP_204_NO_CONTENT
                    )


        return Response(
                        {'message':'success', 'data':serializer.data},
                        status = status.HTTP_200_OK
                    )
        # except Exception as e:
        #     return Response(
        #                 {'message': 'Something went wrong while fetching orders'},
        #                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #             )
    elif request.method == 'POST':
        
        try:
            serializer = OrderSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            order = serializer.save()
            return Response({
                "message": OrderSerializer(order).data,
                "message": "Order Created Successfully.",
            }, status=status.HTTP_201_CREATED)

            
        except Exception as e:
            return Response(
                        {'message': 'Something went wrong while creating order'},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )



@api_view(['PATCH', 'GET'])
@permission_classes([IsAuthenticated])
def user(request):
    user = request.user
    
    if request.method == 'PATCH':
        data = request.data
        serializer = UserSerializer(user, data, partial=True)
        try:
                if serializer.is_valid():

                    serializer.save()
                    return Response({
                        'message':'Updated successfully',
                    }, status = status.HTTP_200_OK)
                else:
                    return Response({
                        'message':'Invalid Data',
                    }, status = status.HTTP_400_BAD_REQUEST)

        
        except Exception as e:     
            return Response({
                'message':'Something went wrong',
            }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        try:

            user = UserSerializer(user)
            return Response(
                {'message': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'message': 'something went wrong when trying to load user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )