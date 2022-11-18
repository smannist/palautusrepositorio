*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Valid Password
    Set Username  testuser
    Set Password  testuser123123
    Set Confirmation Password  testuser123123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  hy
    Set Password  testpassword123123
    Set Confirmation Password  testpassword123123
    Submit Credentials
    Register Should Fail With Message  Username must contain at least 3 letters

Register With Valid Username And Too Short Password
    Set Username  testuser
    Set Password  short12
    Set Confirmation Password  short12
    Submit Credentials
    Register Should Fail With Message  Password must contain at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  testuser
    Set Password  testuser123123
    Set Confirmation Password  testuser923824
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}