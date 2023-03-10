from django.conf import settings
from django.contrib import admin
from django.urls import path,include
# from . import views
from demo import settings
from django.conf.urls.static import static
from .views import login,signup
from.views.login import logout
from.views.cart import Cart
from.views.checkout import CheckOut
from.views.orders import Order, OrderView
# from authentication import views
# from authentication.views import demo
from authentication.views import demo
urlpatterns = [
    path('',demo.as_view(),name="demo"),
    path('login', login.as_view(),name="login"),
    path('signup', signup.as_view(),name="signup"),
    path('logout',logout,name="logout"),
    path('cart',Cart.as_view(),name="cart"),
    path('checkout',CheckOut.as_view(),name="check-out"),
    path('orders',OrderView.as_view(),name="orders"),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
