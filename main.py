from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv

load_dotenv()

def main():
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    cnpj = str(os.getenv("CNPJ"))
    password = str(os.getenv("PASSWORD"))

    browser.get('https://suzano.ginfes.com.br/')
    browser.find_element(
        'xpath', '//*[@id="principal"]/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[1]'
    ).click()
    browser.find_element('xpath', '//*[@id="ext-gen29"]').send_keys(cnpj)
    browser.find_element('xpath', '//*[@id="ext-gen33"]').send_keys(password)
    browser.find_element('xpath', '//*[@id="ext-gen51"]').click()

if __name__ == '__main__':
    main()
