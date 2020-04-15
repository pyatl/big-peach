from django.urls import path, include
from members.views import MemberCreateView

urlpatterns = [
    path('create/', MemberCreateView.as_view(),
        name='member_create'),
]