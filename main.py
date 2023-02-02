from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pyautogui
import pyperclip
import os
import time

load_dotenv()

cnpj_owner = str(os.getenv("CNPJ_OWNER"))
cnpj_owner_dots = str(os.getenv("CNPJ_OWNER_DOTS"))
email_owner = str(os.getenv("EMAIL_OWNER"))
email_password = str(os.getenv("EMAIL_PASSWORD"))
ginfes_password = str(os.getenv("GINFES_PASSWORD"))

account_agency = str(os.getenv("ACCOUNT_AGENCY"))
account_number = str(os.getenv("ACCOUNT_NUMBER"))
account_name = str(os.getenv("ACCOUNT_NAME"))

bank_name = str(os.getenv("BANK_NAME"))
bank_code = str(os.getenv("BANK_CODE"))

cnpj_taker = str(os.getenv("CNPJ_TAKER"))
email_taker = str(os.getenv("EMAIL_TAKER"))

salary = str(os.getenv("SALARY"))
description_nfse = "Reparação e manutenção de computadores e de equipamentos periféricos."

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


def main():
    browser.get('https://suzano.ginfes.com.br/')
    login()
    search_taker()
    services_provided()
    time.sleep(5)
    issue()
    
    browser.get('https://mail.google.com/mail/')
    download()
    time.sleep(20)
    send_email()
    

def login():
    time.sleep(4)

    browser.find_element(By.XPATH, '//*[@id="principal"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/img').click()
    browser.find_element(By.XPATH, '//*[@id="ext-gen29"]').send_keys(cnpj_owner)
    browser.find_element(By.XPATH, '//*[@id="ext-gen33"]').send_keys(ginfes_password)

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
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div/div/div/table[1]/tbody/tr/td/div/div/div/form/fieldset/div/div/fieldset[1]/div/div/table/tbody/tr[2]/td/div/div/div/div/div[1]/div/div/div/div[1]/input').send_keys(cnpj_taker)
    
    time.sleep(1)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div/div/div/table[1]/tbody/tr/td/div/div/div/form/fieldset/div/div/fieldset[1]/div/div/table/tbody/tr[2]/td/div/div/div/div/div[2]/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div/div/div/table[2]/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()
    
    
def services_provided():
    time.sleep(2)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/fieldset[3]/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div/img').click()
    
    time.sleep(1)
    pyautogui.press('enter')
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/fieldset[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/textarea').send_keys(description_nfse)
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/fieldset[5]/div/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/input').send_keys(salary)
    
    time.sleep(2)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[2]/div/div/div/div/div/form/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()

    
def issue():    
    time.sleep(2)
    
    browser.find_element(By.XPATH, '/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td/div/div[2]/div/div[3]/div/div/div/div/div/form/table[2]/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]/em/button').click()

    time.sleep(10)
    
    browser.find_element(By.XPATH, '/html/body/div[10]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button').click()
    browser.find_element(By.XPATH, '/html/body/div[21]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button').click()


def download():    
    pyautogui.click(x=2562, y=250)
    time.sleep(1)
    pyautogui.click(x=2735, y=213)
    pyautogui.click(x=2820, y=385)


def send_email():
    body_email = f"""
    Segue NFS-e em anexo.\n
    
    Estes são os dados da minha conta no {bank_name}:
    BANCO {bank_name} - {bank_code}
    {account_name}
    CNPJ (Pix): {cnpj_owner_dots}
    Agência: {account_agency}
    Conta: {account_number}
    """
    
    pyautogui.click(x=2195, y=452)
    time.sleep(5)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(email_owner)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(email_password)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()
    time.sleep(5)
    browser.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div[1]/div[1]/div/div').click()
    time.sleep(1)
    pyperclip.copy(email_taker)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyperclip.copy('NFS-e')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyperclip.copy(body_email)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(x=2195, y=452)
    pyautogui.click(x=2820, y=381)
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')
    
    
if __name__ == '__main__':
    main()
