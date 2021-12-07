import pickle
import pyautogui
import json
import pyperclip

class db():
    def __init__(self): #loads the database of itens
        data = open(r'C:\Users\sonvi\Desktop\teste.txt')
        self.db = json.load(data) #db of itens
        data.close()
        position = [3,5] #test remove after
        with open('position','wb') as fp: #position inventory manager
            pickle.dump(position,fp)
        
    def read_item(self): #read item
        item = pyperclip.paste()
        line = item.splitlines()
        if( '-' in line[2]):
            k = 1
        else:
            k = 2
        return line[k]

    def search_item(self): #search items in json
        found_item = []
        for one_item in self.db:
                if self.db[one_item].get('name') == db.read_item(self):
                    found_item = one_item
                    break
        return self.db[found_item]

    def write_item(self): #break and write
        item = db.search_item(self)
        new_item = {'item_class' : item.get('item_class'),
                    'inventory_height' : item.get('inventory_height'),
                    'inventory_width' : item.get('inventory_width'),
                    'inventory_position' : db.get_position(self)
                    }
        with open(r'C:\Users\sonvi\Desktop\inventory.txt','a') as f:
            f.write(json.dumps(new_item))
            print(new_item)
              #def readItem(self):    
    def get_position(self):
        with open('position','rb') as fp:
            return pickle.load(fp)

    def set_position(self, item, position):
        if item.get('inventory_height') + position[0] < 12:
            if item.get('inventory_width') + position[1] < 12:
                position
            
        
        
