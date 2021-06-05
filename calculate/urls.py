from django.urls.conf import include
from django.urls import path
from.views import calculateFibunacci,CalculateAckermann,CalculateFactorial,View_all
app_name="calculate"
urlpatterns=[
    path("",View_all,name="view_all"),
    path("/result/Fibunacci",calculateFibunacci,name="result"),
    path("/result/ackermann",CalculateAckermann,name="result1"),
    path("/result/factorial",CalculateFactorial,name="result2"),
]