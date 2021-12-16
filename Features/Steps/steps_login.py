import pdb
import sys
import time

from behave import *
# from parse import parse

from Helpers.Browser_general import BrowserGeneral
from POM.Demosqa_login import DemoSqaLogin


@given('The form is ready to be populated')
def form_is_displayed(context):
    try:
        BrowserGeneral.open_page(context.driver, "https://demoqa.com/automation-practice-form")
        BrowserGeneral.maximize_window(context.driver)
        context.start_logger.info("Form is ready to be populated")
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('Populate name first : {firstname} {lastname}')
def name_is_populated(context, firstname, lastname):
    try:
        DemoSqaLogin(context.driver).populate_name(firstname, lastname)
        context.start_logger.info("Name attribute successfully populated: {} {}".format(firstname, lastname))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('Populate the email id : {email}')
def email_is_populated(context, email):
    try:
        DemoSqaLogin(context.driver).populate_email(email)
        context.start_logger.info("Email was successfully populated : {}".format(email))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('The gender is selected : {sex}')
def gender_is_selected(context, sex):
    try:
        DemoSqaLogin(context.driver).select_gender(sex)
        context.start_logger.info("Sex is selected : {}".format(sex))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('User populates mobile no : {mobile_no}')
def mobile_no_populated(context, mobile_no):
    try:
        DemoSqaLogin(context.driver).mobile_number(mobile_no)
        context.start_logger.info("Mobile no successfully populated : {}".format(mobile_no))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('DOB is populated : {dateofbirth}')
def dob_populated(context, dateofbirth):
    try:
        DemoSqaLogin(context.driver).date_of_birth(dateofbirth)
        context.start_logger.info("Date of Birth successfully populated : {}".format(dateofbirth))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('Hobby is selected : {hobbies}')
def hobbies_selected(context, hobbies):
    try:
        DemoSqaLogin(context.driver).select_hobbies(hobbies)
        context.start_logger.info("Hobbies were selected : {}".format(hobbies))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('A picture is uploaded : {file}')
def picture_is_uploaded(context, file):
    try:
        BrowserGeneral.vertical_scroll(context.driver, 200)
        DemoSqaLogin(context.driver).picture_upload(file)
        context.start_logger.info("File was successfully uploaded : {}".format(file))
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('State is populated : {state}')
def state_is_selected(context, state):
    try:
        ele = DemoSqaLogin(context.driver).populate_state(state)
        BrowserGeneral.press_enter(ele)
        context.start_logger.info("State is selected : {}".format(state))
    # pdb.set_trace()
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('City is populated : {city}')
def city_is_selected(context, city):
    try:
        ele = DemoSqaLogin(context.driver).populate_city(city)
        BrowserGeneral.press_enter(ele)
        context.start_logger.info("City is selected : {}".format(city))
    except Exception as e:
        context.start_logger.info(e)
        raise


@then('The form is submitted')
def form_is_submitted(context):
    try:
        BrowserGeneral.vertical_scroll(context.driver, 1000)
        DemoSqaLogin(context.driver).form_submit()
        context.start_logger.info("Form was successfully submitted")
    except Exception as e:
        context.start_logger.error(e)
        raise


@then('Modal is displayed and closed')
def modal_displayed_closed(context):
    try:
        BrowserGeneral.vertical_scroll(context.driver, 1000)
        DemoSqaLogin(context.driver).modal_close()
        time.sleep(2)
        context.start_logger.info("Modal was closed")
    except Exception as e:
        context.start_logger.error(e)
        raise
