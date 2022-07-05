Feature: exec-bash-skill-basics
  Scenario: safety default
    Given a 30 second timeout
      And an English speaking user
      When the user says "check safety"
      Then mycroft reply should contain "safety is on"

  Scenario: turn safety off
    Given a 30 second timeout
      And an English speaking user
      When the user says "hey, turn the safety off"
      Then mycroft reply should contain "ok, safety is off"


