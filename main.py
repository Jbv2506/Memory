from Memory2 import *

def clic(event):
    if clics[1] is not None:
        return
    col_pos_clic = event.x // 200
    line_pos_clic = event.y // 200
    if board.grid[line_pos_clic][col_pos_clic] != -1:
        board.handle_move(line_pos_clic, col_pos_clic)


board=Board(10,5,4,clic)


board.init_grid()
board.init_canvas()
board.root.mainloop()
