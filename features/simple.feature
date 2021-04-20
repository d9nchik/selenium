Feature: find who is d9ncih
  As a regular internet user
  In order to know who is d9nich
  I want to easily find his github page

  Scenario: find d9nich github page
    Given I have access to the internet
    And I have entered d9nich in google search
    And page contains "Danylo Halaiko"
    When I click on first github link
    Then it would be d9nich github main page
