from django.urls import path
from .views import *

urlpatterns = [
    #path('login/', index, name='login'),
    path('reg/', RegisterApi.as_view(), name='reg'),
    path('verify-email/', VerifyUserEmail.as_view(), name ='verify'),
    path('login/', LoginUserView.as_view(), name = 'login'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', TestAuthenticationView.as_view(), name = "granted"),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='reset-password-confirm'),
    path('set-new-password/', SetNewPasswordView.as_view(), name='set-new-password'),
    path('logout/', LogoutApiView.as_view(), name='logout')
]