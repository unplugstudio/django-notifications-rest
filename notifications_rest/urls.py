from django.urls import re_path as url
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', NotificationViewSet)

app_name = 'notifications_rest'
urlpatterns = [
    url('add/', AddNotification.as_view(), name='add'),
    url('all/', AllNotification.as_view({'get': 'list'}), name='all'),
    url('unread/', UnreadNotificationsList.as_view({'get': 'list'}), name='unread'),
    url('mark-all-as-read/', MarkAllAsRead.as_view(), name='mark_all_as_read'),
    url('mark-as-read/<int:notification_id>', MarkAsRead.as_view(), name='mark_as_read'),
    url('mark-as-unread/<int:notification_id>', MarkAsUnread.as_view(), name='mark_as_unread'),
    url('delete/<int:notification_id>', Delete.as_view(), name='delete'),
    url('api/unread_count/', UnreadNotificationCount.as_view(), name='live_unread_notification_count'),
    url('api/all_count/', AllNotificationCount.as_view(), name='live_all_notification_count'),
    url('api/unread_list/', UnreadNotificationsList.as_view({'get': 'list'}), name='live_unread_notification_list'),
]
