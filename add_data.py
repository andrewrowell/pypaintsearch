import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


class app(tk.Frame):

    def getNext(self):
        self.x.set(self.x.get() + 1)
        if self.x.get() > 8:
            self.x.set(0)
            self.y.set(self.y.get() + 1)
        x1 = 800*self.x.get()
        y1 = 800*self.y.get()
        x2 = 800*(self.x.get() + 1)
        y2 = 800*(self.y.get() + 1)
        self.load = self.main_image.crop(box=(x1,y1,x2,y2))
        draw = ImageDraw.Draw(self.load)
        print(x1,x2,y1,y2)
        print(self.data)
        for item in self.data:
            if item[0] > x1 and item[0] < x2 and item[1] > y1 and item[1] < y2:
                draw.ellipse([(item[0] - x1 - 30,item[1] - y1 - 30), (item[0] - x1 + 30,item[1] - y1 + 30)], fill = (255,0,0,155))
        self.render = ImageTk.PhotoImage(self.load)
        self.img.configure(image=self.render)
        return

    def __init__(self, master=None):
        tk.Frame.__init__(self)
        infile = open("data.csv", "r")
        self.data = [x.replace("\n","").split(",") for x in infile.readlines()[2:]]
        self.data = [[int(x[0]), int(x[1]), x[2], x[3]] for x in self.data]
        print(self.data)
        infile.close()
        self.master.title('Add Data')
        self.x = tk.DoubleVar()
        self.y = tk.DoubleVar()
        self.main_image = Image.open("images/high-def.png")
        x1 = 800*self.x.get()
        y1 = 800*self.y.get()
        x2 = 800*(self.x.get() + 1)
        y2 = 800*(self.y.get() + 1)
        self.load = self.main_image.crop(box=(x1,y1,x2,y2))
        draw = ImageDraw.Draw(self.load)
        for item in self.data:
            if item[0] > x1 and item[0] < x2 and item[1] > y1 and item[1] < y2:
                draw.ellipse([(item[0] - x1 - 40,item[0] - y1 - 40), (item[0] - x1 + 40,item[0] - y1 + 40)], fill = (255,0,0,255))
        self.render = ImageTk.PhotoImage(self.load)
        self.img = tk.Label(image=self.render)
        self.img.pack()
        self.nextButton = tk.Button(text="-->", command=self.getNext)
        self.nextButton.pack()




#window.mainloop()

root = tk.Tk()
a = app(root)
root.mainloop()
