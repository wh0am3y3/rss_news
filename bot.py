from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = False
# firefox_capabilities['binary'] = '/usr/bin/firefox'
binary = FirefoxBinary("/usr/lib/firefox/firefox")
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(
        capabilities=firefox_capabilities,
        firefox_binary=binary,
        firefox_profile=fp,
        executable_path="./geckodriver"
        )
driver.get("http://www.google.com")
# driver.close()
# driver.quit()
