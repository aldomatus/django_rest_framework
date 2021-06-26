#   APIView
#from apps.users.api.api import UserAPIView
#   functions views}
from apps.users.api.api import user_api_view, user_detail_api_view
#   Django
from django.urls import path

urlpatterns = [
    path('usuario/', user_api_view, name='usuario.api'),
    path('usuario/<int:pk>/', user_detail_api_view, name = 'user_detail_api_view')
]
