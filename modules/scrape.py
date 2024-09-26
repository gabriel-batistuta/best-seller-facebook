from typing import Union
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from time import sleep
import json
from utils import *

class Facebook():
    def __init__(self, name, email, password, url):
        self.name = name
        self.email = email
        self.password = password
        self.url = url

class Scraper():
    def __init__(self, facebook:Facebook):
        self.fb = facebook
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = Chrome(options=chrome_options)

    def wait_20s(self, driver, attr_type, attr_value, timeout=20):
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((attr_type, attr_value))
        )

    def login(self):
        login_url = 'https://www.facebook.com/'
        self.driver.get(login_url)
        self.wait_20s(self.driver, By.ID, 'email').send_keys(self.fb.email)
        self.wait_20s(self.driver, By.ID, 'pass').send_keys(self.fb.password)
        self.wait_20s(self.driver, By.NAME, 'login').click()

    def search_marketplace(self, query, location, min_value=None, max_value=None):
        with open('tree.json', 'r') as f:
            tree = json.load(f)
        sleep(10)
        self.driver.get('https://www.facebook.com/marketplace')
        search_bar = self.wait_20s(self.driver, By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/span/div/div/div/div/label/input')
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.ENTER)
        min_input = self.wait_20s(self.driver, By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/span[1]/label/input')
        min_input.send_keys(str(min_value))
        max_input = self.wait_20s(self.driver, By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/span[2]/label/input')
        max_input.send_keys(str(max_value))

        location_list = self.wait_20s(self.driver, By.CSS_SELECTOR, '.x1xfsgkm > div:nth-child(1) > div:nth-child(2)')
        sleep(20)
        elements = location_list.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/div')
        print(len(elements))
        objs = []
        for i in elements:
            if i.text.strip() == "":
                pass
            else:
                print(green(i.text.split('\n')))
                # for i in i.text.split('\n'):
                pc = i.text.split('\n')
                if len(pc) == 4:
                    pc.pop(0)
                objs.append({
                    "preço":pc[0],
                    "descricao":pc[1],
                    "cidade":pc[2],
                    "imagem":i.find_element(By.TAG_NAME, 'img').get_attribute('src')
                })
                # objs.extend(i.text.split('\n'))
        with open('db.json','w') as file:
            json.dump({"data":objs}, file, indent=4, ensure_ascii=False)
        sleep(20)


if __name__ == '__main__':
    with open('keys.json', 'r') as f:
        keys = json.load(f)
    fb = Facebook(keys['name'], keys['email'], 
                  keys['password'], keys['url'])
    print(f'{red("Crawling")} - {yellow(fb.url)}')

    scraper = Scraper(fb)
    scraper.login()
    scraper.search_marketplace('Notebook', 'Los Angeles', 2500, 5000)