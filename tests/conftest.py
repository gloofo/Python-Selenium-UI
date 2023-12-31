import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from imports import *
from source import *

results = ["▬ Automation Test Summary Info ▬\n"]

#Initialized webdriver
@pytest.fixture(scope='session')
def setup():
    print("TEST SETUP")
    options = Options()
    options.add_argument("--hide-scrollbars")
    options.add_argument("--disable=infobars")
    
    getData = data()['page']['main']
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(getData)
    
    yield driver
    print("TEST TEARDOWN")

#get test status
def pytest_runtest_logreport(report):
    if report.when == 'call': 
        name = report.nodeid.split("::")[-1].replace("test_","").replace("_", " ")
        status = report.outcome
        
        if status == "failed":
            results.append(f"{name}: *FAILED* ❌")
        else:
            results.append(f"{name}: *PASSED* ✅")  
    
#Send message to Telegram
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    results.append("\nDevice Name: " + socket.gethostname())
    return send_tg_message("\n".join(results))
