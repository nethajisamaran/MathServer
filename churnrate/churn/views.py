
from django.shortcuts import render

def churn_rate(request):
    i = float(request.POST.get('inicust', '0'))
    c = float(request.POST.get('custlost', '0'))

   churn_rate  = (custlost / inicust)*100 if request.method == 'POST' else 0 

    print("inicust =", i)
    print("custlost=", c)
    print("customer_churn_rate =", churn_rate)

    return render(
        request,
        'churn/form.html',
        {'i': i, 'c': c, 'churn_rate': churn_rate}
    )