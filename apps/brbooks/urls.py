from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.books),
    url(r'^add$', views.add),
    url(r'^add_info$', views.add_info),
    url(r'^(?P<id>\d+)$', views.show_book),
    url(r'^logout$', views.logout),
    url(r'^adding_review$', views.adding_review),
    url(r'^user/(?P<id>\d+)$', views.show_profile),
    url(r'^delete/(?P<id>\d+)$', views.delete)
  ]
