from django.shortcuts import render,HttpResponseRedirect
# Create your views here.
from django.views import View
from .forms import Fibunacci,Ackermann,Factorial
import time 
import sys

def View_all(request):
    form=Fibunacci()
    form1=Ackermann()
    form2=Factorial()
    context={"form":form,"form1":form1,"form2":form2}
    return render(request,"index.html",context)

def calculate_fib(n):
    f = [0, 1]     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

 

def calculateFibunacci(request):
    Duration=0
    form=Fibunacci(request.POST or None)
    if form.is_valid():
        n=form.cleaned_data["number"]
        start=time.time()
        result=calculate_fib(int(n))
        end= time.time() - start
        Duration=str(end)[0:6]
        context={"result":result,"time": Duration}
        return render(request,"result.html",context)



def ackermann(m,n):
    if m==0:
        return n+1
    elif n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))


def CalculateAckermann(request):
    Duration=0
    form1=Ackermann(request.POST or None)
    if form1.is_valid():
        m=int(form1.cleaned_data["number1"])
        n=int(form1.cleaned_data["number2"])
        start=time.time()
        result=ackermann(m,n)
        end= time.time() - start
        Duration=str(end)[0:4]
        context={"resultAck":result,"time1":Duration}
        return render(request,"result.html",context)

        

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1))


def CalculateFactorial(request):
    Duration=0
    form2=Factorial(request.POST or None)
    if form2.is_valid():
        n=int(form2.cleaned_data["number"])
        start=time.time()
        result=factorial(n)
        end=time.time() - start
        Duration=str(end)[0:4]
        context={"resultFactioral":result,"time2":Duration}
        return render(request,"result.html",context)



