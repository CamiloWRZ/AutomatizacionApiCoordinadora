from screenpy import Actor, when, then, scene, act, given
from screenpy_requests.questions import StatusCodeOfTheLastResponse
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, ContainsTheEntry, ContainsTheEntries, ContainsTheText
from Questions.bodyOfTheLastResponse import BodyOfTheLastResponse
from Utils.endpoint import ENDPOINT_COORDINADORA
from Tasks.request import Request
from Tasks.sendRequest import SendRequest
from Utils.responses import dateNotFound, dateNotAvailable, emptyName, emptyLastName, emptyPhone, emptyEmail, emptyDescriptionAdress, emptyApp, dateLimitsBefore, dateLimitsAfter



""" @scene('''El usuario debe poder realizar una solicitud de recogidas''')
@act('''Se realiza una solicitud de recogida correctamente''')

def test_api(usuario: Actor) -> None:

    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "calle 16", "2021-12-09", "ana", "prueba",
            "3005777777", "ana@gmail.com", "calle 16", "envios"), 
        'post'))
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), ContainsTheEntry("isError", False))) """