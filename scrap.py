from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

# # function to take care of downloading file
# def enable_download_headless(browser,download_dir):
#     browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
#     params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
#     browser.execute("send_command", params)

options = Options()
options.binary_location = r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe"
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options, executable_path="chromedriver" )
driver.get('https://www.chess.com/login')

driver.find_element_by_name("_username").send_keys("hesela5462")
time.sleep(0.2)
driver.find_element_by_name("_password").send_keys("chesscrap")
time.sleep(0.4)
driver.find_element_by_name("login").click()

driver.get('https://www.chess.com/games/archive/hikaru')
opening = Select(driver.find_element_by_name('opening'))
openings = []
for Openingoptions in opening.options:
    openings.append(Openingoptions.text)
driver.close

# Strips all the whitespaces and /n character
openings.remove(openings[0])
for i in range(len(openings)):
    openings[i] = openings[i].strip()


