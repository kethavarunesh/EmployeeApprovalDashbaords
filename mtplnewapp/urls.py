from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('create_document/', views.create_document, name='create_document'),
    path('specific_empfilter/', views.specific_empfilter, name='specific_empfilter'),
    path('employee/reports/', views.employee_reports, name='employee_reports'),
    path('hoddashboard/', views.hoddashbaord, name='hoddashbaord'),
    path('approve_document/<int:document_id>/', views.hod_approve_document, name='hod_approve_document'),
    path('reject/<int:document_id>/', views.hod_reject_document, name='hod_reject_document'),
    path('pqa_dashboard/',views.pqa_dashboard,name='pqa_dashboard'),
    path('approve1/<int:document_id>/', views.pqa_approve_document, name='pqa_approve_document'),
    path('reject1/<int:document_id>/', views.pqa_reject_document, name='pqa_reject_document'),
    path('purchasehod_dashboard/',views.purchasehod_dashboard,name='purchasehod_dashboard'),
    path('approve2/<int:document_id>/', views.purchase_approve_document, name='purchase_approve_document'),
    path('reject2/<int:document_id>/', views.purchase_reject_document, name='purchase_reject_document'),
     path('planthead/',views.planthead,name='planthead'),
    path('approve3/<int:document_id>/', views.planthead_approve_document, name='planthead_approve_document'),
    path('reject3/<int:document_id>/', views.planthead_reject_document, name='planthead_reject_document'),
    path('edit_document/<int:document_id>/', views.edit_document, name='edit_document'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)