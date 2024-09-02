# Automatización de Pruebas - API Coordinadora

Este proyecto contiene pruebas automatizadas para la API de Coordinadora utilizando `pytest`, `screenpy-requests`, y un documento xlsx con la descripción de los escenarios de prueba requeridos en `Cucumber` con `Gherkin`. 

## Descripción

Se ha trabajado bajo el patrón de desarrollo ScreenPlay, el proyecto integra casos de prueba que buscan dar cobertura a los posibles fallos en los criterios de aceptación proporcionados para la prueba: 

Se requiere crear un servicio para que los clientes puedan solicitar la recogida de sus
productos, se solicita que el campo dirección sea tipo alfanumérico y que sea obligatorio, el
campo fechaRecogida debe ser de tipo alfanumérico en formato (yyyy-mm-dd) y obligatorio,
se permite ingresar una fecha futura dentro de los 5 días hábiles siguientes, si se crea una
solicitud con una fecha ya ingresada con la misma dirección no se permitirá realizar la
solicitud de recogida, los campos nombreEntrega, apellidosEntrega, celularEntrega,
emailUsuario, descripcionTipoVia y aplicativo son obligatorios y de tipo alfanumérico.

## Estructura del Proyecto

- `screenpy/`: Contiene las definiciones de los actores, acciones y preguntas para las pruebas.
- `Tasks/`: Incluye las tareas y acciones que interactúan con la API.
- `Utils/`: Contiene utilidades y constantes, como endpoints y respuestas esperadas.
- `Questions/`: Contiene las preguntas utilizadas para obtener información de las respuestas de la API.
- `tests/`: Contiene los casos de prueba definidos utilizando `pytest` y `screenpy`.

## Ejecución del proyecto:
- Clonar el proyecto git clone https://github.com/CamiloWRZ/AutomatizacionApiCoordinadora.git
- pip install -r requirements.txt
- pip install pipenv
- pipenv install 
- pipenv Shell (iniciara el entorno virtual de Python para la ejecución de las pruebas
- pytest -k "test_api" --log-cli-level=debug --html=report.html --self-contained-html (Ejecución del test con su reporte HTML correspondiente
