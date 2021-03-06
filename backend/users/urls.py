from django.conf.urls import url
from . import views
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token
urlpatterns = [
    url(r'captcha/(?P<uuid>.*)/$', views.Regiter.as_view()),
    url(r'register/$', views.Regiter.as_view()),
    url(r'login/$', views.Login.as_view()),
    url(r'email/(.*?)/(.*)/$', views.Forgot.as_view()),
    url(r'forgot/$', views.Forgot.as_view()),
    url(r'userinfo/(?P<user_id>\d+)$',views.UserInfo.as_view()),
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^api-token-refresh/', refresh_jwt_token),
    # url(r'^api-token-verify/', verify_jwt_token)

]
