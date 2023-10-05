from django.urls import path
from .views import inbox, Directs, SendDirect, UserSearch, NewConversation

app_name = 'accounts'

urlpatterns = [
    path('', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_direct'),
    path('new/', UserSearch, name='usersearch'),
    path('new/<username>', NewConversation, name='newconversation'),

    # path('register', views.register, name='register'),
    # path('login1', views.login1, name='login1'),
    # path('logout1', views.logout1, name='logout1'),

]