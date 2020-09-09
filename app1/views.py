from django.shortcuts import render,redirect
from.models import Pricing_table
from.forms import PricingForm
from django.contrib import messages

# Create your views here.


def showIndex(request):
    return render(request,"index.html",{"ef":PricingForm(),"data":Pricing_table.objects.all()})
    # Plan_Status = models.CharField(max_length=30)



def saveEmployee(request):
    n1=request.POST.get("ID")
    n2=request.POST.get("Plan_Name")
    n3=request.POST.get("Plan_Formula")
    n4=request.POST.get("Location")
    n5=request.POST.get("Plan_Status")
    n6=request.POST.get("Created_Date")
    n7=request.POST.get("Updated_Date")


    ef = PricingForm(request.POST)
    if ef.is_valid():
        print("one")
        Pricing_table(ID=n1,Plan_Name=n2,Plan_Formula=n3,Location=n4,Plan_Status=n5,Created_Date=n6,Updated_Date=n7).save()
        messages.success(request,"Details are Saved")
        return redirect('main')
    else:
        return render(request,"index.html",{"form":ef})


def update(request):
    i = request.POST["i1"]
    res=Pricing_table.objects.get(ID=i)
    return render(request,"update.html",{"data":res})

def update_details(request):
    Id=request.POST['t5']
    p1=request.POST['t1']
    p2=request.POST['t2']
    l1=request.POST['t3']
    p3=request.POST['t4']
    res1=Pricing_table.objects.filter(ID=Id)
    res1.update(Plan_Name=p1,Plan_Formula=p2,Location=l1,Plan_Status=p3)
    return redirect('main')

def delete(request):
    data = Pricing_table.objects.all()
    del_no=request.GET.get('ID')
    Pricing_table.objects.filter(ID=del_no).delete()
    return redirect('main')





