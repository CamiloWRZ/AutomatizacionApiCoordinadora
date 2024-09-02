from screenpy import Actor, when, then, scene, act, given
from screenpy_requests.questions import StatusCodeOfTheLastResponse
from screenpy.actions import See
from screenpy.resolutions import IsEqualTo, ContainsTheEntry, ContainsTheEntries
from Questions.bodyOfTheLastResponse import BodyOfTheLastResponse
from Utils.endpoint import ENDPOINT_COORDINADORA
from Tasks.request import Request
from Tasks.sendRequest import SendRequest
from Utils.responses import dateNotFound, dateNotAvailable, emptyName, emptyLastName, emptyPhone, emptyEmail,emptyDescriptionAdress, emptyApp, dateLimitsBefore, dateLimitsAfter



@scene('''El usuario no debe poder realizar una solicitud para recoger un producto''')
@act('''Se realiza una solicitud de recogida sin los valores correctos en la fecha''')

def test_dateNotFound(usuario: Actor) -> None:

    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            True, "", "ana", "prueba",
            "3005777777", "ana@gmail.com", "calle 16", "envios"), 
        'post'))
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(dateNotFound)))
    
@scene('''El usuario no debe poder realizar una solicitud para recoger un producto''')
@act('''Se realiza una solicitud de recogida con valores de fecha no disponibles''')    
    
def test_dateNotAvailable(usuario: Actor) -> None:

    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            True, "2024-09-02", "ana", "prueba",
            "3005777777", "ana@gmail.com", "calle 16", "envios"), 
        'post'))
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntries(dateNotAvailable)))

@scene('''El usuario realiza una solicitud de recogida con una fecha anterior a la permitida''')
@act('''Se realiza una solicitud de recogida, verificando los limites de fechas anteriores y posteriores a la fecha actual''')

def test_dateLimits(usuario: Actor) -> None:

    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "calle 16", "2024-08-02", "ana", "prueba",
            "3005777777", "ana@gmail.com", "calle 16", "envios"), 
        'post'))
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntries(dateLimitsBefore)))
    
    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "calle 16", "2024-10-02", "ana", "prueba",
            "3005777777", "ana@gmail.com", "calle 16", "envios"), 
        'post'))
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntries(dateLimitsAfter)))
    

@scene('''El usuario no debe poder realizar una solicitud para recoger un producto''')
@act('''Se realiza una solicitud de recogida, con parametros obligatorios vacios''')

def test_emptyData(usuario: Actor) -> None:

    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "Cl falsa 123", "2024-09-15", "", "Apellido",
            "3150000012", "email@yopmail.com", "casa", "app"), 
        'post'))
    
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(emptyName)))
    
    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "Cl falsa 123", "2024-09-15", "Nombre", "",
            "3150000012", "email@yopmail.com", "casa", "app"), 
        'post'))
    
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(emptyLastName)))
    
    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "Cl falsa 123", "2024-09-15", "Nombre", "Apellido",
            "", "email@yopmail.com", "casa", "app"), 
        'post'))
    
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(emptyPhone)))
    
    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "Cl falsa 123", "2024-09-15", "Nombre", "Apellido",
            "3150000012", "", "casa", "app"), 
        'post'))
    
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(emptyEmail)))
    
    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "Cl falsa 123", "2024-09-15", "Nombre", "Apellido",
            "3150000012", "email@yopmail.com", "", "app"), 
        'post'))
    
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(emptyDescriptionAdress)))
    
    when(usuario).attempts_to(SendRequest.using(
        ENDPOINT_COORDINADORA, 
        Request.solicitudRecogidas(
            "Cl falsa 123", "2024-09-15", "Nombre", "Apellido",
            "3150000012", "email@yopmail.com", "Casa", ""), 
        'post'))
    
    then(usuario).should(
        See.the(StatusCodeOfTheLastResponse(),IsEqualTo(200)),
        See.the(BodyOfTheLastResponse().answered_by(usuario), 
                ContainsTheEntry(emptyApp)))