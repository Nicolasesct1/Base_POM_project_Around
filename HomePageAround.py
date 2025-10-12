from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class HomePageAround:
    # El localizador del botón Agregar
    add_new_place_button = (By.CLASS_NAME, 'profile__add-button')
    # El localizador del campo Nombre
    name_field = (By.NAME, 'name')
    # El localizador del campo Enlace a la imagen
    link_to_picture_field = (By.NAME, 'link')
    # El localizador del botón Guardar
    save_button = (By.XPATH, ".//form[@name='new-card']/button[text()='Guardar']")
    header_email = (By.CLASS_NAME, 'header__user')

    def __init__(self, driver):
        self.driver = driver

    # El metodo hace clic en el botón Agregar
    def click_add_new_place_button(self):
        self.driver.find_element(*self.add_new_place_button).click()

    # El metodo introduce el nombre del nuevo lugar
    def set_name(self):
        new_title = "Lugar1"
        self.driver.find_element(*self.name_field).send_keys(new_title)

    # El metodo introduce un enlace a la imagen
    def set_link_to_picture_field(self):
        self.driver.find_element(*self.link_to_picture_field).send_keys("Enlace a la imagen")

    # El metodo hace clic en el botón Guardar
    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    # El paso para agregar un nuevo lugar
    def add_new_place(self):
        self.click_add_new_place_button()
        self.set_name()
        self.set_link_to_picture_field()
        self.click_save_button()

    def check_head_email(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.header_email)
        )
        return element.text