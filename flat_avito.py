from selenium import webdriver
import time
import datetime
import json
options = webdriver.ChromeOptions()
options.add_argument(
    'usrer-agent=Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(executable_path='/Users/levreyn/Yandex.Disk.localized/python/selenium/driver/chromedriver',
                          options=options)

try:
    start = datetime.datetime.now()
    driver.get(url='https://www.avito.ru/sankt-peterburg/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1')
    driver.implicitly_wait(5)
    items = driver.find_elements_by_class_name('iva-item-content-m2FiN')
    count = 0
    lst_data_main = []
    for item in items:
        # переходим на вкладку
        item.click()
        driver.switch_to.window(driver.window_handles[1])
        driver.implicitly_wait(5)
        # сбор информации
        price = driver.find_element_by_class_name('item-price-wrapper').text

        info_lst = driver.find_elements_by_class_name('item-params-list-item')
        info_lst_need = []
        for info_elem in info_lst:
            info_lst_need.append(info_elem.text)
        adress = driver.find_element_by_class_name('item-address__string').text
        lst_data_main.append({
            'price': price,
            'info': info_lst_need,
            'adress': adress
        })
        with open('data_main.json', 'w') as file:
            json.dump(lst_data_main, file, indent=2, ensure_ascii=False)
        # обратно переходим на главную вкладку
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(5)
        count += 1
        print(f'собранно страниц {count}  из {len(items)}')


except Exception as ex:
    print(ex)
finally:
    finish = datetime.datetime.now()
    print(f'столько времени заняла работа {finish - start}')
    driver.close()
    driver.quit()
