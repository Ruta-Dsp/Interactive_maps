import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set the location and search query
location = 'San Giuliano Milanese'
query = 'attività sportive'

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google Maps
driver.get("https://www.google.com/maps")

# Wait for the "Accept" button to appear and click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".widget-consent-button"))).click()

# Search for the location
search_box = driver.find_element_by_name("q")
search_box.send_keys(location)
search_box.send_keys(Keys.RETURN)

# Wait for the map to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pane")))

# Search for the query
search_box = driver.find_element_by_name("q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".section-result-content")))

# Extract the information for each result
results = driver.find_elements_by_css_selector(".section-result-content")

data = []
for result in results:
    name = result.find_element_by_css_selector(".section-result-title").text
    link = result.find_element_by_css_selector(".section-result-title > a").get_attribute("href")
    address = result.find_element_by_css_selector(".section-result-location").text
    lat = result.get_attribute("data-result-lat")
    lng = result.get_attribute("data-result-lng")

    # Append the information to the list
    data.append({
        "name": name,
        "latitude": lat,
        "longitude": lng,
        "link": link,
        "address": address
    })

# Write the data to a JSON file
with open("results.json", "w") as f:
    json.dump(data, f)

# Close the browser
driver.quit()
