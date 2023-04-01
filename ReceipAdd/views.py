from rest_framework import generics, permissions, status
from .models import Meal
from .serializer import MealSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MealList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

@api_view(['GET', 'DELETE', 'POST'])
def getRoutes(request):
    routes = [
        '/meals/list',
        '/meals/details',
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def meal_list(request):
    if request.method == 'GET':
        meal = Meal.objects.all()
        serializer = MealSerializer(meal, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def meal_detail(request, pk):
    try:
        meal = Meal.objects.get(pk=pk)
    except Meal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MealSerializer(meal)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MealSerializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)