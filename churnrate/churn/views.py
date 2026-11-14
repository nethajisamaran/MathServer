
from django.shortcuts import render

def churn_rate(request):
    i=float(request.POST.get('inicust','0'))
    c=float(request.POST.get('custlost','0'))

    churnrate=(c/i)*100 if request.method=='POST' else 0 

    print("inicust =",i)
    print("custlost=",c)
    print("customer_churn_rate =",churnrate)

    return render(
        request,
        'churn/form.html',
        {'i':i,'c':c,'churnrate':churnrate}
    )