import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoSqaLogin:
    # SELECTORS FOR LOGIN FORM
    firstName_ID = (By.ID, "firstName")
    lastName_ID = (By.ID, "lastName")
    email_ID = (By.ID, "userEmail")
    mobile_ID = (By.ID, "userNumber")
    dateofbirth_ID = (By.ID, "dateOfBirthInput")
    month_CSS = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    year_CSS = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    picture_upload_ID = (By.ID, "uploadPicture")
    state_XPATH = (By.XPATH, "//div[@id='state']//input")
    city_XPATH = (By.XPATH, "//div[@id='city']//input")
    submit_XPATH = (By.XPATH, "//button[@id='submit']")
    close_modal_CSS = (By.CSS_SELECTOR, "#closeLargeModal")

    # INITALIZING OF THE DRIVER
    def __init__(self, driver):
        self.driver = driver

    # POPULATE NAME
    def populate_name(self, firstname, lastname):
        self.driver.find_element(*DemoSqaLogin.firstName_ID).send_keys(firstname)
        self.driver.find_element(*DemoSqaLogin.lastName_ID).send_keys(lastname)

    # POPULATE EMAIL
    def populate_email(self, email):
        self.driver.find_element(*DemoSqaLogin.email_ID).send_keys(email)

    # SELECT GENDER
    def select_gender(self, gender):
        gender_XPATH = (By.XPATH, "//label[contains(text(),'{}')]".format(str(gender)))
        self.driver.find_element(*gender_XPATH).click()

    # POPULATE MOBILE NO.
    def mobile_number(self, number):
        self.driver.find_element(*DemoSqaLogin.mobile_ID).send_keys(number)

    # DATE OF BIRTH POPULATE
    def date_of_birth(self, date):
        day, month, year = date.split(" ")
        self.driver.find_element(*DemoSqaLogin.dateofbirth_ID).click()

        month_dropdown = Select(
            self.driver.find_element(*DemoSqaLogin.month_CSS)
        )
        year_dropdown = Select(
            self.driver.find_element(*DemoSqaLogin.year_CSS)
        )

        month_dropdown.select_by_visible_text(month)
        year_dropdown.select_by_value(year)

        date_picker = self.driver.find_element(
            By.XPATH,
            "//div[@class='react-datepicker__month']/div/div[not("
            "contains(@class,'react-datepicker__day--outside-month'))]["
            "text()='{}']".format(str(day)),
        )
        time.sleep(0.25)
        date_picker.click()

    # SELECT HOBBIES
    def select_hobbies(self, hobbies):
        list_hobbies = hobbies.split(",")
        for hobby in list_hobbies:
            selector_hobby = "//label[contains(text(),'{}')]".format(hobby)
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, selector_hobby))

    # UPLOAD PICTURE
    def picture_upload(self, path):
        self.driver.find_element(*DemoSqaLogin.picture_upload_ID).send_keys(path)

    # POPULATE STATE
    def populate_state(self, state):
        self.driver.find_element(*DemoSqaLogin.state_XPATH).send_keys(state)
        return self.driver.find_element(*DemoSqaLogin.state_XPATH)

    # POPULATE CITY
    def populate_city(self, city):
        self.driver.find_element(*DemoSqaLogin.city_XPATH).send_keys(city)
        return self.driver.find_element(*DemoSqaLogin.city_XPATH)

    # SUBMIT FORM
    def form_submit(self):
        self.driver.find_element(*DemoSqaLogin.submit_XPATH).click()

    # CLOSE MODAL
    def modal_close(self):
        # self.driver.find_element(*DemoSqaLogin.close_modal_CSS).click()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(*DemoSqaLogin.close_modal_CSS))
