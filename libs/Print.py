from pywinauto import Application
from robot.api.deco import keyword
from pywinauto.keyboard import send_keys

app = Application(backend="uia").connect(path="C:\Program Files\SapoFnB\SapoFnB.exe")
dlg = app.MainWindow  
@keyword("Open Application")
def loginPin(button):
    #dlg.print_control_identifiers()
    dlg[""+button+""].click()
    dlg[""+button+""].click()
    dlg[""+button+""].click()
    dlg[""+button+""].click()
@keyword("Click CreateNewCart Button")
def createCart():
    create = dlg.child_window(title="Tạo đơn mới", control_type="Text")
    create.click_input()
    #dlg.print_control_identifiers()

@keyword("Select table")   
def selectTable(table_number):
    table = dlg.child_window(title="Chọn bàn", control_type="Text")
    table.click_input()
    #dlg.print_control_identifiers()
    dlg[""+table_number+""].click()
    #dlg.print_control_identifiers()

@keyword("Select Item")
def selectItem():
    item1 = dlg.child_window(title="Item 1", control_type="Text")
    item1.click_input()

# Action confirm khi tạo cart mới
@keyword("Confirm out to list cart")
def confirmOutListCart():
    yes = dlg.child_window(title="Có, ra danh sách đơn", control_type="Text")
    yes.click_input()
    #dlg.print_control_identifiers()
@keyword("Confirm stay on detail cart")
def confirmStayDetailCart():
    no = dlg.child_window(title="Không, ở lại đơn", control_type="Text")
    no.click_input()
    #dlg.print_control_identifiers()

@keyword("Confirm save with Exit button")
def confirmSaveCart():
    dlg.print_control_identifiers()

@keyword("Confirm not save with Exit button")
def confirmUnSaveCart():
    dlg.print_control_identifiers()


# Cụm action button
@keyword("Click Provisional Button")
def clickProvisional():
    send_keys('{VK_F2}')
    #dlg.print_control_identifiers()
@keyword("Click Payment Button")
def clickPayment():
    send_keys('{VK_F1}')

@keyword("Click Exit Button")
def clickExit():
    send_keys('{ESC}')

@keyword("Click Save Button")
def clickSave():
    send_keys('{VK_F3}')
