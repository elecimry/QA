from BaseApp import BasePage
from selenium.webdriver.common.by import By
from config import USER_EMAIL, USER_PASSWORD
from selenium.common.exceptions import NoSuchElementException 


class SeacrhLocators:
    # Локаторы основной страницы
    LOCATOR_SEARCH_FIELD = (By.ID, "search_query_top")  # Поисковая строка
    LOCATOR_SEARCH_BUTTON = (By.CLASS_NAME, "button-search")  # Кнопка Поиск
    LOCATOR_CART = (By.CLASS_NAME, "shopping_cart")  # Корзина
    LOCATOR_CONTACT = (By.ID, "contact-link")  # Контакты
    LOCATOR_NAVIGATION_BAR = (By.CLASS_NAME, "sf-with-ul")  # Блок навигации
    LOCATOR_MENU_LOGIN = (By.CLASS_NAME, "login")  # Вход в ЛК
    # Локаторы формы входа в ЛК
    LOCATOR_USER_EMAIL = (By.ID, "email")  # Логин
    LOCATOR_USER_PASSWORD = (By.ID, "passwd")  # Пароль
    LOCATOR_SIGNIN_BUTTON = (By.ID, "SubmitLogin")  # Кнопка формы входа в ЛК
    # Локаторы-детекторы входа в ЛК
    LOCATOR_MENU_LOGOUT = (By.CLASS_NAME, "logout")  # Выход из ЛК
    LOCATOR_MYACCOUNT_LINK_LIST = (By.CLASS_NAME, "myaccount-link-list")  # Ссылки ЛК
    LOCATOR_MY_WISHLIST = (By.CLASS_NAME, "lnk_wishlist")  # И еще одна ссылка из ЛК


class Helper(BasePage):

    def menu_login_click(self):
        self.find_element(SeacrhLocators.LOCATOR_MENU_LOGIN, time=2).click()

    def signin(self):
        signin_login = self.find_element(SeacrhLocators.LOCATOR_USER_EMAIL)
        signin_login.click()
        signin_login.send_keys(USER_EMAIL)
        signin_password = self.find_element(SeacrhLocators.LOCATOR_USER_PASSWORD)
        signin_password.click()
        signin_password.send_keys(USER_PASSWORD)
        self.find_element(SeacrhLocators.LOCATOR_SIGNIN_BUTTON).click()

    def main_page_locators(self):
        MainPageLocators = [
            SeacrhLocators.LOCATOR_CART,
            SeacrhLocators.LOCATOR_SEARCH_FIELD,
            SeacrhLocators.LOCATOR_SEARCH_BUTTON,
            SeacrhLocators.LOCATOR_CONTACT,
            SeacrhLocators.LOCATOR_NAVIGATION_BAR,
            SeacrhLocators.LOCATOR_MENU_LOGIN
            ]
        for locator in MainPageLocators:
            try:
                self.find_element(locator)
            except NoSuchElementException:
                return False
            return True

    def account_page_locators(self):

        AccountPageLocators = [
            SeacrhLocators.LOCATOR_MENU_LOGOUT,
            SeacrhLocators.LOCATOR_MYACCOUNT_LINK_LIST,
            SeacrhLocators.LOCATOR_MY_WISHLIST
        ]

        for locator in AccountPageLocators:
            try:
                self.find_element(locator)
            except NoSuchElementException:
                return False
            return True
