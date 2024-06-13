from django.contrib import admin
from django.urls import path
from api.views import UserView, UserPOST, UserEDIT, UserDELETE
from api.views import CategoryView, CategoryPOST, CategoryEDIT, categoryDELETE
from api.views import TransactionPOST, TransactionView, TransactionEDIT, TransactionDELETE

urlpatterns = [
    path('admin/', admin.site.urls),

    #Users
    path('api/users/', UserView.as_view(), name="users"), 
    path('api/user/add', UserPOST.as_view(), name="create-user"),
    path('api/user/detail/<id>', UserView.as_view(), name="user_detail"), 
    path('api/user/edit/<id>', UserEDIT.as_view(), name="edit-user"),
    path('api/user/delete/<id>', UserDELETE.as_view(), name="delete-user"),

    #Categories
    path('api/categories/', CategoryView.as_view(), name="categories"),
    path('api/category/add', CategoryPOST.as_view(), name="create-category"),
    path('api/category/detail/<id>', CategoryView.as_view(), name="category-detail"),
    path('api/category/edit/<id>', CategoryEDIT.as_view(), name="edit-category"),
    path('api/category/delete/<id>', categoryDELETE.as_view(), name="delete-category"),

    #Transactions
    path('api/transactions/', TransactionView.as_view(), name="transactions"),
    path('api/transaction/add', TransactionPOST.as_view(), name="create-transaction"),
    path('api/transaction/detail/<id>', TransactionView.as_view(), name="transaction-detail"),
    path('api/transaction/edit/<id>', TransactionEDIT.as_view(), name="edit-transaction"),
    path('api/transaction/delete/<id>', TransactionDELETE.as_view(), name="delete-transaction"),
]
