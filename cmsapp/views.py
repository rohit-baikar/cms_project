from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from random import *
from django.core.mail import send_mail
from   .models  import   DeptModel,   StudentModel
from   .forms    import    DeptForm,     StudentForm

def ulogin(request):
	if request.user.is_authenticated:
		return redirect("uhome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw = request.POST.get("pw")
			usr = authenticate(username= un, password=pw)
			if usr is None:
				msg = "Login Denied"
				return render(request, "ulogin.html", {"msg":msg})
			else:
				login(request, usr)
				return redirect("uhome")
		else:
			return render(request, "ulogin.html")


def usignup(request):
	if request.user.is_authenticated:
		return redirect("uhome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			try:
				usr = User.objects.get(username=un)
				msg = "email already register"
				return render(request, "usignup.html", {"msg":msg})			
			except User.DoesNotExist:
				pw = ""
				text = "0123456789"
				for i in range(1, 7):
					pw = pw + text[randrange(len(text))]
				print(pw)
				usr = User.objects.create_user(username=un, password=pw)
				usr.save()
				subject = "welcome to collage mgt system"
				text = "ur password is " + str(pw)
				from_email = "rohitbaikar2001@gmail.com"
				to_email = [str(un)]
				send_mail(subject, text, from_email, to_email)		
				return redirect("ulogin")
		else:
			return render(request, "usignup.html")


def urnp(request):
	if request.user.is_authenticated:
		return redirect("uhome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			try:
				usr = User.objects.get(username=un)
				pw = ""
				text = "0123456789"
				for i in range(1, 7):
					pw = pw + text[randrange(len(text))]
				print(pw)
				usr = User.objects.get(username=un)
				usr.set_password(pw)
				usr.save()
				subject = "welcome to collage mgt system"
				text = "ur password is " + str(pw)
				from_email = "sai.tester24jan24@gmail.com"
				to_email = [str(un)]
				send_mail(subject, text, from_email, to_email)		
				return redirect("ulogin")

			except User.DoesNotExist:
				msg = "email does not exists"
				return render(request, "urnp.html", {"msg":msg})
		else:
			return render(request, "urnp.html")



def ulogout(request):
	logout(request)
	return redirect("ulogin")



def uhome(request):
	if request.user.is_authenticated:
		return render(request, "uhome.html")
	else:
		return redirect("ulogin")



def showdept(request):
	data = DeptModel.objects.all()
	return render(request, "showdept.html", {"data":data})


def adddept(request):
	if request.method == "POST":
		data = DeptForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "Department Created"
			fm = DeptForm()
			return render(request, "adddept.html", {"fm": fm, "msg": msg})
		else:
			msg = "Check Errors"
			fm = DeptForm()
			return render(request, "adddept.html", {"fm": fm, "msg": msg})
	else:
		fm = DeptForm()
		return render(request, "adddept.html", {"fm": fm})



def removedept(request, id):
	dt = DeptModel.objects.get(did=id)
	dt.delete()
	return redirect("showdept")


def showstudent(request):
	data = StudentModel.objects.all()
	return render(request, "showstudent.html", {"data":data})


def addstudent(request):
	if request.method == "POST":
		data = StudentForm(request.POST, request.FILES)
		if data.is_valid():
			data.save()
			msg = "Student Record Created"
			fm = StudentForm()
			return render(request, "addstudent.html", {"fm":fm, "msg":msg})
		else:
			msg = "check errors"
			return render(request, "addstudent.html", {"fm":data, "msg":msg})
	else:
		fm = StudentForm()
		return render(request, "addstudent.html", {"fm":fm})



def removestudent(request, id):
	dt = StudentModel.objects.get(rno=id)
	dt.delete()
	return redirect("showstudent")

def updatestudent(request, id):
	if request.method == "POST":
		data = StudentModel.objects.get(rno=id)
		fm = StudentForm(request.POST, instance=data)
		if fm.is_valid():
			fm.save()
			msg = "Records Updated"
			return render(request, "updatestudent.html", {"fm": fm, "msg": msg})
		else:
			msg = "Check Errors"
			return render(request, "updatestudent.html", {"fm": fm, "msg": msg})
	else:	
		data = StudentModel.objects.get(rno=id)
		fm = StudentForm(instance=data)
		return render(request, "updatestudent.html",  {'fm':fm})




