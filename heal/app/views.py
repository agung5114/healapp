# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
# from django.views.decorators.csrf import csrf_exempt
from .models import Makan, Minum, Makanan, Userdata
import pandas as pd

import os
import json
from unipath import Path
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATAPATH = os.path.join(CORE_DIR, "staticfiles")

@login_required(login_url="/login/")    
def index(request):
    args = Userdata.objects.get(user=request.user)
    df = pd.read_csv(DATAPATH+'/data/profile.csv')
    # df = df[df['username'].isin([str(user)])]
    df= df[df['username']==args.user.username]
    df_act = pd.read_csv(DATAPATH+'/data/activities.csv')
    df_act= df_act[df_act['username']==args.user.username]
    dfc = df_act.groupby(['date'],as_index=False).agg({'calorie':'sum','step':'sum','cycling':'sum','exercise':'sum','coin':'sum','score':'mean','sleep':'sum'})
    dfc['score'] = dfc['score']*100
    dfs = df_act.groupby(['sport'],as_index=False).agg({'date':'count'})
    basket = dfs[dfs['sport']=='Basketball']
    cf = dfs[dfs['sport']=='Crossfit']
    mc = dfs[dfs['sport']=='MixedCardio']
    hp = df_act['heartpoin'].mean()
    score = df_act['score'].mean()*100
    coin = df_act['coin'].sum()
    step_goal = 100*dfc['step'].mean()/10000
    sleep_goal = 100*dfc['sleep'].mean()/480
    calorie_goal = 100*dfc['calorie'].mean()/2500
    context = {
        'gender': json.dumps(df['gender'].tolist()),
        'height': json.dumps(df['height'].tolist()),
        'weight': json.dumps(df['weight'].tolist()),
        'disease': str(df['disease'].tolist()[0]),
        'status': str(df['status'].tolist()[0]),
        'name': json.dumps(df['username'].tolist()[0]),
        'data':args,
        'date':json.dumps(dfc['date'].tolist()),
        'calorie':json.dumps(dfc['calorie'].tolist()),
        'step':json.dumps(dfc['step'].tolist()),
        'basketball':json.dumps(basket['date'].tolist()[0]),
        'crossfit':json.dumps(cf['date'].tolist()[0]),
        'mixedcardio':json.dumps(mc['date'].tolist()[0]),
        'cycling':json.dumps(dfc['cycling'].tolist()),
        'exercise':json.dumps(dfc['exercise'].tolist()),
        'date2':json.dumps(dfc['date'].tolist()),
        'heartpoint':str("{:.2f}".format(hp)),
        'score':str("{:.2f}".format(score)),
        'coin':str("{:.4f}".format(coin)),
        'coins':json.dumps(dfc['coin'].tolist()),
        'scores':json.dumps(dfc['score'].tolist()),
        'step_goal':str("{:.2f}".format(step_goal)),
        'sleep_goal':str("{:.2f}".format(sleep_goal)),
        'calorie_goal':str("{:.2f}".format(calorie_goal)),
    }
    # return render(request,'profil.html',{'data':args})
    # return render(request,'dashboard.html',{'data':args})
    return render(request,'profile.html',context)

# @csrf_exempt
# @login_required(login_url="/login/")    
def wallet(request):
    # return render(request,'makan.html',{
    #     "makans":Makan.objects.all()
    # })
    return render(request,'wallet.html',{
        "makans":Makan.objects.all()
    })

# @csrf_exempt
@login_required(login_url="/login/")
def olahraga(request):
    user = request.user
    df = pd.read_excel(DATAPATH+'/aktifitas.xlsx')
    # df = df[df['username'].isin([str(user)])]
    df['tanggal'] = df['tanggal'].astype('str')
    nama = str(df['username'].unique())
    context = {
        'categories': json.dumps(df['tanggal'].tolist()),
        'tensi': json.dumps(df['GulaDarah'].tolist()),
        'gula_darah': json.dumps(df['Tensi'].tolist()),
        'nama': nama
    }
    return render(request,'olahraga.html',context)

# @csrf_exempt
@login_required(login_url="/login/")
def activity(request):
    args = Userdata.objects.get(user=request.user)
    df = pd.read_csv(DATAPATH+'/data/profile.csv')
    # df = df[df['username'].isin([str(user)])]
    df= df[df['username']==args.user.username]
    df_act = pd.read_csv(DATAPATH+'/data/activities.csv')
    df_act= df_act[df_act['username']==args.user.username]
    dfc = df_act.groupby(['date'],as_index=False).agg({'calorie':'sum','step':'sum','cycling':'sum','exercise':'sum'})
    dfs = df_act.groupby(['sport'],as_index=False).agg({'date':'count'})
    basket = dfs[dfs['sport']=='Basketball']
    cf = dfs[dfs['sport']=='Crossfit']
    mc = dfs[dfs['sport']=='MixedCardio']
    hp = df_act['heartpoin'].mean()
    score = df_act['score'].mean()*100
    coin = df_act['coin'].sum()
    context = {
        'gender': json.dumps(df['gender'].tolist()),
        'height': json.dumps(df['height'].tolist()),
        'weight': json.dumps(df['weight'].tolist()),
        'disease': str(df['disease'].tolist()[0]),
        'status': str(df['status'].tolist()[0]),
        'name': json.dumps(df['username'].tolist()[0]),
        'data':args,
        'date':json.dumps(dfc['date'].tolist()),
        'calorie':json.dumps(dfc['calorie'].tolist()),
        'step':json.dumps(dfc['step'].tolist()),
        'basketball':json.dumps(basket['date'].tolist()[0]),
        'crossfit':json.dumps(cf['date'].tolist()[0]),
        'mixedcardio':json.dumps(mc['date'].tolist()[0]),
        'cycling':json.dumps(dfc['cycling'].tolist()),
        'exercise':json.dumps(dfc['exercise'].tolist()),
        'date2':json.dumps(dfc['date'].tolist()),
        'heartpoint':str("{:.2f}".format(hp)),
        'score':str("{:.2f}".format(score)),
        'coin':str("{:.4f}".format(coin))
    }
    return render(request,'activity.html',context)

@login_required(login_url="/login/")
def airquality(request):
    args = Userdata.objects.get(user=request.user)
    df = pd.read_csv(DATAPATH+'/data/profile.csv')
    # df = df[df['username'].isin([str(user)])]
    df= df[df['username']==args.user.username]
    df_act = pd.read_csv(DATAPATH+'/data/activities.csv')
    df_act= df_act[df_act['username']==args.user.username]
    dfc = df_act.groupby(['date'],as_index=False).agg({'calorie':'sum','step':'sum','cycling':'sum','exercise':'sum','coin':'sum','score':'mean','sleep':'sum'})
    dfc['score'] = dfc['score']*100
    dfs = df_act.groupby(['sport'],as_index=False).agg({'date':'count'})
    basket = dfs[dfs['sport']=='Basketball']
    cf = dfs[dfs['sport']=='Crossfit']
    mc = dfs[dfs['sport']=='MixedCardio']
    hp = df_act['heartpoin'].mean()
    score = df_act['score'].mean()*100
    coin = df_act['coin'].sum()
    context = {
        'status': str(df['status'].tolist()[0]),
        'name': json.dumps(df['username'].tolist()[0]),
        'data':args,
        'date':json.dumps(dfc['date'].tolist()),
        'score':str("{:.2f}".format(score)),
        'coin':str("{:.4f}".format(coin)),
        'coins':json.dumps(dfc['coin'].tolist()),
        'scores':json.dumps(dfc['score'].tolist()),
    }
    return render(request,'airquality.html',context)
    
# @login_required(login_url="/login/")
def hospital(request):
    return render(request,'hospital.html')

# @login_required(login_url="/login/")
def government(request):
    return render(request,'government.html')

@login_required(login_url="/login/")
def leaderboard(request):
    df_act = pd.read_csv(DATAPATH+'/data/activities.csv')
    df_act['score'] = df_act['score'].multiply(100).astype(int).divide(100)
    df_act['coin'] = df_act['coin'].multiply(10000).astype(int).divide(10000)
    df_act['heartpoin'] = df_act['heartpoin'].multiply(100).astype(int).divide(100)
    df_act = df_act.groupby(['name'],as_index=False).agg({'score':'mean','coin':'sum','heartpoin':'mean'})
    df_act = df_act.sort_values('coin', ascending=False)
    data = {
        "name": df_act['name'].tolist(),
        "score": df_act['score'].tolist(),
        "coin": df_act['coin'].tolist(),
        "heartpoint": df_act['heartpoin'].tolist()
    }
    all_data = [{'name': data['name'][i], 
                'score': data['score'][i],
                "coin": data['coin'][i],
                "heartpoint": data['heartpoint'][i]} for i in range(len(data['name']))]
    context = {
        'data':all_data
    }
    return render(request,'leaderboard.html',context)
    