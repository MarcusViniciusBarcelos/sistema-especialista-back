from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RulesListView, ValuesListView, VariablesListView

router = DefaultRouter()
router.register(r'values', ValuesListView, basename='values')
router.register(r'variables', VariablesListView, basename='variables')
router.register(r'rules', RulesListView, basename='rules')

urlpatterns = [
    path('variables/<int:variables_id>/values/', ValuesListView.as_view(
        {'get': 'list', 'post': 'create'}), name='variable-values-list'),
    path('variables/<int:variables_id>/values/<int:pk>/', ValuesListView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='variable-values-detail'),
    path('rules/', RulesListView.as_view({'get': 'retrieve',
         'patch': 'partial_update', 'delete': 'destroy'}), name='rules-list'),
    path('', include(router.urls)),
]
