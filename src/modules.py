import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def data():
    with open("resources/locators.yaml") as file:
        r =  yaml.load(file, Loader=yaml.FullLoader)

    return r
