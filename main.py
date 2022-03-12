# OGUsers Autobumper
import configparser, time, warnings, os, random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import element_located_selection_state_to_be, presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from configparser import ConfigParser

# Read config file and grab username/password
config = ConfigParser()
config.read('config.ini')
username = config.get('data','username')
password = config.get('data','password')
channel = config.get('data','channel')
min = float(config.get('data','min'))
max = float(config.get('data','max'))

# Disable python logging to console
warnings.filterwarnings("ignore")
clear = lambda: os.system('cls')
clear()
# Setup web-driver
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--hide-scrollbars')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=3')
options.add_argument('--disable-infobars')
options.add_argument('--start-maximized')
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
clear()

# TODO
class User:
    def login(self):
        try:
            driver.get(channel)
            time.sleep(1)
            driver.find_element_by_name('email').send_keys(username)
            driver.find_element_by_name('password').send_keys(password)
            driver.find_element_by_css_selector("[type=submit]").click()

            wait = WebDriverWait(driver, 300)
            wait.until(presence_of_element_located((By.CLASS_NAME, 'toolbar-3_r2xA')))
        except Exception as e:
            print(e)
            time.sleep(60)
    
    def guessing(self):
        guesses = []
        while True:
            try:
                guess = random.randint(min, max)
                if guess not in guesses:
                    guesses.append(guess)
                    print("[+] Trying " + str(guess))
                    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]').send_keys(guess, Keys.ENTER)
                    time.sleep(3)
            except Exception as error:
                print(error)
                break

randInt = User()
print('[-] Logging in...')
randInt.login()
print('[+] Logged in...')
print('[+] Starting Guesser...')
randInt.guessing()