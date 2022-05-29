from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('total', views.total, name='total'),
    path('list', views.list, name='list'),
    path('input', views.input, name='input'),
    ## 詳細
    path('water/detail', views.water_detail, name='water_detail'),
    path('gas/detail', views.gas_detail, name='gas_detail'),
    path('electricity/detail', views.electricity_detail, name='electricity_detail'),
    ## フォーム用
    # 追加
    path('water/add', views.water_edit, name='water_add'),
    path('gas/add', views.gas_edit, name='gas_add'),
    path('electricity/add', views.electricity_edit, name='electricity_add'),
    # 編集
    path('water/mod/<int:water_id>', views.water_edit, name='water_mod'),
    path('gas/mod/<int:gas_id>', views.gas_edit, name='gas_mod'),
    path('electricity/mod/<int:electricity_id>', views.electricity_edit, name='electricity_mod'),
    # 削除
    path('water/del/<int:water_id>', views.water_del, name='water_del'),
    path('gas/del/<int:gas_id>', views.gas_del, name='gas_del'),
    path('electricity/del/<int:electricity_id>', views.electricity_del, name='electricity_del'),

    # 棒グラフ
    path('gas_bargraph', views.gas_bargraph, name='gas_bargraph'),
    path('water_bargraph', views.water_bargraph, name='water_bargraph'),
    path('electricity_bargraph', views.electricity_bargraph, name='electricity_bargraph'),
    # 折れ線グラフ
    path('gas_linegraph', views.gas_linegraph, name='gas_linegraph'),
    path('water_linegraph', views.water_linegraph, name='water_linegraph'),
    path('electricity_linegraph', views.electricity_linegraph, name='electricity_linegraph'),
]
