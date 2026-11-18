from django.shortcuts import render

def churn_rate(request):
    T = float(request.POST.get('Initcust', '0'))
    S = float(request.POST.get('Custlost', '0'))
    rate = (S / T) * 100 if request.method == 'POST' else 0
    print("Initcust =",T)
    print("Custlost =",S)
    print("Churn_rate =",rate)
    return render(request, 'sarapp/krithwick.html',{'T': T, 'S': S, 'rate': rate})

