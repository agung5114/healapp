"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# import app.dash_nas
# import app.dash_reg

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),           # UI Kits Html files
    # path('main/', include('main.urls')),
    # url('^dash_plot$', TemplateView.as_view(template_name='revenue/plots/dash_plot.html'), name="dash_plot"),
	# url('^django_plotly_dash/', include('django_plotly_dash.urls')),
    # path('django_plotly_dash/', include('django_plotly_dash.urls')),             
]