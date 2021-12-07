import keyboard
import control 

def main():
    action1 = ','
    action2 = '.'
    keyboard.add_hotkey(action1, item_removal)
    keyboard.add_hotkey(action2, sys_exit)     

def item_removal():
    inv = control.Inv()
    inv.click_all()
    del inv

def item_organize():
    stash = control.Stash()
    item_list = stash.content()
    stash.organize(item_list)
    del stash

def sys_exit():
    exit()
  
if __name__== "__main__":
    main()




