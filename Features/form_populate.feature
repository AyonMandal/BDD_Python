Feature: Automation of the login form using BDD
  Scenario Outline: Populate a form and submit
    Given The form is ready to be populated

    Then Populate name first : <firstname> <lastname>

    Then Populate the email id : <email>

    Then The gender is selected : <sex>

    Then User populates mobile no : <mobile_no>

    Then DOB is populated : <dateofbirth>

    Then Hobby is selected : <hobbies>

    Then A picture is uploaded : <file>

    Then State is populated : <state>

    Then City is populated : <city>

    Then The form is submitted

    Then Modal is displayed and closed

    Examples:
    | firstname | lastname|email              |sex |mobile_no |dateofbirth     |hobbies             |file                                            |state  |city   |
    | Ayon      | Mandal  |testmail1@gmail.com|Male|7003432515|20 December 1997|Reading,Sports,Music|F:\app\pythonProject\Python_Behave\banner-01.jpg|Haryana|Panipat|
