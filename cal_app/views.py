# Create your views here.
from django.shortcuts import render_to_response
from cal_app.models import rem_result
from django.http import HttpResponseRedirect
def index(request):
    return render_to_response("index.html")

def apcal(request):
    first_num = request.POST.get('first_num')
    sec_num = request.POST.get('sec_num')
    cal_type = request.POST.get('cal_type')
    if cal_type=='+':
        sum=(first_num+sec_num)
        result=rem_result(first_num=first_num,sec_num=sec_num,cal_type=cal_type,result=sum)
        result.save()
    elif cal_type=='-':
        res=(first_num-sec_num)
        result=rem_result(first_num=first_num,sec_num=sec_num,cal_type=cal_type,result=res)
        result.save()
    return HttpResponseRedirect()

def mul_div(request):
    first_num = request.POST.get('first_num')
    sec_num = request.POST.get('sec_num')
    cal_type = request.POST.get('cal_type')
    if cal_type=='*':
        sum=(first_num+sec_num)
        result=rem_result(first_num=first_num,sec_num=sec_num,cal_type=cal_type,result=sum)
        result.save()
    elif cal_type=='/':
        res=(first_num-sec_num)
        result=rem_result(first_num=first_num,sec_num=sec_num,cal_type=cal_type,result=res)
        result.save()
    return HttpResponseRedirect()


