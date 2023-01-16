from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def accept_cookies(driver):
    """" agree with cookies terms and conditions
    :param driver: selenium driver used to browse application
    :return: none"""

    try:
        agree_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, './/button/span[contains (text(), "AGREE")]')))
    except BaseException as e:
        # print exception.
        print(e)
        agree_button = None
    if agree_button:
        agree_button.click()

