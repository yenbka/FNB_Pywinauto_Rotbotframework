*** Settings ***
Library           ../libs/Print.py

*** Test Cases ***
Kitchen_Stamp_Create_Save
    Open Application    Button
    Click CreateNewCart Button
    Select Item    Item 1
    Sleep    2s
    Select table    7Button
    Click Save Button
    Confirm out to list cart
