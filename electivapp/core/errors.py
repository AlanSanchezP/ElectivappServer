# Errores de eventos (Grupo 100)
EVENT_DOES_NOT_EXIST = {
    'detail': 'El evento indicado no existe.',
    'code': 101
}

EVENT_HAS_NOT_STARTED = {
    'detail': 'El evento aún no esta disponible.',
    'code': 102
}

EVENT_HAS_FINISHED = {
    'detail': 'El evento ha finalizado.',
    'code': 103
}

EVENT_OVERLAP = {
    'detail': 'No puede haber 2 eventos al mismo tiempo.',
    'code': 104
}

EVENT_INVALID_DATE = {
    'detail': 'La fecha del evento debe de ser, al menos, un día después del registro.',
    'code': 105
}

# Errores de captura de datos (Grupo 200)
ATTENDANCE_EXPIRED_STUDENT = {
    'detail': 'La boleta ha expirado.',
    'code': 201
}

ATTENDANCE_FOREIGN_STUDENT = {
    'detail': 'La boleta no corresponde a la escuela.',
    'code': 202
}

ATTENDANCE_DUPLICATED_STUDENT = {
    'detail': 'El alumno ya ha asistido a este evento.',
    'code': 203
}

ATTENDANCE_INVALID_PROGRAM = {
    'detail': 'Nombre de carrera inválido.',
    'code': 204
}

ATTENDANCE_BAD_URL = {
    'detail': 'No se pudo acceder a la página.',
    'code': 205
}

ATTENDANCE_MISSING_PARAMETER = {
    'detail': 'No se encontró un campo obligatorio.',
    'code': 206
}

# Errores de autenticacion y permisos
AUTHENTICATION_INVALID_CREDENTIALS = {
    'detail': 'Boleta y/o contraseña inválidos.',
    'code': 301
}

AUTHENTICATION_PERMISSION_DENIED = {
    'detail': 'No tienes permiso para modificar este evento.',
    'code': 302
}