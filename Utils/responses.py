dateNotFound = {
    "isError": True,
    "message": "Los valores de entrada no son correctos.",
    'code': 'BAD_MESSAGE',
    'cause': '"fechaRecogida" is not allowed to be empty'
}

dateNotAvailable = {
    "isError": True,
    "data": {
        "message": "Error, Ya existe una recogida programada para hoy, id: 26775935",
        "idRecogidaAnterior": "26775935",
        "recogida_anterior": True
    },
}

dateLimitsBefore = {
    "isError": True,
    "data": {
        "message": "El campo fecha: 02-08-2024, no debe ser menor a la fecha actual.",
        "idRecogidaAnterior": "02-08-2024, no debe ser menor a la fecha actual.",
        "recogida_anterior": True
    },
}

dateLimitsAfter = {
    "isError": True,
    "data": {
        "message": "El campo fecha: 02-10-2024, no debe ser mayor a la fecha: 09-09-2024",
        "idRecogidaAnterior": "02-10-2024, no debe ser mayor a la fecha",
        "recogida_anterior": True
    },
}

emptyName = {
    "isError": True,
    "message": "Los valores de entrada no son correctos.",
    "code": "BAD_MESSAGE",
}

emptyLastName = {
    "isError": True,
    "message": "Los valores de entrada no son correctos.",
    "code": "BAD_MESSAGE",
    "cause": "\"apellidosEntrega\" is not allowed to be empty"
}

emptyPhone ={
     "isError": True,
    "message": "Los valores de entrada no son correctos.",
    "code": "BAD_MESSAGE",
    "cause": "\"celularEntrega\" is not allowed to be empty",
}

emptyEmail ={
    "isError": True,
    "message": "Los valores de entrada no son correctos.",
    "code": "BAD_MESSAGE",
    "cause": "\"emailUsuario\" is not allowed to be empty",
}

emptyDescriptionAdress = {
    "isError": True,
    "message": "Los valores de entrada no son correctos.",
    "code": "BAD_MESSAGE",
    "cause": "\"descripcionTipoVia\" is not allowed to be empty"

}

emptyApp = {
    "isError": True,
    "message": "Los valores de entrada no son correctos.",
    "code": "BAD_MESSAGE",
    "cause": "\"aplicativo\" must be one of [web, envios]"
}