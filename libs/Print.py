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
    #dlg.print_control_identifiers()

#Focus item trong order detail
@keyword("Focus Item")
def focusItem(focus_item):
    foit = dlg.child_window(title= ""+focus_item+"", control_type="Text")
    foit.click_input()

#Popup trọng lượng
@keyword("Enter weight")
def selectItemWeight(item_weight):
    #dlg.print_control_identifiers()
    dlg[""+item_weight+""].click()

#Popup số lượng
@keyword("Enter quanity")
def enterQuanity(quanity):
    #dlg.print_control_identifiers()
    dlg[""+quanity+""].click()

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

#Action Tăng (+)
@keyword("Click (+) button")
def clickIncreaseButton():
    dlg.Button10.click()

#Action Tăng (-)
@keyword("Click (-) button")
def clickDecreaseButton():
    dlg.Button9.click()

#Action Sửa item
@keyword("Click Edit button")
def clickEditButton():
    edit = dlg.child_window(title="Sửa", control_type="Text")
    edit.click_input()

#Action Xoá item
@keyword("Click Remove button")
def clickRemoveButton():
    rev = dlg.child_window(title="Xoá", control_type="Text")
    rev.click_input()

    
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
    sav = dlg.child_window(title="Đồng ý", control_type="Text")
    sav.click_input()

@keyword("Confirm not save with Exit button")
def confirmUnSaveCart():
    nosav = dlg.child_window(title="Huỷ", control_type="Text")
    nosav.click_input()
    
#Phím tắt ENTER
@keyword("Enter")
def enter():
    send_keys('{ENTER}')

# Cụm action button
@keyword("Click Provisional Button")
def clickProvisional():
    prov = dlg.child_window(title="Tạm tính", control_type="Text")
    prov.click_input()
    #dlg.print_control_identifiers()
@keyword("Click Payment Button")
def clickPayment():
    payment = dlg.child_window(title="Thanh toán", control_type="Text")
    payment.click_input()

@keyword("Click Exit Button")
def clickExit():
    out = dlg.child_window(title="Thoát", control_type="Text")
    out.click_input()

@keyword("Click Save Button")
def clickSave():
    save = dlg.child_window(title="Lưu đơn", control_type="Text")
    save.click_input()
