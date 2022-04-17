"""
GET	/hotels/	return all hotels
POST	/hotels/	add a new hotel item
GET	/hotels/<pk>/	return a certain hotels
PUT	/hotels/<pk>/	modify a certain hotels
DELETE	/hotels/<pk>/	delete a certain hotels
Response	JSON
"""
from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from .models import HotelInfo


class HotelListView(View):
    def get(self, request):
        hotels = HotelInfo.objects.all()
        hotel_list = []
        for hotel in hotels:
            hotel_dict = {
                'hotel_id': hotel.hotel_id,
                'hotel_name': hotel.hotel_name,
                'price': hotel.price,
                'is_delete': hotel.is_delete
                }
            hotel_list.append(hotel_dict)
        return JsonResponse(hotel_list, safe=False)

    def post(self, request):
        # request.body(bytes to json_str to json_dict)
        json_str_bytes = request.body()
        json_str = json_str_bytes.decode()
        hotel_dict = json.loads(json_str)
        # hotel_dict = json.loads(request.body().decode())

        hotel = HotelInfo(
            hotel_id=hotel_dict['hotel_id'],
            hotel_name=hotel_dict['hotel_name'],
            price=hotel_dict['price'],
            is_delete=0
            )
        hotel.save()
        return JsonResponse(hotel_dict, status=201)


class HotelDetailView(View):
    def get(self, request, pk):
        try:
            hotel = HotelInfo.objects.get(id=pk)
        except HotelInfo.DoesNotExist:
            return HttpResponse({'message': 'Sorry. The hotel you are looking for does not exist.'}, status=404)
        hotel_dict = {
            'hotel_id': hotel.hotel_id,
            'hotel_name': hotel.hotel_name,
            'price': hotel.price,
            'is_delete': hotel.is_delete
            }
        return JsonResponse(hotel_dict)

    def put(self, request, pk):
        try:
            hotel = HotelInfo.objects.get(id=pk)
        except HotelInfo.DoesNotExist:
            return HttpResponse({'message': 'Sorry. The hotel you are looking for does not exist.'}, status=404)
        hotel_dict = json.loads(request.body().decode())
        hotel.hotel_id = hotel_dict['hotel_id']
        hotel.hotel_name = hotel_dict['hotel_name']
        hotel.price = hotel_dict['price']
        hotel.save()
        return JsonResponse(hotel_dict)

    def delete(self, request, pk):
        try:
            hotel = HotelInfo.objects.get(id=pk)
        except HotelInfo.DoesNotExist:
            return HttpResponse({'message': 'Sorry. The hotel you are looking for does not exist.'}, status=404)
        hotel.delete()
        hotel.is_delete = True
        hotel.save()
        return HttpResponse(status=204)
