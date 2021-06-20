from django.http import HttpResponse


from django.shortcuts import render
import joblib
import numpy as np

def home(request):
	return render(request, "home.html")

def result(request):
<<<<<<< Updated upstream
	cls = joblib.load("finalized_model.sav")
	normalize = joblib.load("normalize.sav")
	lis = []
	lis.extend(np.squeeze(normalize.fit_transform([[float(request.POST.get("ApplicantIncome")),request.POST.get("CoapplicantIncome"), request.POST.get("LoanAmount"),request.POST.get("Loan_Amount_Term") ]] )))
	# lis.append(normalize.fit_transform(np.reshape(np.array(float(request.POST.get("ApplicantIncome"))), (1,1))))
	# lis.append(normalize.fit_transform(np.reshape(np.array(float(request.POST.get("CoapplicantIncome"))), (1,1))))
	# lis.append(normalize.fit_transform(np.reshape(np.array(float(request.POST.get("LoanAmount"))), (1,1))))
	# lis.append(normalize.fit_transform(np.reshape(np.array(float(request.POST.get("Loan_Amount_Term"))),(1,1))))
	lis.append(float(request.POST.get("Credit_History")))
	lis.append(float(request.POST.get("Dependents")))
	lis.append(float(request.POST.get("Male")))
	lis.append(float(request.POST.get("married_Yes")))
	lis.append(float(request.POST.get("Not_graduate")))
	lis.append(float(request.POST.get("Self_Employed")))
	lis.append(float(request.POST.get("Rural")))
	lis.append(float(request.POST.get("SemiUrban")))
	lis.append(float(request.POST.get("Urban")))
 	# lis.extend(float(request.POST.get("Credit_History")))
	# lis.append(float(request.POST.get("Dependents")))
	# lis.append(float(request.POST.get("Male")))
	# lis.append(float(request.POST.get("married_Yes")))
	# lis.append(float(request.POST.get("Not_graduate")))
	# lis.append(float(request.POST.get("Self_Employed")))
	# lis.append(float(request.POST.get("Rural")))
	# lis.append(float(request.POST.get("SemiUrban")))
	# lis.append(float(request.POST.get("Urban")))
	print(lis)
	ans = cls.predict([lis])
	return render(request, "result.html", {"ans":ans})

=======
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
>>>>>>> Stashed changes
