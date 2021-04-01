# Roubando no cookieClicker

from selenium import webdriver
import time

chrome_driver = "D:\Downloads\chromedriver_win32\chromedriver.exe"
brave = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'

# Para funcionar no brave
option = webdriver.ChromeOptions()
option.binary_location = brave

# -- Voltando ao padrão
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element_by_id('cookie')

painel_direito = driver.find_elements_by_css_selector('#rightPanel div')


def jogo():
    contador = 5
    timeout_start = time.time()
    while time.time() < timeout_start + contador:
        cookie.click()
    comprar()


def comprar():
    loja = [i for i in driver.find_elements_by_css_selector("#store div")]
    loja_ind = [i for i in driver.find_elements_by_css_selector(".grayed")]
    item_caro = loja[len(loja) - len(loja_ind) - 1]
    item_caro.click()
    jogo()


jogo()
