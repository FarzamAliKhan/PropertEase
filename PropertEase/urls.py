from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static


from listings.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('listings/<pk>/', listing_retrieve, name='retrieve'),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete, name='delete'),
    path('add-listing/', listing_create, name="add"),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login' ),
    path('logout/', logout_user, name='logout' ),
    path('blog', frontpage, name='blog'),
    path('favourite/<int:id>/', favourite, name="favourite"),
    path('favourite/', favourite_list, name="favourite_list"),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('about/', aboutpage, name="about"),


]
 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT )