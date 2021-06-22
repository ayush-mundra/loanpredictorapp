from django.http import HttpResponse


from django.shortcuts import render
import joblib

def home(request):
	return render(request, "home.html")

def result(request):
 
	cls = joblib.load("finalized_model.sav")
	lis = []
	lis.append(request.POST.get("ApplicantIncome"))
	lis.append(request.POST.get("CoapplicantIncome"))
	lis.append(request.POST.get("LoanAmount"))
	lis.append(request.POST.get("Loan_Amount_Term"))
	lis.append(request.POST.get("Credit_History"))
	lis.append(request.POST.get("Dependents"))
	lis.append(request.POST.get("Male"))
	lis.append(request.POST.get("married_Yes"))
	lis.append(request.POST.get("Not_graduate"))
	lis.append(request.POST.get("Self_Employed"))
	lis.append(request.POST.get("Rural"))
	lis.append(request.POST.get("SemiUrban"))
	lis.append(request.POST.get("Urban"))

	ans = cls.predict([lis])
	return render(request, "result.html", {"ans":ans})