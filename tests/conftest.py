import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from imports import *
from source import *

results = []

def pytest_runtest_logreport(report):
    if report.when == 'call': 
        name = report.nodeid.split("::")[-1].replace("test_"," ")
        status = report.outcome
        
        if status == "failed":
            results.append(f"❌ *FAILED* \\- {name} \n")
        else:
            results.append(f"✅ *PASSED* \\- {name} \n")
            
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    return send_tg_message("\n".join(results))
