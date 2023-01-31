from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pyautogui
import os
import time

load_dotenv()

cnpj = str(os.getenv("CNPJ"))
password = str(os.getenv("PASSWORD"))
cnpj_s2b = str(os.getenv("CNPJ_S2B"))
salary = str(os.getenv("SALARY"))

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def main():    
    browser.get('https://suzano.ginfes.com.br/')
    
    login()
    search_taker()
    services_provided()

    time.sleep(5)


def login():
    time.sleep(4)

    browser.find_element(By.XPATH, '//*[@id="principal"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/img').click()
    browser.find_element(By.XPATH, '//*[@id="ext-gen29"]').send_keys(cnpj)
    browser.find_element(By.XPATH, '//*[@id="ext-gen33"]').send_keys(password)

    time.sleep(2)

    browser.find_element(By.XPATH, '//*[@id="ext-gen51"]').click()

    time.sleep(3)

    browser.refresh()
    
    time.sleep(4)
    
    browser.find_element(By.XPATH, '//*[@id="principal"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/img').click()
    
    
def search_taker():
    time.sleep(2)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/img').click()
    
    time.sleep(2)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div/div/div/table[1]/tbody/tr/td/div/div/div/form/fieldset/div/div/fieldset[1]/div/div/table/tbody/tr[2]/td/div/div/div/div/div[1]/div/div/div/div[1]/input').send_keys(cnpj_s2b)
    
    time.sleep(1)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div/div/div/table[1]/tbody/tr/td/div/div/div/form/fieldset/div/div/fieldset[1]/div/div/table/tbody/tr[2]/td/div/div/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div/div/div/table[2]/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()
    
    
def services_provided():
    time.sleep(2)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/fieldset[3]/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/img').click()
    
    time.sleep(1)
    pyautogui.press('enter')
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/fieldset[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/textarea').send_keys("DESCRIÇÃO")
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/fieldset[5]/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/input').send_keys(salary)
    
    time.sleep(1)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()


if __name__ == '__main__':
    main()
