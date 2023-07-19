from django.shortcuts import render,redirect
import joblib
import numpy as np
from .models import Data
model= joblib.load('base/DTClassifier.joblib')
attr=[]
from .ModelForms import DataForm
# Create your views here.

def home(request):
    prediction=''
    form=DataForm  
    
    if(request.method=='POST'):
        form=DataForm(request.POST)
        if(form.is_valid()):
            attr.clear()
            for value in form.cleaned_data.values():
                attr.append(str(value))
            
            pred_temp=model.predict([attr])
            print(pred_temp)
            if(pred_temp == [0]):
                prediction='not ckd'            
            else:
                prediction='ckd'
            form_data=form
            
            
        return render(request,'result.html',{'prediction':prediction,'form':form_data})
    context={'form':form}
        
    return render(request,'home.html',context)


