"""blockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from blockchain_api.views import NodeInfo, BlockInfo, TxInfo, HomeView
from blockchain_api.views import page_not_found, server_error, forbidden, bad_request


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', csrf_exempt(HomeView.as_view())),
    url(r'^node/$', csrf_exempt(NodeInfo.as_view())),
    url(r'^block/(.*)$', csrf_exempt(BlockInfo.as_view())),
    url(r'^transaction/(.*)$', csrf_exempt(TxInfo.as_view())),
]


## Error handling

handler400 = bad_request 
handler403 = forbidden
handler404 = page_not_found
handler500 = server_error
