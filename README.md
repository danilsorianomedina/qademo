Descripción General

Este repositorio contiene pruebas automatizadas para el sitio web DemoQA (https://demoqa.com/), utilizando Selenium en Python, junto con Behave para la implementación de pruebas en estilo BDD (Behavior-Driven Development). Las pruebas cubren diversas funcionalidades del sitio, asegurando que los elementos interactivos funcionen como se espera.

Requisitos Previos
Antes de configurar y ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

Python (3.7 o superior)
Pip (gestor de paquetes de Python)
Navegador web (por ejemplo, Chrome, Firefox)
Configuración

https://github.com/danilsorianomedina/qademo.git.


Copy code
git clone 
Instalar Dependencias: Navega al directorio del repositorio clonado y ejecuta el siguiente comando para instalar las dependencias necesarias:


Copy code
pip install selenium webdriver-manager behave
Configurar el WebDriver: El proyecto usa webdriver-manager para manejar el WebDriver. No es necesario una configuración adicional, ya que webdriver-manager se encargará de descargar la versión correcta del WebDriver para tu navegador.

Ejecución de Pruebas
Para ejecutar las pruebas, usa el comando behave en el directorio raíz del proyecto:


Copy code
behave
Casos de Prueba
Caso de Prueba 1: Formulario
Descripción: Este caso de prueba valida la funcionalidad del formulario en la página "Forms" de DemoQA.

Pasos:

Cargar la página.
Completar y enviar el formulario.
Verificar que el formulario se envíe correctamente.
Caso de Prueba 2: Enlaces
Descripción: Este caso de prueba verifica la funcionalidad de varios enlaces en la página "Links".

Pasos:

Cargar la página de enlaces.
Hacer clic en cada enlace y validar su funcionalidad.
Caso de Prueba 3: Carrusel
Descripción: Este caso de prueba verifica la funcionalidad del control deslizante (slider) en la página "Slider".

Pasos:

Navegar a la sección "Slider".
Arrastrar el control deslizante a la posición 3.
Verificar que el número mostrado sea "3".
