import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


class FlightBookingAutomation:
    def select_cities_and_departure_date(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.goibibo.com/")

        wait = WebDriverWait(driver, 10)

        # Close login popup
        login_popup_close = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@role='presentation']")))
        login_popup_close.click()

        # Click on "From" input box
        from_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Enter city or airport']")))
        from_box.click()

        # Type "Hydera" in the input field
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        input_box.send_keys("Hydera")
        time.sleep(1)

        # Press Enter to select the first suggestion
        input_box.send_keys(Keys.ENTER)

        # Filling the "To" field
        to_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))
        to_box.send_keys("New")

        # List of autosuggestion elements
        autosuggest_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@id='autoSuggest-list']/li")))
        print(f"Number of autosuggestions found: {len(autosuggest_list)}")
        for element in autosuggest_list:
            if "New York, United States" in element.text:
                print(f"Found my search result: {element.text}")
                element.click()
                time.sleep(2)
                break

        # Get today's date
        today = datetime.now()

        # Format the date into string format "dd Mmm'yy"
        formatted_date = f"{today.day} {today.strftime('%b')}'{today.strftime('%y')}"

        # Click on date field
        date_field = wait.until(EC.element_to_be_clickable((By.XPATH, f'//p[text() = "{formatted_date}"]')))
        date_field.click()
        time.sleep(2)

        # Select a date you wanted to book
        departure_date = driver.find_element(By.XPATH, "//div[@aria-label='Fri May 09 2025']")
        departure_date.click()
        time.sleep(1)

        # Clicking on checkbox
        checkbox = driver.find_element(By.XPATH, "//div[contains(@class,'biWUTl')]")
        checkbox.click()
        time.sleep(2)

        # Clicking on Search Flights button
        search_flights = driver.find_element(By.XPATH, "//span[text()='SEARCH FLIGHTS']")
        search_flights.click()
        time.sleep(7)

        driver.quit()


flight_booking = FlightBookingAutomation()
flight_booking.select_cities_and_departure_date()
