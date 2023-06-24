from src.modules import *

def test_page(setup, data):
    goto(setup, data)
    navigate(setup, data)
    menuLists(setup, data)