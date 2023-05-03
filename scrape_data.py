from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set the location and search query
location = 'San Giuliano Milanese'
query = 'attività sportive'

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google Maps
driver.get("https://www.google.com/maps")

# Search for the location
search_box = driver.find_element_by_name("q")
search_box.send_keys(location)
search_box.send_keys(Keys.RETURN)

# Wait for the map to load
sleep(5)

# Search for the query
search_box = driver.find_element_by_name("q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
sleep(5)

# Extract the information for each result
results = driver.find_elements_by_css_selector(".section-result-content")
for result in results:
    name = result.find_element_by_css_selector(".section-result-title").text
    link = result.find_element_by_css_selector(".section-result-title > a").get_attribute("href")
    address = result.find_element_by_css_selector(".section-result-location").text
    lat = result.get_attribute("data-result-lat")
    lng = result.get_attribute("data-result-lng")

    # Print the information for each result
    print(f"Name: {name}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lng}")
    print(f"Link: {link}")
    print(f"Address: {address}")

# Close the browser
driver.quit()
