
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

def test_GoTo(setup):
    main(setup)

def test_Navigate(setup):
    menuLists(setup)