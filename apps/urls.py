from django.urls import path
from apps.views import DebtListView , DebtFinish
from apps.views import DebtCreatView, DebtUpdateView, DebtDeleteView


urlpatterns = [
    path('debt-book/', DebtListView.as_view(), name='debt'),
    path('debt-save/', DebtCreatView.as_view(), name='debt-save'),
    path('debt-update/<int:pk>', DebtFinish.as_view(), name='debt-finish'),
    path('debt-finish/<int:pk>', DebtUpdateView.as_view(), name='debt-update'),
    path('debt-delete/<int:pk>', DebtDeleteView.as_view(), name='debt-delete'),

]

