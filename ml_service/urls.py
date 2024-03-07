from django.urls import path
from .views import GRPCView, stop_grpc_server


urlpatterns = [
    path('start/', GRPCView.as_view(), name='grpc'),
    path('stop/', stop_grpc_server, name='grpc_stop'),
]
