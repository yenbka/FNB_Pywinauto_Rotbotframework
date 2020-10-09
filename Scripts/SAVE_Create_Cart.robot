*** Settings ***
Library           ../libs/Controller.py

*** Test Cases ***
SAVE_Create_Cart
    Open Application    Button
    Sleep    5s
    Select table external    Khu vực 2    6
    Select Item    Item 20k
    Click (+) button
    Click (+) button
    Select Item    Item 10k
    Click (+) button
    Select Menu    Thực đơn 2
    Select Item    Item trọng lượng 10k/gam
    Enter weight    5Button2
    Enter weight    .Button
    Enter weight    6Button2
    Enter
    Click Save Button
    Confirm stay on detail cart

SAVE_Update_Cart
    Focus Item    01.
    Click (-) button
    Focus Item    02.
    Click (+) button
    Select Item    item A
    Focus Item    03.
    Click Remove button
    Enter PIN    1Button2
    Enter Reason Cancel Item    Huỷ item    OK
    Click Save Button

TAMTINH_Create_Cart
    Open Application    Button
    Sleep    5s
    Select table external    Khu vực 2    7
    Select Item    Item 20k
    Click (+) button
    Click (+) button
    Select Item    Item 10k
    Click (+) button
    Select Menu    Thực đơn 2
    Select Item    Item trọng lượng 10k/gam
    Enter weight    5Button2
    Enter weight    .Button
    Enter weight    6Button2
    Enter
    Click Provisional Button
    Confirm stay on detail cart

TAMTINH_Update_Cart
    Focus Item    01.
    Click (-) button
    Focus Item    02.
    Click (+) button
    Select Item    item A
    Focus Item    03.
    Click Remove button
    Enter PIN    1Button2
    Enter Reason Cancel Item    Huỷ item    OK
    Click Provisional Button
