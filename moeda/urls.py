from django.urls import path

from .views import PegarInfoCreate,PegarInfoList, PegarInfoDetail, PegarInfoUpdate,PegarInfoDelete

urlpatterns = [
    path('', PegarInfoList.as_view(), name="index"),
    path('moeda', PegarInfoCreate.as_view(), name="moeda"),
    path('moedadetail/<int:pk>', PegarInfoDetail.as_view(), name='moedadetail'),
    path('moedaupdate/<int:pk>', PegarInfoUpdate.as_view(), name='moedaupdate'),
    path('moedadelete/<int:pk>', PegarInfoDelete.as_view(), name='moedadelete'),

]