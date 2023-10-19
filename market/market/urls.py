from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import *
from item.views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('items/create-item', createItem, name='create-item'),
    path('admin/', admin.site.urls),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

