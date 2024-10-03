from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from elements_to_find import TestLocators
import pytest
from config import BASE_URL, LOGIN_PAGE_URL


class TestPersonalAccountPage:
    def test_go_to_personal_account_click_on_button_page_opened(self, driver, existed_user, authorised_existing_user):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.NAME_INPUT_FIELD))

        assert driver.find_element(*TestLocators.NAME_INPUT_FIELD).get_attribute('value') == existed_user.name

    @pytest.mark.parametrize("buttons_to_the_main_page", [
        (TestLocators.CONSTRUCTOR_BUTTON),
        (TestLocators.LOGO_BUTTON)
    ])
    def test_main_page_from_the_personal_account_constructor_or_logo_buttons_page_opened(self, driver, existed_user, authorised_existing_user, buttons_to_the_main_page):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.NAME_INPUT_FIELD))

        driver.find_element(*buttons_to_the_main_page).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAKE_AN_ORDER_BUTTON))
        assert driver.current_url == BASE_URL

    def test_logout_on_the_personal_account_page_click_button_success_logout(self, driver, existed_user, authorised_existing_user):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))

        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.current_url == LOGIN_PAGE_URL
