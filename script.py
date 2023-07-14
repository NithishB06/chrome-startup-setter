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
import yaml
import subprocess

def kill_chrome_processes():
    subprocess.call("TASKKILL /f  /IM  CHROME.EXE", 
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT)

    subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE", 
    stdout=subprocess.DEVNULL,
    stderr=subprocess.STDOUT) 


def set_browser_preferences():
    try:
        for profile_number in range(start_profile_number, end_profile_number + 1):
            if profile_number < 100:
                if profile_number < 10:
                    profile_end_string = "00" + str(profile_number)
                else:
                    profile_end_string = "0" + str(profile_number)
            else:
                profile_end_string = str(profile_number)

            profile_name = profile_pattern + profile_end_string

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

            driver.get(appearance_url)

            time.sleep(1)
            show_home_button  = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, "settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'appearance']").find_element(By.TAG_NAME,"settings-appearance-page").shadow_root.find_element(By.CSS_SELECTOR,"settings-toggle-button[label = 'Show home button' i]")
            WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(show_home_button)).click()

            toggle_button_shadow_root = driver.find_element(By.XPATH, "/html/body/settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'appearance']").find_element(By.TAG_NAME,"settings-appearance-page").shadow_root
            select_custom_web_url_radio_button = toggle_button_shadow_root.find_element(By.CSS_SELECTOR, "controlled-radio-button#custom-input").shadow_root.find_element(By.CSS_SELECTOR,"div.disc-border")
            WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(select_custom_web_url_radio_button)).click()

            select_custom_web_url_text_box = toggle_button_shadow_root.find_element(By.CSS_SELECTOR, "home-url-input#customHomePage").shadow_root.find_element(By.CSS_SELECTOR,"cr-input#input").shadow_root.find_element(By.CSS_SELECTOR, "input#input")
            select_custom_web_url_text_box.send_keys("fb.com")
            select_custom_web_url_text_box.send_keys(Keys.ENTER)
            time.sleep(1)

            driver.get(startup_url)

            open_a_specific_page_radio = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'onStartup']").find_element(By.TAG_NAME,"settings-on-startup-page").shadow_root.find_element(By.CSS_SELECTOR,"controlled-radio-button[label = 'Open a specific page or set of pages']").shadow_root.find_element(By.CSS_SELECTOR, "#button")
            WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(open_a_specific_page_radio)).click()

            add_a_new_page_button = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'onStartup']").find_element(By.TAG_NAME,"settings-on-startup-page").shadow_root.find_element(By.CSS_SELECTOR, "settings-startup-urls-page").shadow_root.find_element(By.CSS_SELECTOR,'#addPage > a')
            WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(add_a_new_page_button)).click()

            add_url_text_box = driver.find_element(By.CSS_SELECTOR, "body > settings-ui").shadow_root.find_element(By.CSS_SELECTOR, "settings-main#main").shadow_root.find_element(By.CSS_SELECTOR, " settings-basic-page.cr-centered-card-container").shadow_root.find_element(By.CSS_SELECTOR,"settings-section[section = 'onStartup']").find_element(By.TAG_NAME,"settings-on-startup-page").shadow_root.find_element(By.CSS_SELECTOR, "settings-startup-urls-page").shadow_root.find_element(By.CSS_SELECTOR, 'settings-startup-url-dialog').shadow_root.find_element(By.CSS_SELECTOR,'#url').shadow_root.find_element(By.CSS_SELECTOR, '#input')
            WebDriverWait(driver, wait_timeout).until(EC.element_to_be_clickable(add_url_text_box))
            add_url_text_box.send_keys("fb.com")
            add_url_text_box.send_keys(Keys.ENTER)

            time.sleep(1)
            driver.quit()
    
    except Exception as err:
        if driver:
            driver.quit()
        print(err)


if __name__ == '__main__':
    with open('./config.yml') as file:
        CONFIG = yaml.load(file, Loader=yaml.SafeLoader)
        chrome_profile_path = CONFIG['chrome_profile_path']
        user_agent = CONFIG['user_agent']
        chrome_binary_location = CONFIG['chrome_binary_location']
        chrome_driver_path = CONFIG['chrome_driver_path']
        wait_timeout = CONFIG['wait_timeout']
        appearance_url = CONFIG['appearance_url']
        startup_url = CONFIG['startup_url']
        profile_pattern = CONFIG['profile_pattern']
        profile_ranges = CONFIG['profile_ranges']
        about_chrome_selector = CONFIG['about_chrome_selector']


        start_profile_number = profile_ranges[0]
        end_profile_number = profile_ranges[1]

    
    kill_chrome_processes()

    set_browser_preferences()

