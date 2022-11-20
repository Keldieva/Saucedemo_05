from selenium.webdriver.common.by import By


class LoginLocators:
    input_username = (By.ID, 'user-name')
    input_password = (By.ID, 'password')
    login_btn = (By.ID, 'login-button')
    hamburger_btn = (By.ID, 'react-burger-menu-btn')
    logout_btn = (By.ID, 'logout_sidebar_link')
    title = 'Swag Labs'


class InventoryLocators:
    ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-bike-light")
    CART_BUTTON = (By.ID, 'shopping_cart_container')
    CART_BAGE = (By.CLASS_NAME, 'shopping_cart_badge')
    ALL_PRODUCTS = (By.CLASS_NAME, 'inventory_item_name')
    AZ_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[1]',
    )
    ZA_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[2]',
    )
    ASC_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]',
    )
    DESC_BUTTON = (
        By.XPATH,
        '//*[@id="header_container"]/div[2]/div[2]/span/select/option[4]',
    )
