
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.urls import path , include

schema_view = get_schema_view(
   openapi.Info(
      title="AuthProject API",
      default_version='v1',
      description="This is documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('admin/', admin.site.urls),
   path('account/', include('apps.account.urls')),
   path('movies/', include('apps.movies.urls')),
   path('genres/', include('apps.genres.urls')),
   path('comment/', include('apps.comment.urls')),
   path('rating/', include('apps.rating.urls')),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

