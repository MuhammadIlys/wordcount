from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')    

def count(request):
    data=request.GET['tarea']
    list_data=data.split()
    length_list=len(list_data)

    worddictionary={}

    for word in list_data:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word]=1
    sorted_list=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'mydata':data,'length':length_list,'dict': sorted_list })

