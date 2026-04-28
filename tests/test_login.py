import pytest
from pages.login_page import LoginPage

def test_successfull_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user","secret_sauce")
    assert driver.title == "Swag Labs"


def test_login_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user","secret_sauce")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user","wrong_password")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"

def test_login_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("" , "secret_sauce")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username is required"

def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Password is required"

def test_login_empty_username_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("","")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username is required"

def test_login_locked_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Sorry, this user has been locked out."

def test_find_error_message_element(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    element = login_page.find_element(login_page.ERROR_SECTION)
    assert element.is_displayed()
