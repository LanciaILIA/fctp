from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pereval_added, Coords, Pereval_images, Users
from .serializers import Pereval_addedSerializer


class pereval_addedAPIView(APIView):
    def pereval_added(self, request):
        pereval_added_new = Pereval_added.objects.create(
            status=request.data['status'],
            beautyTitle=request.data['beautyTitle'],
            title=request.data['title'],
            other_titles=request.data['other_titles'],
            connect=request.data['connect'],
            coords_id=request.data['coords_id'],
            users_id=request.data['users_id']
        )

class coordsAPIView(APIView):
    def coords(self, request):
        coords_new = Coords.objects.create(
            latitude=request.data['latitude'],
            longitude=request.data['longitude'],
            height=request.data['height']
        )

class pereval_imagesAPIView(APIView):
    def pereval_images(self, request):
        pereval_images_new = Pereval_images.objects.create(
            img=request.data['img'],
            pereval_id=request.data['pereval_id']
        )

class pereval_addedListAPIView(generics.ListAPIView): # Получение всех данных из таблицы Перевал
    queryset = Pereval_added.objects.all()
    serializers_class = Pereval_addedSerializer

class pereval_addedAPIUpdate(generics.UpdateAPIView): # Редактирование конкретной записи из таблицы Перевал
    queryset = Pereval_added.objects.all()
    serializers_class = Pereval_addedSerializer

class pereval_addedDetailAPIView(generics.RetrieveAPIView): # Получение конкретной данной из таблицы Перевал
    queryset = Pereval_added.objects.all()
    serializers_class = Pereval_addedSerializer

