from django.urls import path, include
from django.contrib import admin
from .api.SignUpUserAPI import SignUpUserAPI

admin.autodiscover()

from oauth2_provider import urls as oauth2_urls
from app.api.sampleAPI import UserList, UserDetails, GroupList

# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("o/", include(oauth2_urls)),
    path("users/", UserList.as_view()),
    path("users/<pk>/", UserDetails.as_view()),
    path("groups/", GroupList.as_view()),
    path("auth/signup/", SignUpUserAPI.as_view()),
    # ...
]
