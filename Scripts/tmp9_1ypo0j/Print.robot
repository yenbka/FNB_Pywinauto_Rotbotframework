*** Settings ***
Library           ../libs/Print.py

*** Test Cases ***
Kitchen_Stamp_Create_Save
    Open Application    Button
    Click CreateNewCart Button
    Select Item    Trà sữa đường đen
    Select Genetal Section
    Select price    Nhập giá
    Enter price    Button45
    Enter price    Button48
    Enter
    Enter
