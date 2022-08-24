from turtle import pd
from django.shortcuts import render
import joblib
import prediction_service
import yaml
import os
import json
import pandas as pd
import numpy as np
#from .models import insurance
import psycopg2
import math
# Create your views here.

def index(request):
    return render(request, "index.html")

def result(request):
    tanzeem=joblib.load('../prediction_service/model/model.joblib')
    lis=[]
    lis.append(float(request.GET['age']))
    lis.append(float(request.GET['sex']))
    lis.append(float(request.GET['bmi']))
    lis.append(float(request.GET['children']))
    lis.append(float(request.GET['smoker']))
    lis.append(float(request.GET['region']))

    answer=tanzeem.predict([lis]).tolist()[0]

    return render(request, "index.html", {'answer':answer})