from django.shortcuts import render,redirect
import pandas as pd
import numpy as np
from flask_cors import CORS,cross_origin
from django.http import JsonResponse
from django.http import HttpResponse
import pickle
from sklearn.linear_model import LinearRegression
from pricepredict.models import BuyCar
from contactus.models import ContactUs,contactList
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,user_passes_test

# from footer.models import Footer_links,Footer_item
car = pd.read_csv("./car_price_pridict/Cleaned_Car_data.csv")

model=pickle.load(open('./LinearRegressionModel.pkl','rb'))
@login_required(login_url='login')
def home(request):
    return render(request,'index.html')

@login_required(login_url='login')
def pridict(request):
    companies= sorted(car['company'].unique())
    Car_models= sorted(car['name'].unique())
    year= sorted(car['year'].unique(), reverse=True)
    fuel_type= car['fuel_type'].unique()

    CarDetails=BuyCar.objects.all().order_by('-id') #[0:4] limit the result # extracting all data from model
    paginator=Paginator(CarDetails,4) # data limit= 4
    pageNumber=request.GET.get('page') #getting pagee number
    pageDataFinal=paginator.get_page(pageNumber) # which page number data have to show
    totalPages=pageDataFinal.paginator.num_pages

    PassCarData={
        # 'cardata':CarDetails,
        'cardata': pageDataFinal,
        'lastPage': totalPages,
        'totalPageList':[n+1 for n in range(totalPages)]
       }
    context1={
        'companies': companies,
        'Car_model': Car_models,
        'year': year,
        'fuel_type': fuel_type
    }
    context= {
        **PassCarData,**context1
    }

    
    return render(request,'predict.html',context)


# def predictFunction(request):
#     if request.method == 'POST':
#         # Collecting data from form
#         company_name= request.POST['company']
#         CarModels= request.POST['car_model']
#         year= request.POST['year']
#         fuel_type= request.POST['fuel_type']
#         kms_driven= request.POST['kms_driven']

#     prediction=model.predict(pd.DataFrame([[CarModels, company_name, year, kms_driven, fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))
#     print(prediction)

#     return str(np.round(prediction[0],2))
        

# ChatGPT

def predictFunction(request):
    if request.method == 'POST':
        # Collecting data from form
        company_name = request.POST.get('company')
        car_model = request.POST.get('car_model')
        year = request.POST.get('year')
        fuel_type = request.POST.get('fuel_type')
        kms_driven = request.POST.get('kms_driven')

        # Create a pandas dataframe with the input data
        input_df = pd.DataFrame([[car_model, company_name, int(year), int(kms_driven), fuel_type]],
                                columns=['name','company','year','kms_driven','fuel_type'])

        # Perform the prediction using your machine learning model
        prediction = model.predict(input_df)

        # Tranfering Data TO models
        TransferData=BuyCar(company=company_name,car_model=car_model,year_of_purchase=year,fuel_type=fuel_type,kms_driven=kms_driven,predicted_price=int(np.round(prediction[0], 2)))
        TransferData.save()
        # Return the predicted price as a JSON response
        # return JsonResponse({'Predicted Price': np.round(prediction[0], 2)})
        return HttpResponse(str(np.round(prediction[0], 2)))
    else:
        # Handle invalid HTTP request methods (e.g. GET)
        return JsonResponse({'error': 'Invalid request method'})


@login_required(login_url='login')
def contactUs(request):
    listContact=contactList.objects.all()
    list={
        'list_contact':listContact

    }
    if request.method == 'GET':
        name=request.GET.get('name')
        name1={
            'name': name
        }
    context={
        **list,**name1
    }
    return render(request,'contactus.html',context)

@login_required(login_url='login')
def SendEnquiry(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('textBox')
        TransMsg=ContactUs(name=name,email=email,message=message)
        TransMsg.save()
        url="/contact-us/?name={}".format(name)
        return redirect(url)
    return redirect('/contact-us/')

@user_passes_test(lambda user: not user.is_authenticated, login_url='home')
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            msg="Enter correct username and password"
            return render(request,'login.html', {'errorMsg':msg})
    return render(request, 'login.html')


# def signUp(request):
#     error_message = None
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         cpassword=request.POST.get('cpassword')
#         if password!=cpassword:
#             error_message="Password and Confirm Password must be same."
#             # url="/sign-up/?error={}".format(msg)
#             # return redirect(url)

#         else:
#              # Check if email already exists
#             if User.objects.filter(email=email).exists():
#                 msg = "Email already exists."
#                 url = "/sign-up/?error={}".format(msg)
#                 return redirect(url)
#             else:
#                 my_user = User.objects.create_user(username, email, password)
#                 my_user.save()
#                 return redirect('login')

#     return render(request,'signup.html',{'error_message': error_message})
@user_passes_test(lambda user: not user.is_authenticated, login_url='home')
def signUp(request):
    email_error_message = None
    pw_error_message = None
    username_error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if User.objects.filter(username=username).exists():
            username_error_message = "This username is already taken."
        elif User.objects.filter(email=email).exists():
            email_error_message = "An account with this email already exists."
        elif password != cpassword:
            pw_error_message = "Password and Confirm Password must be same."
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
            return redirect('login')
            
    return render(request, 'signup.html', {'email_error_message': email_error_message, 'pw_error_message':pw_error_message, 'username_error_message':username_error_message})


def LogOut(request):
    logout(request)
    return redirect('login')


