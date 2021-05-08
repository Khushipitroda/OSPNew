from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Policiess, Post_Bills, Post_Announcements, Post_Newss, Govt_Bodiess, Registration, Upload_doc


def registration(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repassword']:
            try:
                user = User.objects.get(username=request.POST['anumber'])
                return render(request, 'one/registration.html', {'msg': "Username has already been taken"})
            except User.DoesNotExist:
                uname = request.POST['anumber']
                fname = request.POST['fname']
                lname = request.POST['lname']
                passwd = request.POST['password']
                uemail = request.POST['email']
                urole = request.POST['role']
                uoccupation = request.POST['Occupation']
                ucontact = request.POST['contact']

                user = User.objects.create_user(username=uname, email=uemail, password=passwd)
                user.first_name = fname
                user.last_name = lname
                user.save()
                new_user = Registration(user=user, anumber=uname, role=urole, contact=ucontact, occupation=uoccupation)
                new_user.save()
                user_doc = Upload_doc(anumber=user)
                user_doc.save()
                return render(request, 'one/login.html', {'msg': "Registered Successfully.."})
        else:
            return render(request, 'one/registration.html', {'msg': "Password Don't Match"})
    else:
        return render(request, 'one/registration.html')


def login_user(request):
    if request.method == "POST":
        username1 = request.POST['adhar']
        password1 = request.POST['pass']

        myuser = auth.authenticate(username=username1, password=password1)

        if myuser is not None:
            auth.login(request, myuser)
            return render(request, 'one/home.html', {'msg': "Logged In!"})

    return render(request, 'one/login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('/one/login/')


def about(request):
    return render(request, 'one/about.html')


def form(request):
    policy = Policiess.objects.all()
    return render(request, 'one/form.html', {'policy': policy})


def contact(request):
    return render(request, 'one/contact.html')


@login_required(login_url='/one/login/')
def g_college(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/g-college.html', {'govt_bodies': govt_bodies})


@login_required(login_url='/one/login/')
def g_court(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/g-court.html', {'govt_bodies': govt_bodies})


@login_required(login_url='/one/login/')
def g_hospital(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/g-hospital.html', {'govt_bodies': govt_bodies})


@login_required(login_url='/one/login/')
def g_office(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/g-office.html', {'govt_bodies': govt_bodies})


@login_required(login_url='/one/login/')
def g_policestation(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/g-policestation.html', {'govt_bodies': govt_bodies})


@login_required(login_url='/one/login/')
def g_school(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/g-school.html', {'govt_bodies': govt_bodies})


@login_required(login_url='/one/login/')
def Govt_Bodies(request):
    govt_bodies = Govt_Bodiess.objects.all()
    return render(request, 'one/gov_bodies.html', {'govt_bodies': govt_bodies})


def home(request):
    return render(request, 'one/home.html')


@login_required(login_url='/one/login/')
def mydocs(request):
    doc = Upload_doc.objects.filter(anumber=request.user)
    if request.method == "POST":
        d = Upload_doc(id=doc[0].id)

        d.anumber = request.user
        try:
            d.Adhar_card = request.FILES['adhar']
        except:
            d.Adhar_card = doc[0].Adhar_card
        try:
            d.Pan_card = request.FILES['pan']
        except:
            d.Pan_card = doc[0].Pan_card
        try:
            d.Voterid_card = request.FILES['votecard']
        except:
            d.Voterid_card = doc[0].Voterid_card
        try:
            d.Passport = request.FILES['passport']
        except:
            d.Passport = doc[0].Passport
        try:
            d.Rashan_card = request.FILES['rasancard']
        except:
            d.Rashan_card = doc[0].Rashan_card
        try:
            d.R_C_Book = request.FILES['rcbook']
        except:
            d.R_C_Book = doc[0].R_C_Book
        try:
            d.Driving_licence = request.FILES['dlicense']
        except:
            d.Driving_licence = doc[0].Driving_licence
        try:
            d.Income_certi = request.FILES['income']
        except:
            d.Income_certi = doc[0].Income_certi
        try:
            d.Noncriminal_certi = request.FILES['non_criminal']
        except:
            d.Noncriminal_certi = doc[0].Noncriminal_certi
        try:
            d.Other = request.FILES['other']
        except:
            d.Other = doc[0].Other
        finally:
            d.save()
            return render(request, 'one/mydocs.html', {'msg': 'Updated Successfully...'})
    else:
        return render(request, 'one/mydocs.html')


@login_required(login_url='/one/login/')
def Policies(request):
    policy = Policiess.objects.all()
    user = Registration.objects.all()

    for i in user:
        if i.anumber == request.user.username:
            policy_for = i.occupation
        else:
            policy_for = ""
    return render(request, 'one/policies.html', {'policy': policy, 'policy_for': policy_for})


@login_required(login_url='/one/login/')
def Poli_scheme(request):
    policy = Policiess.objects.all()
    user = Registration.objects.all()

    for i in user:
        if i.anumber == request.user.username:
            policy_for = i.occupation
        else:
            policy_for = ""

    return render(request, 'one/policies-schemes.html', {'policy': policy, 'policy_for': policy_for})


@login_required(login_url='/one/login/')
def Subsidies(request):
    policy = Policiess.objects.all()
    user = Registration.objects.all()

    for i in user:
        if i.anumber == request.user.username:
            policy_for = i.occupation
        else:
            policy_for = ""

    return render(request, 'one/subsidy.html', {'policy': policy, 'policy_for': policy_for})


@login_required(login_url='/one/login/')
def view_policy(request, myid):
    v = Policiess.objects.filter(id=myid)
    return render(request, 'one/view.html', {'v': v[0]})


@login_required(login_url='/one/login/')
def view_post(request, myid):
    v = Post_Newss.objects.filter(id=myid)
    return render(request, 'one/view_post.html', {'v': v[0]})


@login_required(login_url='/one/login/')
def view_gov(request, myid):
    v = Govt_Bodiess.objects.filter(id=myid)
    return render(request, 'one/view_govbody.html', {'v': v[0]})


@login_required(login_url='/one/login/')
def Policy_Desc(request):
    policy_desc = Policiess.objects.all()
    return render(request, 'one/policy_desc.html', {'policy_desc': policy_desc})


@login_required(login_url='/one/login/')
def Post_Announcement(request):
    post_announcement = Post_Announcements.objects.all()
    return render(request, 'one/post-announcement.html', {'post_announcement': post_announcement})


@login_required(login_url='/one/login/')
def Post_Bill(request):
    post_bill = Post_Bills.objects.all()
    return render(request, 'one/post-bills.html', {'post_bill': post_bill})


@login_required(login_url='/one/login/')
def Post_News(request):
    post_news = Post_Newss.objects.all()
    return render(request, 'one/posts.html', {'post_news': post_news})


@login_required(login_url='/one/login/')
def user_info(request):
    r = Registration.objects.filter(user=request.user)
    u = Upload_doc.objects.filter(anumber=request.user)
    l1 = {}
    l2 = {}

    l1['Adhar_card'] = u[0].Adhar_card
    l1['Pan_card'] = u[0].Pan_card
    l1['Voterid_card'] = u[0].Voterid_card
    l1['Rashan_card'] = u[0].Rashan_card
    l1['Passport'] = u[0].Passport
    l1['R_C_Book'] = u[0].R_C_Book
    l1['Driving_licence'] = u[0].Driving_licence
    l1['Income_certi'] = u[0].Income_certi
    l1['Noncriminal_certi'] = u[0].Noncriminal_certi
    l1['Other'] = u[0].Other

    for key, value in l1.items():
        if value != "None":
            l2[key] = value

    print(l2)

    return render(request, 'one/prof.html', {
        'user_info': r[0],
        'l2': l2,
    })


@login_required(login_url='/one/login/')
def view_postannc(request, myid):
    v = Post_Announcements.objects.filter(id=myid)
    l1 = {}
    l2 = {}
    l1['Document'] = v[0].doc

    for key, value in l1.items():
        if value != "None":
            l2[key] = value

        if value == "None":
            l2[key] = "No Documents Available yet"

    print(l2)
    return render(request, 'one/view_postannc.html', {'v': v[0], 'l2': l2})


@login_required(login_url='/one/login/')
def view_postbill(request, myid):
    v = Post_Bills.objects.filter(id=myid)
    return render(request, 'one/view_postbill.html', {'v': v[0]})