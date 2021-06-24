from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(executable_path='/Users/levreyn/Yandex.Disk.localized/python/selenium/driver/chromedriver',
                          options=options)

try:
    driver.get(url='https://www.avito.ru/sankt-peterburg/avtomobili/audi?cd=1')
    time.sleep(5)
    # print(f'url now {driver.current_url}')
    items = driver.find_elements_by_xpath("//div[@class='photo-slider-item-15V4q photo-slider-keepImageRatio-1bSLF']")

    for i in range(0, len(items)):
        items[i].click()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        if i == 4:
            time.sleep(5)
        try:
            price = driver.find_element_by_class_name('item-price-wrapper')
            # price = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[5]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span')
        except:
            print('blet')
            price = driver.find_element_by_xpath('//*[@id="price-value"]/span')
        print(f'price is {price.text}')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
