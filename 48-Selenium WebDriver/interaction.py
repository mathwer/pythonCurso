from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "D:\Downloads\chromedriver_win32\chromedriver.exe"
brave = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'

# Para funcionar no brave
option = webdriver.ChromeOptions()
option.binary_location = brave

# -- Voltando ao padrão
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

artigos_qt = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(artigos_qt.text)


todos_portais = driver.find_element_by_link_text('All portals')
# todos_portais.click()

busca = driver.find_element_by_name('search')
busca.send_keys('Python')
busca.send_keys(Keys.ENTER)

#  -------------- Inserir dados em um formulário
driver.get('https://secure-retreat-92358.herokuapp.com/')
nome = driver.find_element_by_name('fName')
nome.send_keys('Podolmos')
sobrenome = driver.find_element_by_name('lName')
sobrenome.send_keys('Paminondas')
email = driver.find_element_by_name('email')
email.send_keys('ppaminondas@podolmail.com')
botao = driver.find_element_by_css_selector('form button')
botao.click()

# driver.quit()
