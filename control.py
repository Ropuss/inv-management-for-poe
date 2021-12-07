import pyautogui
import time
import pyperclip
class Position(): 
    def __init__(self, xk, yk, nx, ny, kx, ky): #(initial position, number of positions and constant to move)
        screen = pyautogui.size()
        self.x = round(screen.width * xk)
        self.y = round(screen.height * yk)
        self.nx = nx
        self.ny = ny
        self.kx = kx
        self.ky = ky
        pyautogui.PAUSE = 0.05

    def move(self, i, j): #INTERNAL
        pyautogui.moveTo(round(self.x + self.kx * i), round(self.y + self.ky * j))

    def click_all(self): #MAIN  #if self.nx * self.ny != 60:#   raise Exception('only inventory for now') #not happy
        pyautogui.keyDown('ctrl')
        for i in range(0, self.nx):
            for j in range(0, self.ny):
                self.move(i, j)
                pyautogui.click()
        pyautogui.keyUp('ctrl')#self.click(i, j)
        
    def organize(self,matrix_tab):
        pyautogui.keyDown('ctrl')
        for i in range(0, self.nx):
            for j in range(0, self.ny):
                if matrix_tab[i][j] == 'Currency_Tab':
                    self.move(i, j)
                    pyautogui.click()
        for i in range(0, self.nx):
            for j in range(0, self.ny):
                if matrix_tab[i][j] == 'Map_Tab':
                    self.move(i, j)
                    pyautogui.click()
        pyautogui.keyUp('ctrl')#self.click(i, j)

    def click_all_id(self): #identify all itens MAIN #if self.nx * self.ny != 60:#   raise Exception('only inventory for now') #not happy
        pyautogui.keyDown('shift')
        for i in range(0, self.nx):
            for j in range(0, self.ny):
                self.move(i, j)
                pyautogui.click()
        pyautogui.keyUp('shift')#self.click(i, j)
        


    def click(self, i, j): #INTERNAL BRICKED NOT USED
        self.move(i, j)
        pyautogui.keyDown('ctrl')
        pyautogui.click()
        pyautogui.keyUp('ctrl')


    def click_id(self, i, j): #INTERNAL BRICKED NOT USED
        self.move(i, j)
        self.reg()
        pyautogui.click()
            
    def content(self): #EXTERNAL identify all itens in stash terms
        matrix_tab = []
        for i in range(0, self.nx):
            matrix_tab.append([])
            for j in range(0, self.ny):
                self.move(i, j)
                pyautogui.hotkey('ctrl', 'c')
                matrix_tab[i].append(self.identify_type(pyperclip.paste()))
        return matrix_tab

    def identify_type(self, item):
        items = item.splitlines()
        for key, value in self.stash_dict.items():
            aux = ''
            aux = aux.join(self.stash_dict[key])
            if items[1] in aux:
                return key
        return 'none'
        

    def unreg():
            a = 1#here comes database method for reg

    def chaos():
        a =1#chaos maker

class Inv(Position): 
    def __init__(self):
        super().__init__(0.6867, 0.5794, 12, 5, 36.1818, 37.25)

class Stash(Position): 
    def __init__(self):
        super().__init__(0.020498, 0.196614, 12, 12, 36.5454, 36.1818)
        archive_stash_type = open(r'C:\Users\sonvi\Documents\6 - InvManag\Tab\Tab_List.txt')
        stash_type = [line.split() for line in archive_stash_type.readlines()]
        path = r'C:\Users\sonvi\Documents\6 - InvManag\Tab\{}.txt'
        self.stash_dict = {
        }
        for i in range(0, len(stash_type)):
            aux = open(path.format(stash_type[i]),'r')
            aux2 = ''
            aux2 = aux2.join(stash_type[i])
            aux3 = ''
            aux3 = aux3.join(aux.readlines())
            self.stash_dict[aux2] = {aux3}


class Stash4(Position):
    def __init__(self):
        super().__init__(0.0102, 0.1771, 48, 48, 9, 9)

    
