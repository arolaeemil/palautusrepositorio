*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  seppo  taalasmaa222
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  taalasmaa222
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  taalasmaa222
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  seppo  maa222
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kseppo  taalasmaakalle
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123
    Input New Command

