# Importa el controlador
from selenium import webdriver
# Importa la clase de la página de inicio de sesión
from LoginPageAround import LoginPageAround

class Test:
    driver = None

    @classmethod
    def setup_class(cls):
        # Crea un controlador para Chrome
        cls.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get('https://around-v1.nm.tripleten-services.com/signin?lng=es')
        # Crea un objeto de página para la página de inicio de sesión
        login_page = LoginPageAround(self.driver)
        # Iniciar sesión
        login_page.login('hola0@gmail.com', 'Pruebas123')

    @classmethod
    def teardown_class(cls):
        # Cerrar el navegador
        cls.driver.quit()