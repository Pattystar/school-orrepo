import tkinter as tk
import random
# from PIL import ImageTk, Image
# myimg = ImageTk.PhotoImage(Image.open("snake-gif-.gif"))


WIDTH = 600
HEIGHT = 400
PART_SIZE = 20
IN_GAME = True



def create_doping():
    """ Создание жертвы """
    global SOMCHAY
    posx = PART_SIZE * random.randint(1, (WIDTH-PART_SIZE) / PART_SIZE)
    posy = PART_SIZE * random.randint(1, (HEIGHT-PART_SIZE) / PART_SIZE)
    SOMCHAY = c.create_oval(posx, posy,
                          posx+PART_SIZE, posy+PART_SIZE,
                          fill="blue")


def main():
    global IN_GAME
    if IN_GAME:
        s.move()
        head_coords = c.coords(s.parts[-1].instance)
        x1, y1, x2, y2 = head_coords
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        elif head_coords == c.coords(SOMCHAY):
            s.add_part()
            c.delete(SOMCHAY)
            create_doping()
        else:
            for index in range(len(s.parts)-1):
                if head_coords == c.coords(s.parts[index].instance):
                    IN_GAME = False
        root.after(100, main)
    else:
        c.create_text(WIDTH/2, HEIGHT/2,
                      text="YOU LOOSE!! AHAHAHAAA!!!",
                      font="Arial 30",
                      fill="red")


class Part(object):
    """ Отдельная асть змея """
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x+PART_SIZE, y+PART_SIZE,
                                           fill="green")


class Python(object):
    """ Змей в сборе """
    def __init__(self, parts):
        self.parts = parts
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        self.vector = self.mapping["Right"]

    def move(self):
        for index in range(len(self.parts)-1):
            part = self.parts[index].instance
            x1, y1, x2, y2 = c.coords(self.parts[index+1].instance)
            c.coords(part, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.parts[-2].instance)
        c.coords(self.parts[-1].instance,
                 x1+self.vector[0]*PART_SIZE,
                 y1+self.vector[1]*PART_SIZE,
                 x2+self.vector[0]*PART_SIZE,
                 y2+self.vector[1]*PART_SIZE)

    def add_part(self):
        last_part = c.coords(self.parts[0].instance)
        x = last_part[2] - PART_SIZE
        y = last_part[3] - PART_SIZE
        self.parts.insert(0, Part(x, y))

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

# Настройка окна игры
root = tk.Tk()

root.title("Python Yummm")

c = tk.Canvas(root, width=WIDTH, height=HEIGHT)
c.grid()
bg = tk.PhotoImage(file="snake-gif-.gif")
c.create_image(300, 200, image=bg)
c.focus_set()
parts = [Part(PART_SIZE, PART_SIZE),
        Part(PART_SIZE*2, PART_SIZE),
        Part(PART_SIZE*3, PART_SIZE)]
s = Python(parts)
c.bind("<KeyPress>", s.change_direction)

create_doping()
main()
root.mainloop()