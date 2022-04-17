from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^hotels/$', views.HotelListView.as_view()),

    url(r'^hotels/(?P<pk>\d+)$', views.HotelDetailView.as_view())

]