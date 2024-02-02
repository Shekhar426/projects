from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

chrome_options =   ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.flightradar24.com/data/airports/pnq")

Required_city = ["Bangalore", "Delhi", "Goa", "Chandigarh", "Hyderabad", "Nagur", "Dubai"]
Matched_City = []
city_name = driver.find_elements(By.XPATH, "//span[@class='hide-mobile-only ng-binding']")

for i in range(len(city_name)):
    if city_name[i].text in Required_city:
        status = driver.find_element(By.XPATH, f"(//span[@class='hide-mobile-only ng-binding'])[{i+1}]/../../following-sibling::td[4]")
        print(f"{city_name[i].text}: {status.text}")
        Matched_City.append(city_name[i].text)
for j in Required_city:
    if j not in Matched_City:
        print(f"{j}: Data not Available")

