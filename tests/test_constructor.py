from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from elements_to_find import TestLocators
from selenium.webdriver.common.by import By
import pytest


class TestConstructor:
    @pytest.mark.parametrize("section_button", [
        TestLocators.SAUCES_CONSTRUCTION_BUTTON,
        TestLocators.TOPPINGS_CONSTRUCTION_BUTTON
    ])
    def test_transition_to_the_sauces_and_topping_sections_by_clicking_on_section_buttons_section_selected(self, driver, main_page, section_button):
        active_button = driver.find_element(*section_button)
        active_button.click()

        section_status = active_button.find_element(By.XPATH, "./parent::div")

        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                (By.XPATH, f"({section_button[1]})/parent::div"), "class", "current"
            )
        )

        assert 'current' in section_status.get_attribute('class')

    def test_transition_to_the_puns_sections_by_clicking_on_puns_button_section_selected(self, driver, main_page):
        driver.find_element(*TestLocators.SAUCES_CONSTRUCTION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                (By.XPATH, f"({TestLocators.SAUCES_CONSTRUCTION_BUTTON[1]})/parent::div"), "class", "current"
            )
        )

        active_button = driver.find_element(*TestLocators.PUNS_CONSTRUCTOR_BUTTON)
        active_button.click()

        section_status = active_button.find_element(By.XPATH, "./parent::div")

        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                (By.XPATH, f"({TestLocators.PUNS_CONSTRUCTOR_BUTTON[1]})/parent::div"), "class", "current"
            )
        )

        assert 'current' in section_status.get_attribute('class')