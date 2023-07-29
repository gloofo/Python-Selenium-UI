
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

def test_Go_To_Main_Page(setup):
    mainPage(setup)

def test_Python_Search(setup):
    navigate(setup)
    
def test_Getting_Started_Docs(setup):
    menuLists(setup)