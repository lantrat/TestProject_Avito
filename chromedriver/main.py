from selenium import webdriver
import time

url = 'https://www.avito.ru/avito-care/eco-impact'
driver = webdriver.Chrome()


try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
