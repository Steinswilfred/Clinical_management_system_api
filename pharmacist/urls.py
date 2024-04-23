from django.urls import path
from pharmacist.views import medicince_list,medicince_details,medistate_list, medistate_details, medicine_bill

urlpatterns = [
    # path("api/pharmacist/", ),
    path('api/pharmacist/medicince-list/',medicince_list),
    path('api/pharmacist/edit/<int:passed_id>',medicince_details),
    path('api/pharmacist/medicine-states/',medistate_list),
    path('api/pharmacist/medicine-state/<int:passed_id>',medistate_details),
    path('api/pharmacist/medicine-bill/',medicine_bill),
]
