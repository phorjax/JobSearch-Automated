from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = 'forjaxtres@gmail.com'
password = '1000893751'
Chrome_driver_path = r"C:\Users\19549\Downloads\chrome-win64\chrome-win64"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/jobs/search/?keywords=entry%20level%20software%20engineer')
sign_in = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
sign_in.click()
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(username)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)
sign_in = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
sign_in.click()
time.sleep(2)

all_listings = driver.find_elements(By.CLASS_NAME, 'job-card-container--clickable')
for listing in all_listings:
    listing.click()
    time.sleep(2)
    apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
    if apply_button.get_attribute('role') == 'link':
        continue
    apply_button.click()
    time.sleep(1)
    footer_button = driver.find_element(By.CSS_SELECTOR, 'footer button')
    footer_button.click()
    if len(driver.find_elements(By.CLASS_NAME, 'artdeco-modal__dismiss'))> 0:
        close_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
        close_button.click()
        continue
    footer_button = driver.find_element(By.CLASS_NAME, 'artdeco-button-primary')
    if footer_button.get_attribute('aria-label') == 'Continue your application':
        close_button = driver.find_element(By.CLASS_NAME, 'artdeco-button__icon')
        close_button.click()
        time.sleep(1)
        discard_button = driver.find_element(By.XPATH, "//button[contains(@class, 'artdeco-button')]//*[contains(.,'discard')]/..")
        discard_button.click()
        continue
    else:
        footer_button.click()
# driver.close()
















