from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Profile_Page:
    profile_edit_button = (By.CLASS_NAME, 'profile__edit-button')
    profile_description_field = (By.ID, 'owner-description')
    #Se utiliza el punto por que la clase se sepran y se toma como 2 clases, la clase es button popup__button
    button_save = (By.CLASS_NAME, 'button.popup__button')

    def __init__(self, driver):
        self.driver = driver

    def click_profile_edit_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.profile_edit_button)
        ).click()

    def set_description(self, description):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.profile_description_field)
        ).send_keys(description)

    def click_button_save(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.button_save)
        ).click()


