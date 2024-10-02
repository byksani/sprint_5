from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from elements_to_find import TestLocators


class TestRegistration:
    def test_register_new_user_with_email_name_password_success(self, driver, register_page, new_correct_user):
        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys(new_correct_user.name)
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(new_correct_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(new_correct_user.password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/login'))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_register_new_user_short_password_error_displays(self, driver, register_page, new_correct_user):
        driver.find_element(*TestLocators.NAME_INPUT_FIELD).send_keys(new_correct_user.name)
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(new_correct_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys('12345')
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

        assert driver.find_element(*TestLocators.INPUT_ERROR_TEXT).text == 'Некорректный пароль'