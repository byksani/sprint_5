from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from elements_to_find import TestLocators
import pytest
from config import REGISTER_PAGE_URL, FORGOT_PASSWORD_URL


class TestLogin:

    @pytest.mark.parametrize("login_button_locator", [
        (TestLocators.GO_TO_LOGIN_BUTTON),
        (TestLocators.PERSONAL_ACCOUNT_BUTTON)
    ])
    def test_login_from_main_page_success(self, driver, main_page, existed_user, login_button_locator):
        driver.find_element(*login_button_locator).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.EMAIL_INPUT_FIELD))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existed_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existed_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_AN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.MAKE_AN_ORDER_BUTTON)

    @pytest.mark.parametrize("pages_with_link_to_login_page", [
        (REGISTER_PAGE_URL),
        (FORGOT_PASSWORD_URL)
    ])
    def test_login_from_register_page_success(self, driver, existed_user, pages_with_link_to_login_page):
        driver.get(pages_with_link_to_login_page)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LINK_TO_LOGIN_PAGE))
        driver.find_element(*TestLocators.LINK_TO_LOGIN_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.EMAIL_INPUT_FIELD))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existed_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existed_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_AN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.MAKE_AN_ORDER_BUTTON)
