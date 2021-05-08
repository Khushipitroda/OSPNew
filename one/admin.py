from django.contrib import admin
from .models import Policiess, Govt_Bodiess, Post_Bills, Post_Announcements, Post_Newss, Adhar_Card, Feedback ,Registration
from  .models import Upload_doc


# Register your models here.
class Policy_tbl(admin.ModelAdmin):
    list_display = ('name', 'logo', 'type', 'date', 'desc')


admin.site.register(Policiess, Policy_tbl)


class Govt_Bodies_tbl(admin.ModelAdmin):
    list_display = ('name', 'logo', 'type', 'address', 'contact', 'desc')


admin.site.register(Govt_Bodiess, Govt_Bodies_tbl)


class Post_Bill_tbl(admin.ModelAdmin):
    list_display = ('name', 'logo', 'date', 'desc')


admin.site.register(Post_Bills, Post_Bill_tbl)


class Post_Announcement_tbl(admin.ModelAdmin):
    list_display = ('name', 'logo', 'date', 'doc')

admin.site.register(Post_Announcements, Post_Announcement_tbl)


class Post_News_tbl(admin.ModelAdmin):
    list_display = ('name', 'logo', 'date', 'desc')

admin.site.register(Post_Newss, Post_News_tbl)


class Adhar_Card_tbl(admin.ModelAdmin):
    list_display = ('anumber', 'fname', 'mname', 'lname', 'gender', 'address', 'contact', 'dob', 'cast', 'scan')
    radio_fields = {'gender':admin.HORIZONTAL}

admin.site.register(Adhar_Card, Adhar_Card_tbl)


class Feedback_tbl(admin.ModelAdmin):
    list_display = ('anumber', 'name', 'email', 'cno', 'message')

admin.site.register(Feedback, Feedback_tbl)


# class registration_tbl(admin.ModelAdmin):
#     list_display = ('anumber','role','contact','occupation')

admin.site.register(Registration)


class Upload_doc_tbl(admin.ModelAdmin):
    list_display = ('anumber', 'Adhar_card', 'Pan_card', 'Voterid_card', 'Rashan_card', 'Passport', 'R_C_Book', 'Driving_licence','Income_certi', 'Noncriminal_certi', 'Other')

admin.site.register(Upload_doc,Upload_doc_tbl)