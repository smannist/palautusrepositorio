*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  puutarhatonttu  tonttu123123213
    Output Should Contain  New user registered

*** Test Cases ***
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  testisalasana1213
    Output Should Contain  User with username kalle already exists

*** Test Cases ***
Register With Too Short Username And Valid Password
    Input Credentials  hy  testisalasana123123
    Output Should Contain  Username must contain at least 3 letters

*** Test Cases ***
Register With Valid Username And Too Short Password
    Input Credentials  testuser  1a3
    Output Should Contain  Password must contain at least 8 characters

*** Test Cases ***
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  testuser  thisshouldnotwork
    Output Should Contain  Password should contain at least one letter and number

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123