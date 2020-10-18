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

check property
    Open Application    Button
    Sleep    5s
    Click More Action    Khu vực 1    12
    Investigate Properity

THANHTOANLUON_Create
    Open Application    Button
    Sleep    4s
    Click CreateNewCart Button
    Select Item    Item 10k
    Select Item    Item 20k
    Select Menu    Thực đơn 2
    Select Item    Item trọng lượng 10k/gam
    Enter weight    5Button2
    Enter weight    .Button
    Enter weight    6Button2
    Enter
    Click Payment Button
    Click Confirm Payment button
    Click Print and Finish button

THANHTOANLUON_Update_Cart
    Sleep    4s
    Click Exit Button
    Open cart    Khu vực 1    17
    Focus Item    01.
    Click (+) button
    Focus Item    02.
    Click (-) button
    Focus Item    03.
    Click Remove button
    Enter PIN    1Button2
    Enter Reason Cancel Item    Huỷ item    OK
    Select Item    item A
    Click Payment Button
    Click Confirm Payment button
    Click Print and Finish button

THOAT_SAVE_Create_Cart
    Open Application    Button
    Sleep    4s
    Select table external    Khu vực 2    3
    Select Item    Item 10k
    Select Item    Item 20k
    Click Exit Button
    Confirm save with Exit button
    Confirm out to list cart

THOAT_UNSAVE_Upate_Cart
    Open cart    Khu vực 1    12
    Focus Item    01.
    Click (+) button
    Focus Item    02.
    Click (-) button
    Focus Item    03.
    Click Remove button
    Enter PIN    1Button2
    Enter Reason Cancel Item    Huỷ item    OK
    Focus Item    item A
    Click Exit Button
    Confirm not save with Exit button
