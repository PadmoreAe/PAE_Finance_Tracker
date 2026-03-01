from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, IncomeViewSet, TotalBalanceView, ReportView

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'income', IncomeViewSet, basename='income')

urlpatterns = [
    path('', include(router.urls)),
    path('balance/total/', TotalBalanceView.as_view(), name='total-balance'),
    path('reports/', ReportView.as_view(), name='reports'),
]