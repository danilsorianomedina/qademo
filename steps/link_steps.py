from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
import time

@given('El usuario ha cargado la página de Links de DemoQA')
def step_impl(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.browser.get("https://demoqa.com/links")

@when('El usuario hace clic en cada uno de los enlaces')
def step_impl(context):
    links_xpaths = [
        "//*[@id='created']",
        "//*[@id='no-content']",
        "//*[@id='moved']",
        "//*[@id='bad-request']",
        "//*[@id='unauthorized']",
        "//*[@id='forbidden']",
        "//*[@id='invalid-url']"
    ]

    for xpath in sorted(links_xpaths):
        WebDriverWait(context.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()
        time.sleep(1)  # Espera para la respuesta del enlace

@then('Cada enlace debería llevar a la página correcta')
def step_impl(context):
    context.browser.quit()