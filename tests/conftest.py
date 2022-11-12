import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import conf


@pytest.fixture()
def b(browser):
    driver = None
    if browser == 'chrome':
        o = webdriver.ChromeOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Chrome(
            service=ChromiumService(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=o,
        )
    else:
        o = webdriver.FirefoxOptions()
        o.headless = conf.BROWSER_HEADLESS
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()), options=o
        )
    return driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="firefox",
        help="define browser: chrome or firefox, --browser=chrome",
    )


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True)
def g(b):
    print('\n*** start fixture = setup ***\n')
    b.get(conf.URL)
    yield b
    b.quit()
    print('\n*** end fixture = teardown ***\n')


def pytest_html_report_title(report):
    report.title = "Kate Fox"
