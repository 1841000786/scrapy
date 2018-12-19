from django.urls import path
from . import views

app_name = 'polls'  # 为整个路由起一个命名空间
urlpatterns = [
    # 首页 ip:port/polls/
    path('', views.index, name='index'),
    # 首页 问题列表 ip:port/index/
    # path('index', views.index, name='index'),
    # 问题详情页 ex: /polls/1/
    path('<int:question_id>', views.detail, name='detail'),
    # 投票结果页 /polls/1/result
    path('<int:question_id>/result', views.results, name='results'),
    # 去投票，选项投票数加1   /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote')
]

# (注意)django1.x路由写法是 正则风格
# from django.conf.urls import url
# urlpatterns = [
#     # /polls/
#     url('^$', views.index, name='index'),
#     # /polls/index/
#     url(r'^index$', views.index),
#     # /polls/5/
#     url(r'^(?p<question_id>[0-9]+)/$'),]


# 与flask对比
# @app.route('/')
# def index():
#     pass


# 先引入视图函数
# path()函数定义的路由最总到会在项目启动时加载
# path(路由规则)
