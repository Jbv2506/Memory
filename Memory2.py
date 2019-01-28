from tkinter import *
from random import *
from PIL import ImageTk, Image

clics = [None, None]
x_position = [100, 300, 500, 700]
y_position = [100, 300, 500, 700, 900]
image = ['Images_Memory/bleu.png', 'Images_Memory/gris.png', 'Images_Memory/jaune.png', 'Images_Memory/noir.png',
         'Images_Memory/orange.png', 'Images_Memory/rose.png', 'Images_Memory/rouge.png',
         'Images_Memory/turquoise.png', 'Images_Memory/vert.png', 'Images_Memory/violet.png']
class Board:
    def __init__(self, nb_cards, nb_line, nb_col,clic_fct):
        self.nb_cards = nb_cards
        self.nb_line = nb_line
        self.nb_col = nb_col
        self.clic_fct=clic_fct
        self.height = 200 * nb_line
        self.withd = 200 * nb_col
        self.grid = []
        self.root = Tk()
        self.root.title("Memory")
        self.canvas = Canvas(self.root, width=self.withd, height=self.height, bg="ivory")
        self.click = [None, None]
        self.ids_logo = [[None for j in range(nb_col)] for i in range(nb_line)]
        self.clics = [None, None]
        self.col_position_clic = 0
        self.line_position_clic = 0
        self.state = True
        self.step = 0
        self.cover = "Images_Memory/cover.png"
        self.logo = PhotoImage(file=self.cover)
        self.logo_image = [ImageTk.PhotoImage(file=filename) for filename in image]

    def init_grid(self):
        L = [Card(i // 2, x_position[i // 5], y_position[i % 4]) for i in range(self.nb_cards * 2)]
        M = [cards.id_carte for cards in L]
        shuffle(M)
        k = 0
        for line in range(self.nb_line):
            row = []
            for col in range(self.nb_col):
                row.append(M[k])
                k = k + 1
            self.grid.append(row)

    def init_canvas(self):
        for line in range(self.nb_line):
            for col in range(self.nb_col):
                x, y = x_position[col], y_position[line]
                numero_image = self.grid[line][col]
                mon_image = self.logo_image[numero_image]
                self.canvas.create_image(x, y, image=mon_image)
                self.id_logo = self.canvas.create_image(x, y, image=self.logo)
                self.ids_logo[line][col] = (self.id_logo)
                self.canvas.pack()
                self.canvas.bind('<Button>', self.clic_fct)



    def hide(self, line_0, col_0, line_1, col_1):
        self.ids_logo[line_0][col_0] = self.canvas.create_image(x_position[col_0], y_position[line_0], image=self.logo)
        self.ids_logo[line_1][col_1] = self.canvas.create_image(x_position[col_1], y_position[line_1], image=self.logo)
        clics[0] = clics[1] = None

    def handle_move(self, line_pos, col_pos):
        self.col_position_clic, self.line_position_clic = col_pos, line_pos
        self.canvas.delete(self.ids_logo[self.line_position_clic][self.col_position_clic])
        if clics[0] is None:
            clics[0] = (self.line_position_clic, self.col_position_clic)
        else:
            if clics[0] == (self.line_position_clic, self.col_position_clic):
                return
            clics[1] = (self.line_position_clic, self.col_position_clic)
            line_0, col_0 = clics[0]
            if self.grid[line_0][col_0] == self.grid[self.line_position_clic][self.col_position_clic] != -1:
                self.grid[line_0][col_0] = self.grid[self.line_position_clic][self.col_position_clic] = -1
                clics[0] = clics[1] = None
                self.step = self.step + 1
                self.is_finished()
            else:
                self.canvas.after(500, self.hide, line_0, col_0, self.line_position_clic, self.col_position_clic)
        if self.state is not True:
            self.root.destroy()

    def clic_fct(self,event):
        if clics[1] is not None:
            return
        col_pos_clic = event.x // 200
        line_pos_clic = event.y // 200
        if self.grid[line_pos_clic][col_pos_clic] != -1:
            self.handle_move(line_pos_clic, col_pos_clic)

    def is_finished(self):
        if self.step == self.nb_cards:
            self.state = False


class Card:
    def __init__(self, id_carte, x_position, y_position):
        self.height = 200
        self.withd = 200
        self.id_carte = id_carte
        self.color = 'None'
        self.x_position = x_position
        self.y_position = y_position

    def init_color(self):
        self.color = Image[self.id_carte]





def launch_game(board):
    board.init_grid()
    board.init_canvas()

    board.root.mainloop()








