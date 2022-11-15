*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Click Login Link
    Click Link  link:Login
    Login Page Should Be Open

Click Register Link
    Click Link  link:Register new user
    Register Page Should Be Open

*** Keywords ***
    