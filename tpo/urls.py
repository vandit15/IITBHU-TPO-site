from django.conf.urls import url
from tpo import views
from django.contrib import auth
from django.conf import settings


app_name = 'tpo'

urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^leavePage$', views.Leave_Page, name='Leave_Page'),
    url(r'^contactUs$', views.Contact_Us, name='Contact_Us'),
    url(r'^calender$', views.Calender, name='Calender'),
    url(r'^varanasi$', views.Varanasi, name='Varanasi'),
    url(r'^why$', views.Why, name='Why'),
    url(r'^Procedure&Policy', views.Procedure_And_Policy, name='Procedure_And_Policy'),
    url(r'^register$', views.Register, name='Register'),
    url(r'^login$', views.Login, name='Login'),
    url(r'^logout$', views.Logout, name='Logout'),
    url(r'^Policypdf$',views.Policy_pdf, name='Policy_pdf'),
    url(r'^zip$',views.Zip, name='Zip'),
    url(r'^feedback$', views.Feedback, name='Feedback'),
    url(r'^companyResponseSheet$', views.CompanyResponseSheet, name='CompanyResponseSheet'),
    url(r'^startchat$', views.start_chat, name='start_chat'),
    url(r'^chat$', views.chat, name='chat'),
    url(r'^prevrec$', views.Prevrec, name='prevrec'),
    url(r'^disciplines$', views.Disciplines, name='disciplines'),
    url(r'^overview$', views.Overview, name='overview'),
    url(r'^Beyond$', views.Beyond, name='Beyond'),
    url(r'^tpomessage$', views.Tpomessage, name='Tpomessage'),
    url(r'^facilities$', views.Facilities, name='Facilities'),
    url(r'^directormsg$', views.Directormsg, name='directormsg'),
    url(r'^tpomsg$', views.Tpomsg, name='tpomsg'),

]