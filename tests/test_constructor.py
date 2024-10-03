from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from elements_to_find import TestLocators
from selenium.webdriver.common.by import By
import pytest


class TestConstructor:
    @pytest.mark.parametrize('section_button,status_of_construction_button', [
        [TestLocators.SAUCES_CONSTRUCTION_BUTTON, TestLocators.STATUS_OF_SAUCES_CONSTRUCTION_BUTTON],
        [TestLocators.TOPPINGS_CONSTRUCTION_BUTTON, TestLocators.STATUS_OF_TOPPINGS_CONSTRUCTION_BUTTON]
    ])
    def test_transition_to_the_sauces_and_topping_sections_by_clicking_on_section_buttons_section_selected(self, driver, main_page, section_button, status_of_construction_button):
        driver.find_element(*section_button).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                status_of_construction_button, "class", "current"
            )
        )

        assert 'current' in driver.find_element(*status_of_construction_button).get_attribute('class')

    def test_transition_to_the_puns_sections_by_clicking_on_puns_button_section_selected(self, driver, main_page):
        driver.find_element(*TestLocators.SAUCES_CONSTRUCTION_BUTTON).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                TestLocators.STATUS_OF_SAUCES_CONSTRUCTION_BUTTON, "class", "current"
            )
        )

        driver.find_element(*TestLocators.PUNS_CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                TestLocators.STATUS_OF_PUNS_CONSTRUCTOR_BUTTON, "class", "current"
            )
        )

        assert 'current' in driver.find_element(*TestLocators.STATUS_OF_PUNS_CONSTRUCTOR_BUTTON).get_attribute('class')
