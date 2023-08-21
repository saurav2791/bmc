import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import pandas as pd

# Load input data from a JSON file
with open('test_input.json') as json_file:
    test_input = json.load(json_file)

# Launch the browser
driver = webdriver.Chrome()

try:
    # Open URL - http://www.google.com
    driver.get("http://www.google.com")
    
    # Enter the keyword "amazon" in the search bar
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("amazon")
    search_bar.send_keys(Keys.RETURN)
    
    # Print all the search results
    search_results = driver.find_elements(By.TAG_NAME, "h3")
    for result in search_results:
        print(result.text)
    
    # Click on the link which takes you to the amazon login page.
    amazon_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon")
    amazon_link.click()

    # Log in to https://www.amazon.in/
    def login_to_amazon(username, password):
        driver.get("https://www.amazon.in/")
        login_link = driver.find_element(By.ID, "nav-link-accountList")
        login_link.click()

        email_field = driver.find_element(By.ID, "ap_email")
        email_field.send_keys(username)
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()

        password_field = driver.find_element(By.ID, "ap_password")
        password_field.send_keys(password)
        sign_in_button = driver.find_element(By.ID, "signInSubmit")
        sign_in_button.click()

    # Click on all buttons on search & select Electronics.
    def click_all_buttons_and_select_electronics():
        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in all_buttons:
            button.click()
        electronics_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Electronics")
        electronics_link.click()

    # Search for dell computers and apply the filter of range Rs 30000 to 50000
    def search_and_apply_filter(min_price, max_price):
        search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.send_keys("dell computers")
        search_bar.send_keys(Keys.RETURN)

        filter_min_price = driver.find_element(By.ID, "low-price")
        filter_max_price = driver.find_element(By.ID, "high-price")
        filter_min_price.clear()
        filter_min_price.send_keys(min_price)
        filter_max_price.clear()
        filter_max_price.send_keys(max_price)
        go_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][aria-labelledby='a-autoid-1-announce']")
        go_button.click()

    # Validate products within the price range
    def validate_price_range(min_price, max_price):
        product_prices = driver.find_elements(By.CSS_SELECTOR, ".a-price-whole")
        for price_element in product_prices:
            price = int(price_element.text.replace(',', ''))
            assert min_price <= price <= max_price, f"Price {price} is not within the range {min_price}-{max_price}"

    # Print all the products on the first 2 pages whose rating is 5 out of 5
    def print_highly_rated_products():
        product_ratings = driver.find_elements(By.CSS_SELECTOR, ".a-icon-alt")
        product_titles = driver.find_elements(By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")
        for rating, title in zip(product_ratings, product_titles):
            if rating.text == "5.0 out of 5 stars":
                print(f"Highly Rated: {title.text}")

    # Add the first product whose rating is 5 out of 5 to the wish list. (Create a new wish list)
    def add_product_to_wishlist():
        first_highly_rated_product = driver.find_element(By.CSS_SELECTOR, ".a-icon-alt[alt='5.0 out of 5 stars']")
        product = first_highly_rated_product.find_element(By.XPATH, "../..")
        product.click()

        add_to_wishlist_button = driver.find_element(By.ID, "add-to-wishlist-button-submit")
        add_to_wishlist_button.click()

    # Validate the product is added to the wish list
    def validate_product_added_to_wishlist():
        success_message = driver.find_element(By.ID, "WLHUC_result").text
        assert "added to your" in success_message, "Product was not added to wishlist"
        
    # Verify the product in the wishlist
    def verify_product_in_wishlist():
        wishlist_link = driver.find_element(By.ID, "nav-link-wishlist")
        wishlist_link.click()
        

    # Load input data from the JSON file
    username = test_input["amazon_username"]
    password = test_input["amazon_password"]
    min_price = test_input["min_price"]
    max_price = test_input["max_price"]

    # Execute the test steps
    login_to_amazon(username, password)
    click_all_buttons_and_select_electronics()
    search_and_apply_filter(min_price, max_price)
    validate_price_range(min_price, max_price)
    print_highly_rated_products()
    add_product_to_wishlist()
    validate_product_added_to_wishlist()


finally:
    driver.quit()
