import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the search query
search_query = "Nome della città"

# Configure the Chrome driver and open Google Maps
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/maps/")

# Wait for the "Accept" button to be visible and click it
accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="introAgreeButton"]/span/span')))
accept_button.click()

# Wait for the search input to be visible and type the search query
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
search_input.clear()
search_input.send_keys(search_query)
search_input.submit()

# Wait for the search results to be visible and extract the data
search_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="section-result"]')))
results = []
for result in search_results:
    name = result.find_element_by_xpath('.//*[@class="section-result-title"]/span[1]').text
    address = result.find_element_by_xpath('.//*[@class="section-result-location"]/span[1]').text
    lat, lng = result.get_attribute('data-result-position').split(',')
    link = result.find_element_by_css_selector('a').get_attribute('href')
    results.append({
        "name": name,
        "address": address,
        "lat": float(lat),
        "lng": float(lng),
        "link": link
    })

# Save the results to a JSON file
with open("search_results.json", "w") as outfile:
    json.dump(results, outfile)

# Quit the driver
driver.quit()
