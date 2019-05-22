from django.utils.translation import ugettext as _

# Errores de eventos (Grupo 100)
EVENT_DOES_NOT_EXIST = {
    'detail': _('El evento indicado no existe.'),
    'code': 101
}

EVENT_HAS_NOT_STARTED = {
    'detail': _('El evento aún no esta disponible.'),
    'code': 102
}

EVENT_HAS_FINISHED = {
    'detail': _('El evento ha finalizado.'),
    'code': 103
}

EVENT_OVERLAP = {
    'detail': _('No puede haber 2 eventos al mismo tiempo.'),
    'code': 104
}

EVENT_INVALID_DATE = {
    'detail': _('La fecha del evento debe de ser, al menos, un día después del registro.'),
    'code': 105
}

# Errores de captura de datos (Grupo 200)
ATTENDANCE_EXPIRED_STUDENT = {
    'detail': _('La boleta ha expirado.'),
    'code': 201
}

ATTENDANCE_FOREIGN_STUDENT = {
    'detail': _('La boleta no corresponde a la escuela.'),
    'code': 202
}

ATTENDANCE_DUPLICATED_STUDENT = {
    'detail': _('El alumno ya ha asistido a este evento.'),
    'code': 203
}

ATTENDANCE_INVALID_PROGRAM = {
    'detail': _('Nombre de carrera inválido.'),
    'code': 204
}

ATTENDANCE_BAD_URL = {
    'detail': _('No se pudo acceder a la página.'),
    'code': 205
}

ATTENDANCE_MISSING_PARAMETER = {
    'detail': _('No se encontró un campo obligatorio.'),
    'code': 206
}

ATTENDANCE_NONMATCHING_DATA = {
    'detail': _('El nombre y/o la carrera no coinciden con esta boleta.'),
    'code': 207
}

# Errores de autenticacion y permisos
AUTHENTICATION_INVALID_CREDENTIALS = {
    'detail': _('Boleta y/o contraseña inválidos.'),
    'code': 301
}

AUTHENTICATION_PERMISSION_DENIED = {
    'detail': _('No tienes permiso para modificar este evento.'),
    'code': 302
}

# Errores de actividades
ACTIVITY_TYPE_CREDITS = {
    'detail': _('Las horas requeridas deben de ser mayores a 0.'),
    'code': 401
}