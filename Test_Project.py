import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from faker import Faker

class SalesforceSignupTest:

    def wait_for(self, n=1):
        time.sleep(n)

    def submit_form(self):

        # Initialize Faker
        fake = Faker()

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.salesforce.com/in/form/signup/sales-ee/?d=topnav2-btn-ft")

        # Generate fake data
        first_name = fake.first_name()
        last_name = fake.last_name()
        job_title = fake.job()
        company_name = fake.company()
        phone_number = fake.phone_number()
        email_id = fake.email()

        # Fill in the form
        firstName = driver.find_element(By.NAME, "UserFirstName")
        firstName.send_keys(first_name)
        self.wait_for()

        lastName = driver.find_element(By.NAME, "UserLastName")
        lastName.send_keys(last_name)
        self.wait_for()

        jobTitle = driver.find_element(By.NAME, "UserTitle")
        jobTitle.send_keys(job_title)
        self.wait_for()

        Next1 = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
        Next1.click()

        employees = driver.find_element(By.NAME, "CompanyEmployees")
        dd_employees = Select(employees)
        dd_employees.select_by_visible_text("1 - 20 employees")
        self.wait_for()

        company = driver.find_element(By.NAME, "CompanyName")
        company.click()
        company.send_keys(company_name)
        self.wait_for()

        country = driver.find_element(By.NAME, "CompanyCountry")
        dd_country = Select(country)
        dd_country.select_by_value("GB")
        self.wait_for()

        Next1 = driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
        Next1.click()

        phone = driver.find_element(By.NAME, "UserPhone")
        phone.send_keys(phone_number)
        self.wait_for()

        email = driver.find_element(By.NAME, "UserEmail")
        email.send_keys(email_id)
        self.wait_for()

        # Check the checkbox using XPath
        check_box = driver.find_element(By.XPATH, "(//div[@class='checkbox-ui'])[2]")
        check_box.click()
        self.wait_for()

        # Click Submit
        submit = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
        submit.click()
        self.wait_for(2)

        driver.quit()


# Run the Test
test = SalesforceSignupTest()
test.submit_form()
