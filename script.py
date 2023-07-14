from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_profile_path = r"C:\Users\vaibh\AppData\Local\Google\Chrome\User Data"
user_agent = r"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
chrome_binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_path = r"D:\Python\Selenium webdriver\chromedriver.exe"
delay_before_browser_close = 2
wait_timeout = 5
about_chrome_selector = "#about-menu" 

URL = f"chrome://settings/appearance"
URL2 = f"chrome://settings/onStartup"
profile_name = 'HENG_Chrome-001'
start = time.perf_counter()
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument('--disable-software-rasterizer')
chrome_options.add_argument(f"--profile-directory={profile_name}")
chrome_options.add_argument("disable-extensions")
chrome_options.binary_location=chrome_binary_location
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s,options=chrome_options)
driver.get(URL)
element  = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'appearance']").find_element(By.TAG_NAME,"settings-appearance-page").shadow_root.find_element(By.CSS_SELECTOR,"settings-toggle-button[label = 'Show home button']")
WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(element)).click()
element  = driver.find_element(By.XPATH, "/html/body/settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'appearance']").find_element(By.TAG_NAME,"settings-appearance-page").shadow_root
select_custom_web_url = element.find_element(By.CSS_SELECTOR, "controlled-radio-button#custom-input").shadow_root.find_element(By.CSS_SELECTOR,"div.disc-border")
WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(select_custom_web_url)).click()
select_custom_web_url = element.find_element(By.CSS_SELECTOR, "home-url-input#customHomePage").shadow_root.find_element(By.CSS_SELECTOR,"cr-input#input").shadow_root.find_element(By.CSS_SELECTOR, "input#input")
select_custom_web_url.send_keys("fb.com")
select_custom_web_url.send_keys(Keys.ENTER)
time.sleep(1)
driver.get(URL2)
open_a_specific_page_radio = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'onStartup']").find_element(By.TAG_NAME,"settings-on-startup-page").shadow_root.find_element(By.CSS_SELECTOR,"controlled-radio-button[label = 'Open a specific page or set of pages']").shadow_root.find_element(By.CSS_SELECTOR, "#button")
WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(open_a_specific_page_radio)).click()
add_a_new_page_button = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'onStartup']").find_element(By.TAG_NAME,"settings-on-startup-page").shadow_root.find_element(By.CSS_SELECTOR, "settings-startup-urls-page").shadow_root.find_element(By.CSS_SELECTOR,'#addPage > a')
WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(add_a_new_page_button)).click()
add_url_text_box = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'onStartup']").find_element(By.TAG_NAME,"settings-on-startup-page").shadow_root.find_element(By.CSS_SELECTOR, "settings-startup-urls-page").shadow_root.find_element(By.CSS_SELECTOR, 'settings-startup-url-dialog').shadow_root.find_element(By.CSS_SELECTOR,'#url').shadow_root.find_element(By.CSS_SELECTOR, '#input')
WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(add_url_text_box))
add_url_text_box.send_keys("fb.com")
add_url_text_box.send_keys(Keys.ENTER)
time.sleep(2)
