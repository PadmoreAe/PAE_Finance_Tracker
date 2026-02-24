from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, IncomeViewSet

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)
router.register(r'income', IncomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]