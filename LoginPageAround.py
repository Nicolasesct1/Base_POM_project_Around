from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.ID, 'email')
    # El localizador del campo Contraseña
    password_field = (By.ID, 'password')
    # El localizador del botón Iniciar sesión
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')

    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # El metodo comprueba si se puede hacer clic en el botón Iniciar sesión
    def check_sign_in_is_enabled(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.sign_in_button)
        ).is_enabled()

    # El metodo rellena el campo Correo electrónico
    def set_email(self, email):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.email_field)
        ).send_keys(email)

    # El metodo rellena el campo Contraseña
    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.password_field)
        ).send_keys(password)

    # El metodo hace clic en el botón Iniciar sesión
    def click_sign_in_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.sign_in_button)
        ).click()

    # El metodo de inicio de sesión combina el correo electrónico, la contraseña y el clic del botón
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()