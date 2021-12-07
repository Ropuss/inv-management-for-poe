import pickle

class matrix():
    def __init__(self, quad = None, n): #create matrix n numero da aba matrix
        self.m = []
        self.length = 12
        if quad is not None:
            self.length = 48
        try :
            self.m = self.get_matrix(self, n)
        except FileNotFoundError:
            for y in range(self.length):
                linha = []
                for x in range(self.length):
                    linha.append(True)
                self.m.append(linha)

    def search_empty(self, height, width): #look for empty spot
        space = True
        for x in range(self.length):
            for y in range(self.length):

                if self.m[x][y]:
                    for j in range(height):
                        if y + j < self.length:
                            for i in range(width):
                                if x + i < self.length:
                                    space = space and self.m[x + i][y + j]
                                else:
                                    space = False
                        else:
                            space = False
                    if space:
                        return [x, y]
                space = True
                    
        return False             

    def set_item(self, height, width): #mark the item 
        coord = self.search_empty(height, width)
        for x in range(width):
            for y in range(height):
                self.m[coord[0] + x][coord[1] + y] = False

    def get_item(self, height, width, coord): #remove the item
        for x in range(width):
            for y in range(height):
                self.m[coord[0] + x][coord[1] + y] = True

    def store_matrix(self, n): #store matrix
        with open('matrix' + n,'wb') as fp: #position matrix inventory manager
            pickle.dump(self.m,fp)

    def get_matrix(self, n):
        with open('matrix' + n, 'rb') as fp
            return pickle.load(fp)
        
