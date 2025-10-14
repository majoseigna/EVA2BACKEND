from django.db import models

# --- CHOICES ---
GENERO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]

ESTADO_CONSULTA = [
    ('P', 'Pendiente'),
    ('R', 'Realizada'),
    ('C', 'Cancelada'),
]

# --- TABLAS PRINCIPALES (8 en total) ---
class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    def __str__(self):
        return self.nombre


class SalaAtencion(models.Model):  # Tabla extra (mejora)
    numero = models.CharField(max_length=10)
    piso = models.IntegerField()
    capacidad = models.IntegerField()
    def __str__(self):
        return f"Sala {self.numero} (Piso {self.piso})"


class ConsultaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    sala = models.ForeignKey(SalaAtencion, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    motivo = models.TextField()
    estado = models.CharField(max_length=1, choices=ESTADO_CONSULTA, default='P')
    def __str__(self):
        return f"{self.paciente} - {self.medico}"


class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_dias = models.IntegerField()
    def __str__(self):
        return self.nombre


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=50)
    laboratorio = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class RecetaMedica(models.Model):
    consulta = models.ForeignKey(ConsultaMedica, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    indicaciones = models.TextField()
    def __str__(self):
        return f"Receta {self.id} ({self.consulta})"
