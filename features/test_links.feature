Feature: Verificación de enlaces en DemoQA

  Scenario: Verificar la funcionalidad de los enlaces en la sección Links
    Given El usuario ha cargado la página de Links de DemoQA
    When El usuario hace clic en cada uno de los enlaces
    Then Cada enlace debería llevar a la página correcta
