from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import glob

#initialize the gooey
gui = Tk()
#Gooey Dimensions (width, height)
gui.geometry("1000x600")
#Gooey Name
gui.title("Scute Picker")
pagenum = 1
max_key_points = 0

img_list = []
folder_path = None

image_number = 0

dict = {}
coords = []


def changepage():
    global pagenum
    for widget in gui.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2()
        pagenum = 2
    elif pagenum == 2:
        page3()
        pagenum = 3


def page1():
    canvas1 = Canvas(gui, width=400, height=300, relief='raised')
    canvas1.pack()

    label1 = Label(gui, text='Initialize max number of key points per picture')
    label1.config(font=('helvetica', 25))
    canvas1.create_window(200, 25, window=label1)

    label2 = Label(gui, text='Type the max number of key points:')
    label2.config(font=('helvetica', 20))
    canvas1.create_window(200, 100, window=label2)

    entry1 = Entry(gui)
    canvas1.create_window(200, 140, window=entry1)

    def save_max_key_points():
        global max_key_points
        max_key_points = entry1.get()
        print(max_key_points)
        changepage()

    button1 = Button(text='Next Page', command=save_max_key_points)
    canvas1.create_window(200, 180, window=button1)


def page2():
    photos = []

    def getFolderPath():
        global folder_path
        folder_selected = filedialog.askdirectory()
        folderPath.set(folder_selected)
        folder_path = folderPath.get() + '/*'
        print(folder_path)
        # for path in photos:
        #     string1 = path
        #     name = string1[11:len(string1) - 4]
        #
        #     tkimage = PhotoImage(file=path)
        #
        #     photo = (tkimage, name)
        #     photos.append(photo)

    folderPath = StringVar()
    a = Label(gui ,text="Find Folder")
    a.grid(row=0,column = 0)
    E = Entry(gui,textvariable=folderPath)
    E.grid(row=0,column=1)
    btnFind = Button(gui, text="Browse",command=getFolderPath)
    btnFind.grid(row=0,column=2)

    c = Button(gui ,text="Next Page", command=changepage)
    c.grid(row=4,column=0)


def page3():
    path_list = glob.glob(folder_path)

    for file in path_list:
        path = file
        img = Image.open(path)
        width, height = img.size
        factor = 1000/height

        newHeight = 1000
        newWidth = width * factor
        # PIL solution
        img = img.resize((int(newWidth), int(newHeight)), Image.ANTIALIAS)  # The (250, 250) is (width, height)
        park_img = ImageTk.PhotoImage(img)
        img_list.append(park_img)

    def save_coords_and_paint (event):
        if len(coords) >= int(max_key_points):
            None
        else:
            click_loc = [canvas.canvasx(event.x), canvas.canvasy(event.y)]
            # print("you clicked on", click_loc)
            coords.append(click_loc)
            dict[image_number] = coords

            # Paint part of code
            python_white = '#FFFFFF'
            x1, y1 = (canvas.canvasx(event.x) - 1), (canvas.canvasy(event.y) - 1)
            x2, y2 = (canvas.canvasx(event.x) + 1), (canvas.canvasy(event.y) + 1)
            canvas.create_oval(x1, y1, x2, y2, fill=python_white, outline=python_white, width=10, tags="dot")

    def backwards():
        global coords
        global image_number
        if image_number == 0:
            pass
        else:
            canvas.delete("dot")
            coords = []
            image_number = image_number - 1
            load()


    def forward():
        global coords
        global image_number
        if image_number < len(path_list) - 1:
            canvas.delete("dot")
            coords = []
            image_number = image_number + 1
            load()

    def load():
        img = img_list[image_number]
        canvas.itemconfig(image_on_canvas, image=img, anchor="nw")
        load_dots()


    def reset():
        global coords
        dict[image_number] = []
        canvas.delete("dot")
        coords = []


    def reject():
        reset()
        forward()

    def load_dots():
        global coords
        global dict
        if image_number in dict:
            coords = dict[image_number]
            python_white = '#FFFFFF'
            for coord in coords:
                eventx, eventy = coord[0], coord[1]
                x1, y1 = (eventx - 1), (eventy - 1)
                x2, y2 = (eventx + 1), (eventy + 1)
                canvas.create_oval(x1, y1, x2, y2, fill=python_white, outline=python_white, width=10, tags="dot")
        else:
            coords = []

    canvas = Canvas(gui, width = 600, height = 600)
    canvas.pack(expand=YES, fill=BOTH, side="left")
    img = img_list[image_number]
    image_on_canvas = canvas.create_image(0, 0, image=img, anchor="nw")
    scrollbar = Scrollbar(gui)
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox(ALL))
    scrollbar.pack(side="right",fill=Y)
    canvas.bind("<Button-1>", save_coords_and_paint)
    B = Button(gui, text ="Back", command = backwards, pady = 10)
    B.pack()
    C = Button(gui, text ="Next", command = forward, pady = 10)
    C.pack()
    D = Button(gui, text ="Reset", command = reset, pady = 10)
    D.pack()
    E = Button(gui, text="Reject", command=reject, pady = 10)
    E.pack()


page1()
gui.mainloop()