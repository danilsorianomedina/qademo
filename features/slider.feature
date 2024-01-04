Feature: Verificar la funcionalidad del carrusel en DemoQA

  Scenario: Arrastrar el control deslizante a la posición 3 y verificar el número
    Given El usuario está en la sección Slider de DemoQA
    When El usuario arrastra el control deslizante a la posición 3
    Then El número 3 debería mostrarse en el control deslizante
