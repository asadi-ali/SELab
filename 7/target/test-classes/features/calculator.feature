@tag
Feature: Calculator
  Scenario: add two numbers
    Given Two input values, 1 and 2
    When I add the two values
    Then I expect the result 3

  Scenario Outline: add two numbers
    Given Two input values, <first> and <second>
    When I add the two values
    Then I expect the result <result>
    Examples:
      | first | second | result |
      | 1 | 12 | 13 |
      | -1 | 6 | 5 |
      | 2 | 2 | 4 |

    Scenario: div two numbers
      Given Two input values, 35 and 7
      When I / the two values
      Then I expect the result 5

    Scenario: pow two numbers
      Given Two input values, 3 and 4
      When I ^ the two values
      Then I expect the result 81

    Scenario Outline: opt two numbers
      Given Two input values, <first> and <second>
      When I <opt> the two values
      Then I expect the result <result>
      Examples:
        | first | second | opt | result |
        | 6 | 2 | / | 3 |
        | 6 | 2 | ^ | 36 |
        |-1 | 3 | ^ | -1 |
        |51 |17 | / | 3  |
