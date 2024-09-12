from django.shortcuts import render

# Create your views here.
def add_numbers(request):
    result = None
    error = None

    if request.method == "POST":
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')

        try:
            sum = float(num1)+float(num2)
            result = f"The sum is: {sum}"

        except:
            error = "Something went wrong"
    return render(request,'add.html',{'result':result,'error':error})  

def cal(request):
    result = None
    error = None

    if request.method == "POST":
        p = request.POST.get('p')
        t = request.POST.get('t')
        r = request.POST.get('r')

        try:
            interest = (float(p)*float(t)*float(r))/100
            result = f"The interest is: {interest}"

        except:
            error = "Something went wrong"
    return render(request,'pnr.html',{'result':result,'error':error})  




