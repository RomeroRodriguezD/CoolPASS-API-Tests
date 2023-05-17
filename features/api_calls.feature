Feature: TestAPIoptions

  Scenario Outline: APISingleOptions
     Given we are in the landing page
      When we create password with "<number_chars>" and "<option>"
      Then we should get a custom password

    Examples:
        | number_chars | option |
        |       8      | animals|
        |       12     | colors |
        |       20     | cities |
        |       16     | famous |
