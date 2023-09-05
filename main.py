from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

username = 'forjaxtres@gmail.com'
password = '1000893751'
Chrome_driver_path = r"C:\Users\19549\Downloads\chrome-win64\chrome-win64"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir="r"c:\Users\19549\AppData\Local\Google\Chrome\WebDriver")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)   

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3673972994&f_AL=true&keywords=entry%20level%20software%20engineer')
    
# sign_in = driver.find_element(By.CLASS_NAME, 'nav__button-secondary')
# sign_in.click()
# email_field = driver.find_element(By.ID, 'username')
# email_field.send_keys(username)
# password_field = driver.find_element(By.ID, 'password')
# password_field.send_keys(password)
# sign_in = driver.find_element(By.CLASS_NAME, 'btn__primary--large')
# sign_in.click()
time.sleep(3)


def scrolling():
    jobs_listing_body = driver.find_element(By.CSS_SELECTOR, 'div.jobs-search-results-list')
    scroll_down = "arguments[0].scrollTop += 1000;"
    scroll_up = "arguments[0].scrollTop -= 3000;"
    driver.execute_script(scroll_down, jobs_listing_body)
    time.sleep(1)
    driver.execute_script(scroll_down, jobs_listing_body)
    time.sleep(1)
    driver.execute_script(scroll_down, jobs_listing_body)

    time.sleep(1)
    driver.execute_script(scroll_up, jobs_listing_body)

# def pagination():
#     # find_pages = driver.find_element(By.CLASS_NAME, 'artdeco-pagination__pages')

#     # page_buttons = find_pages.find_element(By.TAG_NAME, 'button')
#     # print(len(page_buttons))
#     for i in range(1, 40):
#         scrolling()
#         next_button = driver.find_element(By.XPATH, "//button[span[text()='" + str(i + 1) + "']]")        
#         next_button.click()
#         time.sleep(1)

        
#         continue
        
        
def get_and_apply_to_listings():
        for i in range(1, 40):
            scrolling()
            all_listings = driver.find_elements(By.CLASS_NAME, 'job-card-container--clickable')
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
                    next_exists = False
                    post_apply_button_exists = False
                    for span in spans:
                        if span.text == 'Next':
                            next_exists = True
                            break
                        if span.text == 'Add Skill' or span.text == 'Get started' or span.text == 'Done' or span.text == 'Answer questions':
                            post_apply_button_exists = True
                            print('job applied successfully')
                            break
                    if post_apply_button_exists == True:
                        x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                        x_button.click()
                        time.sleep(1)
                        continue
                    if next_exists == True:
                        x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                        x_button.click()
                        time.sleep(1)
                        discard_button = driver.find_element(By.XPATH, "//button[span[text()='Discard']]")
                        discard_button.click()
                        time.sleep(1)
                    try_premium_button_to_check = driver.find_element(By.TAG_NAME, 'a').text
                    if try_premium_button_to_check == 'Try Premium for $0':
                        print('job applied successfully')
                        x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                        x_button.click()
                        time.sleep(1)
                        continue
                    footer_button = driver.find_element(By.XPATH, "//button[span[text()='Review']]")
                    footer_button.click()
                    time.sleep(1)
                    submit_button = driver.find_element(By.XPATH, "//button[span[text()='Submit application']]")
                    submit_button.click()
                    print('job applied successfully')

                    time.sleep(1)
                    x_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
                    x_button.click()
                    time.sleep(1)
                    continue
                except NoSuchElementException:
                    continue
            try:
                next_button = driver.find_element(By.XPATH, "//button[span[text()='" + str(i + 1) + "']]")        
                next_button.click()
                time.sleep(1)
                continue
            except NoSuchElementException:
                next_button = driver.find_element(By.XPATH, "//button[span[text()='…']]")
                next_button.click()
                time.sleep(1)
                continue         
get_and_apply_to_listings()    
    
    
    
    
    
    
    
    
# driver.close()


# footer_button = driver.find_element(By.XPATH, "//button[span[text()='Next']]")














