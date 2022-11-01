import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import AuthorsBaseTest


@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = 'pass'
        user = User.onjects.create_user(
            username='my_user',
            password=string_password
        )

        # Usuario abre a pag de login
        self.browser.get(self.live_server_url + reverse('authors:login'))

        # usuario ve o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')
        username_field = self.get_by_placeholder(form, 'Type your username')
        password_field = self.get_by_placeholder(form, 'Type your password')

        # usuario preenche os campos
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        # usuario envia o formulario
        form.submit()

        # usuario ve a mensagem de login com sucesso e seu nome
        self.assertIn(
            f'You are logged in with {user.username}',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_login_create_404_if_not_POST_method(self):
        self.browser.get(
            self.live_server_url +
            reverse('authors:login_create')
        )

        self.assertIn(
            'Not Found',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_is_invalid(self):
        # usuario abre a pagina de login
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # usuario ve o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # e tenta enviar valores vazios
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys(' ')
        password.send_keys(' ')

        # ve uma mensagem de erro na tela
        self.assertIn(
            'Invalid username or password',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )

    def test_form_login_is_invalid_credentials(self):
        # usuario abre a pagina de login
        self.browser.get(
            self.live_server_url + reverse('authors:login')
        )

        # usuario ve o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, 'main-form')

        # e tenta enviar valores com dados que nao correspondem
        username = self.get_by_placeholder(form, 'Type your username')
        password = self.get_by_placeholder(form, 'Type your password')
        username.send_keys('Invalid_user')
        password.send_keys('Invalid_password')

        # ve uma mensagem de erro na tela
        self.assertIn(
            'Invalid credentials',
            self.browser.find_element(By.TAG_NAME, 'body').text
        )
