from django.shortcuts import *
from django.http import HttpResponse

from utilitycosts.models import *
from utilitycosts.forms import *

from django.views import generic
import io
import matplotlib.pyplot as plt
import numpy as np

import datetime

""" TOP """
def index(request):
    return render(request, 'utilitycosts/index.html')

""" 合計表示 """
def total(request):
    return render(request, 'utilitycosts/total.html')

""" 一覧表示 """
def list(request):
    waters = Water.objects.all().order_by("-payment_date")[0:5] #最新5件
    gases = Gas.objects.all().order_by("-payment_date")[0:5]
    electricities = Electricity.objects.all().order_by("-payment_date")[0:5]

    return render(request , 'utilitycosts/list.html' , { 'waters':waters , 'gases':gases , 'electricities':electricities })

""" 詳細表示 """
def water_detail(request):
    waters = Water.objects.all().order_by("-payment_date")
    return render(request , 'utilitycosts/details/water_detail.html' , { 'waters':waters })

def gas_detail(request):
    gases = Gas.objects.all().order_by("-payment_date")
    return render(request , 'utilitycosts/details/gas_detail.html' , { 'gases':gases })

def electricity_detail(request):
    electricities = Electricity.objects.all().order_by("-payment_date")
    return render(request , 'utilitycosts/details/electricity_detail.html' , { 'electricities':electricities })


""" 追加ページ """
def input(request):
    return render(request, 'utilitycosts/input.html')

""" フォーム """
# 水道代
def water_edit(request , water_id=None):
    """ 水道代の編集 """
    # 修正
    if water_id:
        water = get_object_or_404(Water , pk=water_id)
        initial_data={
                'target_year': water.target_year,
                'target_month': water.target_month,
                'cost': water.cost,
                'payment_date': water.payment_date,
                'date_to': water.date_to,
                'date_from': water.date_from,

            }
    # 新規
    else:
        water = Water()
        last_data = Water.objects.order_by("-payment_date")[0]
        if last_data.target_month == '12':
            default_year = int(last_data.target_year) +1
            default_month = 1
        else:
            default_year = last_data.target_year
            default_month = int(last_data.target_month) +1

        initial_data={
                'target_year': default_year,
                'target_month': default_month,
                'cost': '',
                'payment_date': '',
                'date_to': '',
                'date_from': '',

            }

    if request.method == 'POST':
        form = WaterForm(request.POST , instance=water)
        if form.is_valid():
            water = form.save(commit=False)
            water.save()
            return redirect('list')
    else:
        form = WaterForm(instance=water, initial=initial_data)

    context = {
        'form': form,
        'water_id': water_id,
    }

    return render(request , 'utilitycosts/edits/water_edit.html' , context)

# ガス代
def gas_edit(request , gas_id=None):
    """ ガス代の編集 """
    # 修正
    if gas_id:
        gas = get_object_or_404(Gas , pk=gas_id)
        initial_data={
                'target_year': gas.target_year,
                'target_month': gas.target_month,
                'cost': gas.cost,
                'payment_date': gas.payment_date,
                'date_to': gas.date_to,
                'date_from': gas.date_from,

            }
    # 新規
    else:
        gas = Gas()
        last_data = Gas.objects.order_by("-payment_date")[0]
        if last_data.target_month == '12':
            default_year = int(last_data.target_year) +1
            default_month = 1
        else:
            default_year = last_data.target_year
            default_month = int(last_data.target_month) +1
        initial_data={
                'target_year': default_year,
                'target_month': default_month,
                'cost': '',
                'payment_date': '',
                'date_to': '',
                'date_from': '',

            }

    if request.method == 'POST':
        form = GasForm(request.POST , instance=gas)
        if form.is_valid():
            gas = form.save(commit=False)
            gas.save()
            return redirect('list')
    else:

        form = GasForm(instance=gas,initial=initial_data)

    context = {
        'form': form,
        'gas_id': gas_id,
    }

    return render(request , 'utilitycosts/edits/gas_edit.html' , context)


# 電気代　Electricity
def electricity_edit(request , electricity_id=None):
    """ 電気代の編集 """
    # 修正
    if electricity_id:
        electricity = get_object_or_404(Electricity , pk=electricity_id)
        initial_data={
                'target_year': electricity.target_year,
                'target_month': electricity.target_month,
                'cost': electricity.cost,
                'payment_date': electricity.payment_date,
                'date_to': electricity.date_to,
                'date_from': electricity.date_from,

            }
    # 新規
    else:
        electricity = Electricity()
        last_data = Electricity.objects.order_by("-payment_date")[0]
        if last_data.target_month == '12':
            default_year = int(last_data.target_year) +1
            default_month = 1
        else:
            default_year = last_data.target_year
            default_month = int(last_data.target_month) +1

        initial_data={
                'target_year': default_year,
                'target_month': default_month,
                'cost': '',
                'payment_date': '',
                'date_to': '',
                'date_from': '',

            }

    if request.method == 'POST':
        form = ElectricityForm(request.POST , instance=electricity)
        if form.is_valid():
            electricity = form.save(commit=False)
            electricity.save()
            return redirect('list')
    else:
        form = ElectricityForm(instance=electricity, initial=initial_data)

    context = {
        'form': form,
        'electricity_id': electricity_id,
    }

    return render(request , 'utilitycosts/edits/electricity_edit.html' , context)

def water_del(request, water_id):
    """水道代の削除"""
    water = get_object_or_404(Water, pk=water_id)
    water.delete()
    return redirect('water_detail')

def gas_del(request, gas_id):
    """ガス代の削除"""
    gas = get_object_or_404(Gas, pk=gas_id)
    gas.delete()
    return redirect('gas_detail')

def electricity_del(request, electricity_id):
    """電気代の削除"""
    electricity = get_object_or_404(Electricity, pk=electricity_id)
    electricity.delete()
    return redirect('electricity_detail')
    
# 棒グラフ作成
def setBar(data):
    x = [ '{0}/{1}'.format(d.target_year,d.target_month) for d in data]
    y = [d.cost for d in data] # 料金
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(x,y)
    plt.setp(ax.get_xticklabels(), rotation=30)
    plt.grid(axis='y',linestyle='dotted')
    plt.show()

def setLine(data):
    """折れ線グラフ"""
    x = [ '{0}/{1}'.format(d.target_year,d.target_month) for d in data]
    y = [d.cost for d in data] # 料金
    plt.xlabel('年月')
    plt.ylabel('料金')
    plt.grid()

    plt.plot(x, y)

# svgに変換
def pltToSvg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s
# svg取得(棒グラフ)
def get_svg_bar(request , data):
    setBar(data)
    svg = pltToSvg()
    plt.cla()
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

# svg取得(折れ線グラフ)
def get_svg_line(request , data):
    setLine(data)
    svg = pltToSvg()
    plt.cla()
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

def gas_bargraph(request):
    gases = Gas.objects.all()
    return get_svg_bar(request, gases)

def gas_linegraph(request):
    gases = Gas.objects.all()
    return get_svg_line(request, gases)

def water_bargraph(request):
    waters = Water.objects.all()
    return get_svg_bar(request, waters)

def water_linegraph(request):
    waters = Water.objects.all()
    return get_svg_line(request, waters)

def electricity_bargraph(request):
    electricities = Electricity.objects.all()
    return get_svg_bar(request, electricities)

def electricity_linegraph(request):
    electricities = Electricity.objects.all()
    return get_svg_line(request, electricities)