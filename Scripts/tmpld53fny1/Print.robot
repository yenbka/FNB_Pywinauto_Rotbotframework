*** Settings ***
Library           ../libs/Print.py

*** Test Cases ***
Kitchen_Stamp_Create_Save
    Open Application    Button
    Click CreateNewCart Button
    Select Item    Trà sữa đường đen
    Select Genetal Section
    Select price    Nhập giá
    Enter price    2Button2
    Enter price    000Button
    Enter
    Enter
