import pytest
import random
from selenium import webdriver
from elements_to_find import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class UserRegistration:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

@pytest.fixture
def new_correct_user():
    name = 'Оксана'
    email = f"oxanaklimocheva14{random.randint(100, 999)}@gmail.com"
    password = f"{random.randint(100000, 999999)}"
    return UserRegistration(name, email, password)

@pytest.fixture
def existed_user():
    return UserRegistration(name='Оксана', email='oxanaklimocheva13123@gmail.com', password='123456')

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page_url = 'https://stellarburgers.nomoreparties.site'
    driver.get(main_page_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.GO_TO_LOGIN_BUTTON))
    return driver

@pytest.fixture
def register_page(driver):
    register_page_url = 'https://stellarburgers.nomoreparties.site/register'
    driver.get(register_page_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON))
    return driver

@pytest.fixture
def authorised_existing_user(driver, existed_user):
    register_page_url = 'https://stellarburgers.nomoreparties.site/login'
    driver.get(register_page_url)
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))

    driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existed_user.email)
    driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existed_user.password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_BUTTON))
    return driver
