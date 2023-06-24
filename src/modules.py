import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@pytest.fixture
def data():
    with open("resources/locators.yaml") as file:
        r =  yaml.load(file, Loader=yaml.FullLoader)

    return r

@pytest.fixture(scope='function')
def setup():
    print("TEST STARTED")
    yield webdriver.Chrome()
    print("TEST ENDED")

def goto(setup, data):
    getData = data['page']['main']
    setup.get(getData)
    setup.maximize_window()
    
def navigate(setup, data):
    element = setup.find_element(By.CSS_SELECTOR, data['page']['search'])
    element.click()
    wait(setup, data, "searchContainer")
    search = setup.find_element(By.ID, data['page']['searchMain'])
    search.send_keys("Python")
    
    sleep(1)
    
    hoverElements = setup.find_elements(By.CSS_SELECTOR, data['page']['results'])
    for i in hoverElements:
        hover = ActionChains(setup).move_to_element(i)
        hover.perform()
        
    if hoverElements:
        firstElement = hoverElements[0]
        hover = ActionChains(setup).move_to_element(firstElement)
        hover.click().perform()
    
    wait(setup, data, "sidebar")
    scroll(setup, -1000)
    
def wait(setup, data, locator):
    return WebDriverWait(setup, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, data['page'][f'{locator}'])
    ))

def scroll(setup, scroll_amount: int):
    return setup.execute_script(f"window.scrollBy(0, {scroll_amount});")
    
def menuLists(setup, data):
    elements = setup.find_elements(By.CSS_SELECTOR, data['page']['list'])
    for element in elements:
        element.click()