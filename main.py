from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

chrome_driver_path = "/Users/david.cordero/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(3)


driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=90000084&keywords=python%20developer&location=San%20Francisco%20Bay%20Area")
time.sleep(3)

# search_pane = driver.find_element_by_class_name("jobs-search-two-pane__results")
# job_cards = search_pane.find_elements_by_tag_name("ul li div")
# job_cards = driver.find_elements_by_class_name("job-card-container__link")
resume = "/Users/david.cordero/Desktop/"
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        listing.click()
        apply_now = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_now.click()
        time.sleep(2)
        ##add phone number
        phone_field = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone_field == "":
            phone_field.send_keys("+14158675309")
        else:
            next_button = driver.find_element_by_class_name("artdeco-button--primary")
            next_button.click()
        ##upload file
        upload = driver.find_element_by_name("file")
        time.sleep(2)
        upload.send_keys("/Users/david.cordero/Desktop/Untitled.pdf")
        time.sleep(2)

        submit_button = driver.find_element_by_class_name("artdeco-button--primary")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
    except:
        print("No application button, skipped.")
        continue
driver.quit()



