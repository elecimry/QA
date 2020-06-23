import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    yield driver
    driver.quit()
