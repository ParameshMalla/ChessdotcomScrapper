from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import os

# function to take care of downloading file
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

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

def countPages(url):
    n = int(url[url.find('page=')+5:])
    return n

# Strips all the whitespaces and /n character
openings.remove(openings[0])
for i in range(len(openings)):
    openings[i] = openings[i].strip()
    openings[i] = openings[i].replace(' ','%20')
    openings[i] = openings[i].replace('-','_')
    url = "https://www.chess.com/games/archive/hikaru?gameOwner=other_game&gameType=live&opening="+openings[i]+"&timeSort=desc&gameTypes%5B0%5D=chess960&gameTypes%5B1%5D=daily"
    driver.get(url)
    if(len(driver.find_elements_by_xpath('//*[@id="games-root-index"]/div/div[1]/div/nav/button[7]'))>0):
        driver.find_element_by_xpath('//*[@id="games-root-index"]/div/div[1]/div/nav/button[7]').click()
        pageUrl = driver.current_url
        noOfPages = countPages(pageUrl)
    else:
        noOfPages = 2
    if not os.path.exists(openings[i]):
            os.makedirs(openings[i])
    pgns = os.path.join(r'D:\Programming\WebScraping\ChessdotcomScrapper', openings[i])
    enable_download_headless(driver, pgns)
    for j in range(noOfPages,0,-1):
        pageUrl = pageUrl[:pageUrl.find('page=')+5] + str(j)
        driver.get(pageUrl)
        if(len(driver.find_elements_by_xpath('//*[@id="games-root-index"]/div/div[2]/div/table/thead/tr/th[7]/input')) > 0):
            driver.find_element_by_xpath('//*[@id="games-root-index"]/div/div[2]/div/table/thead/tr/th[7]/input').click()
        elif(len(driver.find_elements_by_xpath('//*[@id="games-root-index"]/div/div[1]/div/table/thead/tr/th[7]/input')) > 0):
            driver.find_element_by_xpath('//*[@id="games-root-index"]/div/div[1]/div/table/thead/tr/th[7]/input').click()
            j = 1
            pageUrl = pageUrl[:pageUrl.find('page=')+5] + str(j)
            driver.get(pageUrl)
        driver.find_element_by_xpath('//*[@id="games-root-index"]/div/header/div/button/div/span').click()
        src = os.path.join(pgns,'chess_com_games_2020-12-19.pgn')
        dst = os.path.join(pgns, openings[i]+str(j)+'.pgn')
        while not os.path.exists(src):
            time.sleep(0.2)
        os.rename(src,dst)

driver.close

