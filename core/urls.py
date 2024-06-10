from django.contrib import admin
from django.urls import path
from api.views import TestConnectionView, UserView, UserPOST, UserEDIT, UserDELETE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserView.as_view(), name="users"), 
    path('api/user/<id>', UserView.as_view(), name="user_detail"), 
    path('api/user/add', UserPOST.as_view(), name="create-user"),
    path('api/user/edit/<id>', UserEDIT.as_view(), name="edit-user"),
    path('api/user/delete/<id>', UserDELETE.as_view(), name="delete-user"),
]
