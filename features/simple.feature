Feature: find who is "d9ncih"
  As a regular internet user
  In order to know who is "d9nich"
  I want to easily find his github page

  Scenario Outline: find <nickname> github page
    Given I have access to the internet
    And I have entered <nickname> in google search
    And page contains <realName>
    When I click on first github link
    Then it would contain <learningSkills>

    Examples: names
      | nickname      | realName       | learningSkills                                                         |
      | d9nich        | Danylo Halaiko | Ask me about Java, Python, Golang, JavaScript, Kotlin, TypeScript, C++ |
      | byteofmydream | Ivan Mikula    | rozetkaTest                                                            |