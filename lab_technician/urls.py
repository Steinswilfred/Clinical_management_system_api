from django.urls import path
from .views import test_list,test_details,testreport_list,testreport_details
urlpatterns = [
    path("list_test",test_list),
    path("test_details/<int:passed_id>",test_details),
    path("list_testreport/",testreport_list),
    path("testreport_details/<int:passed_id>",testreport_details),
]
