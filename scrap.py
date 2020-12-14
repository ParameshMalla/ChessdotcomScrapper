from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver" )
driver.get('http://google.com/')