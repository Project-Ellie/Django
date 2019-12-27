from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import BookApiView, CustomUserApiView, ContractualPartyApiView


urlpatterns = [
    path('books/', BookApiView.as_view()),
    path('users/', CustomUserApiView.as_view()),
    path('contractual_parties/', ContractualPartyApiView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
