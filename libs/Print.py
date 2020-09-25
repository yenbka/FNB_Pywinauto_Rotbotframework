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

# Chọn item trong thực đơn
@keyword("Select Item")
def selectItemOnePrice(item_one_price):
    item_one_price = dlg.child_window(title= ""+item_one_price+"", control_type="Text")
    item_one_price.click_input()

#Popup trọng lượng
@keyword("Enter weight")
def selectItemWeight(item_weight):
    #dlg.print_control_identifiers()
    dlg[""+item_weight+""].click()

#Select price
@keyword("Select price")
def selectPrice(s_price):
    price = dlg.child_window(title=""+s_price+"", control_type="Text")
    price.click_input()
    #dlg.print_control_identifiers()

#Select General Section
@keyword("Select Genetal Section")
def selectGene():
    gene = dlg.child_window(title="Phần chung", control_type="Text")
    gene.click_input()

#Select Mod-option
@keyword("Select Mod-Option")
def selectMod():
    mod = dlg.child_window(title="Lựa chọn thêm", control_type="Text")
    mod.click_input()

#Enter price
@keyword("Enter price")
def enterPrice(e_price):
    dlg[""+e_price+""].click()

#Select Mod-set
@keyword("Select Mod-set")
def selectModSet(s_mod):
    mod_set = dlg.child_window(title=""+s_mod+"", control_type="Text")
    mod_set.click_input()
    
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

#Phím tắt ENTER
@keyword("Enter")
def enter():
    send_keys('{ENTER}')

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
