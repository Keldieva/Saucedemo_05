from pages.login_page import LoginPage
import pytest
from locators.locators import LoginLocators as ll


class TestSample1:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_sample1(self, driver):
        lp = LoginPage(driver)
        assert lp.login_title() == ll.title
