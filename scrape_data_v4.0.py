import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the search query
search_query = "attività sport, san giuliano milanese"

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google Maps
driver.get("https://www.google.com/maps")

# Wait for the "Accept" button to appear
accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/div[1]/div[1]/form[2]/div/div/button')))

# Click the "Accept" button
accept_button.click()

# Wait for the search input to be visible and type the search query
search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
search_input.clear()
search_input.send_keys(search_query)

# Click the search button
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchbox-searchbutton')))
search_button.click()


# Wait for the search results to be visible and extract the data
search_results = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.DxyBCb:nth-child(1)')))
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
