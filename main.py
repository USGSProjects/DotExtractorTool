from tkinter import *
from PIL import ImageTk,Image
import glob

#initialize the gooey
gui = Tk()
#Gooey Dimensions (width, height)
gui.geometry("1000x600")
#Gooey Name
gui.title("Scute Picker")
parking_img_list = []

dict = {}
coords = []

#folder path is parking_img_path, add * to get all files
parking_img_path = 'folder/path'
parking_path_list = glob.glob(parking_img_path)

for parking_file in parking_path_list:
    path = parking_file
    img = Image.open(path)
    width, height = img.size
    factor = 1000/height

    newHeight = 1000
    newWidth = width * factor
    # PIL solution
    img = img.resize((int(newWidth), int(newHeight)), Image.ANTIALIAS)  # The (250, 250) is (width, height)
    park_img = ImageTk.PhotoImage(img)
    parking_img_list.append(park_img)

image_number = 0


def save_coords_and_paint (event):
    click_loc = [canvas.canvasx(event.x), canvas.canvasy(event.y)]
    # print("you clicked on", click_loc)
    coords.append(click_loc)
    dict[image_number] = coords

    #Paint part of code
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
    if image_number < len(parking_path_list) - 1:
        canvas.delete("dot")
        coords = []
        image_number = image_number + 1
        load()

def load():
    img = parking_img_list[image_number]
    canvas.itemconfig(image_on_canvas, image=img, anchor="nw")
    load_dots()


def reset():
    global coords
    dict[image_number] = []
    canvas.delete("dot")
    coords = []

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
img = parking_img_list[image_number]
image_on_canvas = canvas.create_image(0, 0, image=img, anchor="nw")
scrollbar = Scrollbar(gui)
scrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox(ALL))
scrollbar.pack(side="right",fill=Y)
canvas.bind("<Button-1>", save_coords_and_paint)
B = Button(gui, text ="Back", command = backwards)
B.pack()
C = Button(gui, text ="Next", command = forward)
C.pack()
D = Button(gui, text ="Reset", command = reset)
D.pack()
gui.mainloop()

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from PIL import Image
#
# gui = Tk()
# gui.geometry("700x700")
# gui.title("Scute Picker")
#
#
# photos = []
# def getFolderPath():
#     folder_selected = filedialog.askdirectory()
#     folderPath.set(folder_selected)
#     for path in photos:
#         string1 = path
#         name = string1[11:len(string1) - 4]
#
#         tkimage = PhotoImage(file=path)
#
#         photo = (tkimage, name)
#         photos.append(photo)
#
# def doStuff():
#     folder = folderPath.get()
#     print("Doing stuff with folder", folder)
#
# folderPath = StringVar()
# a = Label(gui ,text="Enter name")
# a.grid(row=0,column = 0)
# E = Entry(gui,textvariable=folderPath)
# E.grid(row=0,column=1)
# btnFind = ttk.Button(gui, text="Browse Folder",command=getFolderPath)
# btnFind.grid(row=0,column=2)
#
# c = ttk.Button(gui ,text="find", command=doStuff)
# c.grid(row=4,column=0)
# gui.mainloop()
