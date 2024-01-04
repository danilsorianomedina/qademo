from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

@given('El usuario está en la sección Slider de DemoQA')
def step_impl(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.maximize_window()
    context.browser.get("https://demoqa.com/slider")

@when('El usuario arrastra el control deslizante a la posición 3')
def step_impl(context):
    slider = WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='range']"))
    )
    ActionChains(context.browser).click_and_hold(slider).move_by_offset(30, 0).release().perform()

@then('El número 3 debería mostrarse en el control deslizante')
def step_impl(context):
    slider_value = context.browser.find_element(By.ID, "sliderValue").get_attribute("value")
    assert slider_value == "3", f"Expected slider value to be 3, but got {slider_value}"
    context.browser.quit()
