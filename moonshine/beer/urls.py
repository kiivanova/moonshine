from django.conf.urls import url
from beer.views import BeerView

urlpatterns = [
    url(r'^beer/$', BeerView.as_view(), name='beer-post'),
    url(r'^beer/(?P<pk>.*)/$', BeerView.as_view(), name='beer-get'),
]

beer_api_urls = urlpatterns
