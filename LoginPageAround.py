from selenium.webdriver.common.by import By


class LoginPageAround:
    # El localizador del campo Correo electrónico
    email_field = (By.ID, 'email')
    # El localizador del campo Contraseña
    password_field = (By.ID, 'password')
    # El localizador del botón Iniciar sesión
    sign_in_button = (By.CLASS_NAME, 'auth-form__button')
    # Agrega aquí un localizador para el botón Registrarse
    register_button = (By.CLASS_NAME, 'auth-form__button')

    # El constructor de clase
    def __init__(self, driver):
        self.driver = driver

    # El metodo comprueba si se puede hacer clic en el botón Iniciar sesión
    def check_sign_in_is_enabled(self):
        return self.driver.find_element(*self.sign_in_button).is_enabled()

    # El metodo hace clic en el botón Iniciar sesión
    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    # El metodo hace clic en el botón Registrarse
    def click_registration_button(self):
        self.driver.find_element(*self.register_button).click()

    # El metodo valida el texto en el botón Registrarse
    def check_text_registration_button(self):
        registration_button_text = self.driver.find_element(*self.register_button).text
        assert registration_button_text == "Registrarse"