from asyncio.windows_events import NULL
from escuela_api import api


def test_lista_estudiante():
    assert api.update_asistencia(
        '1234567890') == '<h2>EL REGISTRO HA SIDO MODIFICADO POR EL USUARIO</h2>'
