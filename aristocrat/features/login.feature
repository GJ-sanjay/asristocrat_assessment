Feature: Launch the Saucedemo website and validate the login and product features

@TC001
Scenario: Valid login Credentials
  Given The user navigates to the website
  When user Enters username and password
  And user click on log in button
  Then User will be logged in

@TC002
Scenario: Invalid login Credentials
  Given The user navigates to the website from the URL
  When user Enters locked out username and password 
  And user click on the log in button
  Then User will be prompted with error

@TC003
 Scenario: Order a product
    Given I am on the inventory page
    When user sorts products from low price to high price
    And user adds lowest priced product
    And user clicks on cart
    And user clicks on checkout
    And user enters first name John
    And user enters last name Doe
    And user enters zip code 123
    And user clicks Continue button
    Then I verify in Checkout overview page if the total amount for the added item is $8.63
    When user clicks Finish button
    Then Thank You header is shown in Checkout Complete page
