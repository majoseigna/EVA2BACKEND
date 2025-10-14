from django.urls import path, include
from rest_framework import routers
from .views import (
    EspecialidadViewSet,
    MedicoViewSet,
    PacienteViewSet,
    SalaAtencionViewSet,
    ConsultaMedicaViewSet,
    TratamientoViewSet,
    MedicamentoViewSet,
    RecetaMedicaViewSet
)

router = routers.DefaultRouter()
router.register('especialidades', EspecialidadViewSet)
router.register('medicos', MedicoViewSet)
router.register('pacientes', PacienteViewSet)
router.register('salas', SalaAtencionViewSet)
router.register('consultas', ConsultaMedicaViewSet)
router.register('tratamientos', TratamientoViewSet)
router.register('medicamentos', MedicamentoViewSet)
router.register('recetas', RecetaMedicaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

