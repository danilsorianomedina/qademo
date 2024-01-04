from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
import time

@given('El usuario ha cargado la página de formularios de DemoQA')
def step_impl(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.browser.get("https://demoqa.com/forms")
    time.sleep(15)

@when('El usuario rellena el formulario con datos específicos')
def step_impl(context):
    # Clic en el botón para abrir el formulario
    context.browser.find_element(By.CSS_SELECTOR, "#item-0 > span").click()

    # Esperar a que el formulario esté visible
    WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )

    # Completar el formulario
    context.browser.find_element(By.ID, "firstName").send_keys("DANIEL")
    context.browser.find_element(By.ID, "lastName").send_keys("SORIANO")
    context.browser.find_element(By.ID, "userEmail").send_keys("daniel54_1@hotmail.com")
    context.browser.find_element(By.CSS_SELECTOR, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1) > label").click()
    context.browser.find_element(By.ID, "userNumber").send_keys("3133556508")

    # Fecha de nacimiento
    dob = context.browser.find_element(By.ID, "dateOfBirthInput")
    dob.clear()
    dob.send_keys("18 Sep 1988")
    dob.send_keys(Keys.RETURN)

    # Materias
    context.browser.find_element(By.CSS_SELECTOR, "#subjectsContainer").click()
    context.browser.find_element(By.ID, "subjectsInput").send_keys("Maths", Keys.RETURN)
    context.browser.find_element(By.ID, "subjectsInput").send_keys("English", Keys.RETURN)

    # Hobbies
    context.browser.find_element(By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]/label").click()

    # Scroll y enviar formulario
    submit_button = context.browser.find_element(By.ID, "submit")
    ActionChains(context.browser).move_to_element(submit_button).perform()
    submit_button.click()

@then('El formulario se envía correctamente')
def step_impl(context):
    # Esperar a que aparezca el botón de cierre y luego hacer clic
    WebDriverWait(context.browser, 20).until(
        EC.visibility_of_element_located((By.ID, "closeLargeModal"))
    ).click()

    context.browser.quit()