from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url('about', views.about, name="about"),
    url('contact', views.contact, name="contact"),
    url('g-college', views.g_college, name="g-college"),
    url('g-court', views.g_court, name="g-court"),
    url('g-hospital', views.g_hospital, name="g-hospital"),
    url('g-office', views.g_office, name="g-office"),
    url('g-policestation', views.g_policestation, name="g-policestation"),
    url('g-school', views.g_school, name="g-school"),
    url('gov_bodies', views.Govt_Bodies, name="gov_bodies"),
    url('login', views.login_user, name="login"),
    url('logout', views.logout_user, name="logout"),
    url('mydocs', views.mydocs, name="mydocs"),
    url('policies', views.Policies, name="policies"),
    url('subsidies', views.Subsidies, name="subsidies"),
    url('user_info', views.user_info, name="profile"),
    path('view_policy/<int:myid>/', views.view_policy, name='view_page'),
    path('view_post/<int:myid>/', views.view_post, name='view_post'),
    path('view_govbody/<int:myid>/', views.view_gov, name='view_govbody'),
    url('poli_scheme', views.Poli_scheme, name="schemes"),
    url('policy_desc', views.Policy_Desc, name="policy_desc"),
    url('posts', views.Post_News, name="posts"),
    url('post-announcement', views.Post_Announcement, name="post-announcement"),
    url('post-bills', views.Post_Bill, name="post-bills"),
    url('registration', views.registration, name="registration"),
    url('form', views.form, name="form"),
    path('view_postannc/<int:myid>/', views.view_postannc, name='view_postannc'),
    path('view_postbill/<int:myid>/', views.view_postbill, name='view_postbill'),
]