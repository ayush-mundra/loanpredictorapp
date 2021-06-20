from django.http import HttpResponse


from django.shortcuts import render
import joblib

def home(request):
	return render(request, "home.html")

def getPredictions(ApplicantIncome,CoapplicantIncome, Loan_Amount_Term,  LoanAmount, Credit_History, Dependents, Male, married_Yes, Not_graduate, Self_Employed, Rural, SemiUrban, Urban):

    model =  joblib.load("finalized_model.sav")
    min_max_scaler = joblib.load("normalize.sav")
    prediction = model.predict(min_max_scaler.fit_transform([[ApplicantIncome,CoapplicantIncome, Loan_Amount_Term,  LoanAmount, Credit_History, Dependents, Male, married_Yes, Not_graduate, Self_Employed, Rural, SemiUrban, Urban]]))    
    return prediction

def result(request):
	ApplicantIncome = float(request.POST.get("ApplicantIncome"))
	CoapplicantIncome = float(request.POST.get("CoapplicantIncome"))
	LoanAmount = float(request.POST.get("LoanAmount"))
	Loan_Amount_Term = float(request.POST.get("Loan_Amount_Term"))
	Credit_History = float(request.POST.get("Credit_History"))
	Dependents = float(request.POST.get("Dependents"))
	Male = float(request.POST.get("Male"))
	married_Yes = float(request.POST.get("married_Yes"))
	Not_graduate = float(request.POST.get("Not_graduate"))
	Self_Employed = float(request.POST.get("Self_Employed"))
	Rural = float(request.POST.get("Rural"))
	SemiUrban = float(request.POST.get("SemiUrban"))
	Urban = float(request.POST.get("Urban"))
	result = getPredictions(ApplicantIncome, CoapplicantIncome, Loan_Amount_Term,  LoanAmount, Credit_History, Dependents, Male, married_Yes, Not_graduate, Self_Employed, Rural, SemiUrban, Urban)
	return render(request, "result.html", {"ans": result})