from pywinauto import Application
from robot.api.deco import keyword
from pywinauto.keyboard import send_keys

app = Application(backend="uia").connect(path="C:\Program Files\SapoFnB\SapoFnB.exe")
dlg = app.MainWindow

@keyword("Open Application")
def loginPin(button):
    dlg[""+button+""].click()
    dlg[""+button+""].click()
    dlg[""+button+""].click()
    dlg[""+button+""].click()

@keyword("Click CreateNewCart Button")
def createCart():
    create = dlg.child_window(title="Tạo đơn mới", control_type="Text")
    create.click_input()

@keyword("Open cart")
def openCart(area, table):
    open_cart = dlg.child_window(title= ""+area+"", control_type="Text")
    open_cart = dlg.child_window(title= ""+table+"", control_type="Text")
    open_cart.click_input()

@keyword("Select table internal")   
def selectTableInternal(area2, table2):
    table = dlg.child_window(title="Chọn bàn", control_type="Text")
    table.click_input()
    area3 = dlg.child_window(title= ""+area2+"", control_type="Text")
    area4 = dlg.child_window(title= ""+table2+"", control_type="Text")
    area3.click_input()
    area4.click_input()

@keyword("Select table external")   
def selectTableExternal(area1, table1):
    maps = dlg.child_window(title="Sơ đồ bàn", control_type="Text")
    maps.click_input()
    area1 = dlg.child_window(title= ""+area1+"", control_type="Text")
    area2 = dlg.child_window(title= ""+table1+"", control_type="Text")
    area1.click_input()
    area2.click_input()


@keyword("Select Services")
def selectService(services):
    services = dlg.child_window(title= ""+services+"", control_type="Text")
    services.click_input()

@keyword("Click More Action")
def clickMoreAction(more_action, action):
    dlg[""+more_action+""].click_input()

# Chọn item trong thực đơn
@keyword("Select Item")
def selectItemOnePrice(item_one_price):
    item_one_price = dlg.child_window(title= ""+item_one_price+"", control_type="Text")
    item_one_price.click_input()

#Chọn thực đơn
@keyword("Select Menu")
def selectCa(menu):
    menu = dlg.child_window(title= ""+menu+"", control_type="Text")
    menu.click_input()

#Focus item trong order detail
@keyword("Focus Item")
def focusItem(focus_item):
    foit = dlg.child_window(title= ""+focus_item+"", control_type="Text")
    foit.click_input()

#Popup trọng lượng
@keyword("Enter weight")
def selectItemWeight(item_weight):
    dlg[""+item_weight+""].click()

#Popup số lượng
@keyword("Enter quanity")
def enterQuanity(quanity):
    dlg[""+quanity+""].click()

#Select price
@keyword("Select price")
def selectPrice(s_price):
    price = dlg.child_window(title=""+s_price+"", control_type="Text")
    price.click_input()

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

@keyword("Enter PIN")
def enterPIN(pin):
    dlg[""+pin+""].click()
    dlg[""+pin+""].click()
    dlg[""+pin+""].click()
    dlg[""+pin+""].click()
    
@keyword("Enter Reason Cancel Item")
def enterReason(reason, ac):
    dlg.Edit2.type_keys(""+reason+"", with_spaces=True)
    action = dlg.child_window(title=""+ac+"", control_type="Text")
    action.click_input()

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
    rev = dlg.child_window(title="Xóa", control_type="Text")
    rev.click_input()

    
# Action confirm khi tạo cart mới
@keyword("Confirm out to list cart")
def confirmOutListCart():
    yes = dlg.child_window(title="Có, ra danh sách đơn", control_type="Text")
    yes.click_input()

@keyword("Confirm stay on detail cart")
def confirmStayDetailCart():
    no = dlg.child_window(title="Không, ở lại đơn", control_type="Text")
    no.click_input()
    

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

#Investigate properity
@keyword("Investigate Properity")
def investigate():
    dlg.print_control_identifiers()