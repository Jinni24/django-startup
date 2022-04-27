from django.urls import path,URLPattern
from boot import views

app_name = "boot"
urlpatterns = [
    path("base/",views.test),
    path("blog/",views.blog, name="blog"),
    path("home/",views.home, name="home"),
    path("about/",views.about , name="about"),
    path("contact/",views.contact, name="contact"),
    path("login/",views.login, name = "login"),
    path("sign-up/",views.sign_up, name = "sign_up"),
    path("logout/",views.logout, name = "logout"),
]