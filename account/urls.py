from .views import CurrentUserView
from django.conf.urls import url
urlpatterns = [
    url(r'^user/$',CurrentUserView.as_view())
]
