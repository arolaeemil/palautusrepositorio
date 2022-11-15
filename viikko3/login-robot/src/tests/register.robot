*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  seppo  taalasmaa
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  taalasmaa
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
# ...

Register With Valid Username And Too Short Password
# ...

Register With Valid Username And Long Enough Password Containing Only Letters
# ...

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command

