Feature: Evaluate cost allocation


  @Priority-high
  Scenario: Test all budget is allocated
    Given a total budget of "500"
    And an hospital list
    When the cost allocation matrix is generated
    Then the output is equal to the total budget

  @Priority-medium
  Scenario Outline: Test minimum allocations
    Given a total budget of "<total_budget>"
    And an hospital list
    When the cost allocation matrix is generated
    Then all allocations must be superior to "<minimum_budget>"

    Examples:
      | total_budget | minimum_budget |
      | 100 | 30 |
      | 200 | 60 |

  @Priority-high
  Scenario Outline: Launch browser and search for people
    Given a launched browser on main ATIH page
    And a "<user_firstname>" and a "<user_lastname>"
    When the main page is visited and searched for user identity
    Then the searched text appears in results header

    Examples:
      | user_firstname | user_lastname |
      | Max | Bensadon |
      | Emmanuel | Thammavong |
