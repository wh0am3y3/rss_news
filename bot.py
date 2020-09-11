from selenium.webdriver import Firefox
from time import sleep


def browser():
    driver = Firefox(executable_path="./geckodriver")
    driver.get("http://127.0.0.1:5000")
    sleep(10)
    driver.close()
    quit()


if __name__ == '__main__':
    try:
        browser()
    except Exception as e:
        print(e)
        quit()
