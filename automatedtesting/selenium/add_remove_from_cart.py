# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

# --uncomment when running in Azure DevOps.
options = ChromeOptions()    
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(options=options)
totalItems = 6

# Start the browser and login with standard_user
def login (user, password):
    print (log_timestamp() + 'Starting the browser...')
    print (log_timestamp() + 'Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.CSS_SELECTOR, "input[id='user-name']").send_keys(user)
    driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    el_products_label = driver.find_element(By.CSS_SELECTOR, "span.title").text
    assert 'Products' in el_products_label

    print (log_timestamp() + 'User is login successfully: username {:s}, password {:s}.'.format(user, password))

def add_cart():
    for i in range(totalItems):
        el_item_link = "a[id='item_" + str(i) + "_img_link']"
        driver.find_element(By.CSS_SELECTOR, el_item_link).click()

        el_add_to_cart = "button[id='add-to-cart']"
        driver.find_element(By.CSS_SELECTOR, el_add_to_cart).click()

        el_item_name = "div.inventory_details_name"
        item_name = driver.find_element(By.CSS_SELECTOR, el_item_name).text

        print(log_timestamp() + '{:s} item was added to shopping cart.'.format(item_name))

        el_back_to_products = "button[id='back-to-products']"
        driver.find_element(By.CSS_SELECTOR, el_back_to_products).click()
    
    el_shopping_cart_container = "div[id='shopping_cart_container'] > a > span"
    total_items = driver.find_element(By.CSS_SELECTOR, el_shopping_cart_container).text
    assert totalItems == int(total_items)
    print (log_timestamp() + 'Total item added to shopping cart is: {:s}.'.format(total_items))

def remove_cart():
    for i in range(totalItems):
        el_item_link = "a[id='item_" + str(i) + "_img_link']"
        driver.find_element(By.CSS_SELECTOR, el_item_link).click()

        el_item_name = "div.inventory_details_name"
        item_name = driver.find_element(By.CSS_SELECTOR, el_item_name).text

        el_remove = "button[id='remove']"
        driver.find_element(By.CSS_SELECTOR, el_remove).click()

        print(log_timestamp() + '{:s} item was removed from shopping cart.'.format(item_name))

        el_back_to_products = "button[id='back-to-products']"
        driver.find_element(By.CSS_SELECTOR, el_back_to_products).click()
    
    el_shopping_cart_container = "div[id='shopping_cart_container'] > a"
    total_items = driver.find_element(By.CSS_SELECTOR, el_shopping_cart_container).text
    assert '' == total_items
    print (log_timestamp() + 'All items were removed from shopping cart.')

def log_timestamp():
    ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    return (ts + ' ')

print (log_timestamp() + 'Start Selenium Tests...')
login('standard_user', 'secret_sauce')
add_cart()
remove_cart()
print (log_timestamp() + 'Completed Selenium Tests.')