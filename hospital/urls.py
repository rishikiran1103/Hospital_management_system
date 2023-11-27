from django.urls import path,include
from . import views
urlpatterns = [
    path('homepage/',views.homepage),
    path('login/',views.login),
    path('about/',views.about),
    path('bookappointment/',views.bookappointment),
    path('response/',views.response),
    path('validate/',views.validate),
    path('test/',views.test),
    path('treatment/',views.treatment),
    path('deo/',views.deo),
    path('test_submit/',views.test_submit),
    path('treatment_submit/',views.treatment_submit),
    path('search/',views.search),
    path('doctor/',views.doctor),
    path('dataadminstrator/',views.dataadminstrator),
    path('add_doctor/',views.add_doctor),
    path('del_deo/',views.del_deo),
    path('del_doctor/',views.del_doctor),
    path('del_admin/',views.del_admin),
    path('del_fdo/',views.del_fdo),
    path('del_user/',views.del_user),
    path('add_admin/',views.add_admin),
    path('add_deo/',views.add_deo),
    path('add_fdo/',views.add_fdo),
    path('add_user/',views.add_user),
    path('doc_add/',views.doc_add),
    path('fdo/',views.fdo),
    path('fdo_task/',views.fdo_task),
    path('toggle/',views.toggle),
]