
import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_path)

from imports import *
from source import *

'''
=================================================================================
=================================== TESTS =======================================
=================================================================================
'''

def test_Go_to_main_page(setup):
    mainPage(setup)

def test_Python_search(setup):
    navigate(setup)
    
def test_Getting_started_docs(setup):
    menuLists(setup)