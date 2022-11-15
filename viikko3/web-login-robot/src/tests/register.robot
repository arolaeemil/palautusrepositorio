*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  seppo
    Set Password  seppotaalas123
    Set Password Confirmation  seppotaalas123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  se
    Set Password  seppotaalas123
    Set Password Confirmation  seppotaalas123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  seppo
    Set Password  sepp0
    Set Password Confirmation  sepp0
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  seppo
    Set Password  seppotaalas123
    Set Password Confirmation  taalasseppo123
    Submit Credentials
    Register Should Fail With Message  Password doesn't match

Login After Successful Registration
    Register Correctly
    Go To Login Page
    Set username  seppo
    Set password  seppotaalas123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Register Incorrectly
    Go To Login Page
    Set username  seppo6
    Set password  seppotaalas123
    Submit Credentials Login
    Login Should Not Succeed
    
*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Not Succeed
    Login Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Correctly
    Go To Register Page
    Set Username  seppo
    Set Password  seppotaalas123
    Set Password Confirmation  seppotaalas123
    Submit Credentials

Register Incorrectly
    Go To Register Page
    Set Username  seppo6
    Set Password  seppotaalas123
    Set Password Confirmation  seppotaalas123
    Submit Credentials