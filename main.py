from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

username = 'forjaxcuatro@gmail.com'
password = '1000893751'
Chrome_driver_path = r"C:\Users\19549\Downloads\chrome-win64\chrome-win64"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3673972994&f_AL=true&keywords=entry%20level%20software%20engineer')
def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
def scroll_to_top():
    driver.execute_script("window.scrollTo(0, 0);")
    
sign_in = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
sign_in.click()
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)
sign_in = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
sign_in.click()
time.sleep(2)

scroll_down()
all_listings = driver.find_elements(By.CLASS_NAME, 'job-card-container--clickable')
scroll_to_top()
for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
        if apply_button.get_attribute('role') == 'link':
            continue
        apply_button.click()
        time.sleep(1)
        footer_button = driver.find_element(By.CSS_SELECTOR, 'footer button')
        footer_button.click()
        time.sleep(1)
        spans = driver.find_elements(By.TAG_NAME, 'span')
        span_exists = False
        for span in spans:
            if span.text == 'Next':
                span_exists = True
                break
        if span_exists == True:
            x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
            x_button.click()
            time.sleep(1)
            discard_button = driver.find_element(By.XPATH, "//button[span[text()='Discard']]")
            discard_button.click()
            time.sleep(1)
        footer_button = driver.find_element(By.XPATH, "//button[span[text()='Review']]")
        footer_button.click()
        time.sleep(1)
        submit_button = driver.find_element(By.XPATH, "//button[span[text()='Submit application']]")
        time.sleep(1)
        x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        x_button.click()
        time.sleep(1)
        continue
    except NoSuchElementException:
        continue
    
    
    
    
    
    
    
    
    
    
    
    
# driver.close()


# footer_button = driver.find_element(By.XPATH, "//button[span[text()='Next']]")














