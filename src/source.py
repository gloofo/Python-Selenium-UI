#imports all from imports.py
from imports import *
    
#read and open yaml file for locators variable.
def data():
    with open("resources/locators.yaml") as file:
        load =  yaml.load(file, Loader=yaml.FullLoader)
    return load

#main method for test case.
def mainPage(setup):
    assert setup.current_url == "https://playwright.dev/"

#navigates through the page
def navigate(setup):
    #search   
    element = setup.find_element(By.CSS_SELECTOR, data()['page']['search'])
    element.click()
    wait(setup, "searchContainer")
    search = setup.find_element(By.ID, data()['page']['searchMain'])
    search.send_keys("Python")
    sleep(1)
    
    #hover results until the end and go back to the first element then click.
    hoverElements = setup.find_elements(By.CSS_SELECTOR, data()['page']['results'])
    for i in hoverElements:
        hover = ActionChains(setup).move_to_element(i)
        hover.perform()
        
    if hoverElements:
        firstElement = hoverElements[0]
        hover = ActionChains(setup).move_to_element(firstElement)
        hover.click().perform()
        assert setup.current_url == "https://playwright.dev/docs/languages#python"
    
    wait(setup, "sidebar")
    
    #call scroll method
    scroll(setup, -1000)
    sleep(2)
    scroll(setup, 0)
    assert 1 + 2 == 4
    
#waits an element (locator) 
def wait(setup, locator):
    
    return WebDriverWait(setup, 10).until(EC.visibility_of_element_located(
        (By.CLASS_NAME, data()['page'][f'{locator}'])
    ))

#scroll through the page scroll_amount value
def scroll(setup, scroll_amount: int):
    return setup.execute_script(f"window.scrollBy(0, {scroll_amount});")

#clicks every page and save a screenshot
def menuLists(setup):
    elements = setup.find_elements(By.CSS_SELECTOR, data()['page']['list'])
    x = 0
    for element in elements:
        element.click()
        scrolltoBottom(setup)
            
        sleep(1)
        x += 1
        setup.execute_script(f"window.scrollTo(0, 0);")
        setup.save_screenshot(f"screenshots/capture {x}.png")
        
    setup.quit()

#scroll to the bottom until the page data is all loaded    
def scrolltoBottom(setup):
    height = setup.execute_script("return document.body.scrollHeight")
    while True:
        setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        current_height = setup.execute_script("return document.body.scrollHeight")
        if current_height == height:
            break
        height = current_height
    
def send_tg_message(message):
        token = os.environ.get("token", "")
        Id = os.environ.get("Id", "")
        bot = telepot.Bot(token)
        bot.sendMessage(Id, message, parse_mode='MarkdownV2')
