from selenium import webdriver

chrome_driver = "D:\Downloads\chromedriver_win32\chromedriver.exe"
brave = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'

# Para funcionar no brave
option = webdriver.ChromeOptions()
option.binary_location = brave

# -- Voltando ao padrão
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)

driver.get('https://www.amazon.com.br/Driving-Logitech-Joysticks-Controles-Computador/dp/B00Z0UWV3O/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=th8a&qid=1617126899&sr=8-1')

preco = driver.find_element_by_id('price_inside_buybox')
print(preco.text)
# Fecha a aba que foi aberta
# driver.close()

# --- Outros exemplos para encontrar elementos

driver.get('https://python.org/')

barra_busca = driver.find_element_by_name('q')
print(barra_busca.get_attribute('placeholder'))

logo = driver.find_element_by_class_name('python-logo')

doc_link = driver.find_element_by_css_selector('.documentation-widget a')
print(doc_link.text)

link = driver.find_element_by_xpath('//*[@id="container"]/li[4]/ul/li[13]/a')
print(link.text)

# Fecha o browser por completo
driver.quit()
