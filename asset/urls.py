from django.urls  import path
from . import api
from  .import views

urlpatterns = [
    path('asset.html',views.AssetListAll.as_view(),name='asset_list'),
    path('asset-add.html',views.AssetAdd.as_view(),name='asset_add'),
    path('asset-del.html',views.AssetDel.as_view(),name='asset_del'),
    path('asset-all-del.html',views.asset_all_del,name='asset_all_del'),
    path('asset-detail-<int:pk>.html',views.AssetDetail.as_view(),name='asset_detail'),
    path('asset-update-<int:pk>.html', views.AssetUpdate.as_view(), name='asset_update'),

    path('asset-hardware-update.html', views.asset_hardware_update, name='asset_hardware_update'),
    path('asset-performance-<int:nid>.html', views.asset_performance, name='asset_performance'),
    path('asset-webssh.html', views.asset_web_ssh, name='asset_web_ssh'),

    path('system-user.html', views.system_user_list, name='system_user'),
    path('system-user-asset-<int:pk>.html', views.system_user_asset, name='system_user_asset'),
    path('system-user-add.html', views.system_user_add, name='system_user_add'),
    path('system-user-del.html', views.system_user_del, name='system_user_del'),
    path('system-user-detail-<int:pk>.html', views.system_user_detail, name='system_user_detail'),
    path('system-user-update-<int:pk>.html', views.system_user_update, name='system_user_update'),

    path('api/asset.html',api.AssetList.as_view(),name='asset_api_list'),
    path('api/asset-detail-<int:pk>.html', api.AssetDetail.as_view(), name='asset_api_detail'),

    path('asset-export.html',views.export,name='asset_export'),
    path('asset-show.html',views.AssetShow,name='asset_show'),
]


app_name="asset"