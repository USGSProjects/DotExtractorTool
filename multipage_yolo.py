from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import glob
import os
import csv

# initialize the gooey
gui = Tk()
# Gooey Dimensions (width, height)
gui.geometry("1000x600")
# Gooey Name
gui.title("Scute Picker")
pagenum = 1

img_list = []
original_folder_path = ""
folder_path = ""

image_number = 0

dict = {}
coords = []
resized_dimensions = {}

image_indicator = StringVar()
image_indicator.set("N/A")

image_name = StringVar()
image_name.set("N/A")

# A class to hold the information for the original photo, resized image, and image name
class MyImage:
    def __init__(self, img, resized_img, img_name):
        self.img = img
        self.processed_img = resized_img
        self.__name = img_name

    def __str__(self):
        return self.__name


# Function that changes deletes current page to goes to next page
def changepage():
    global pagenum
    for widget in gui.winfo_children():
        widget.destroy()
    if pagenum == 1:
        page2()
        pagenum = 2


# This is a page that is used to pick the folder that images will taken from
def page1():
    waiting_text = StringVar()
    waiting_text.set("")

    loading_indicator_label = Label(gui, textvariable=waiting_text)
    loading_indicator_label.grid(row=5, column=0)

    def getFolderPath():
        global folder_path
        global original_folder_path
        folder_selected = filedialog.askdirectory()
        folderPath.set(folder_selected)
        folder_path = folderPath.get() + '/*'
        original_folder_path = folderPath.get() + '/'

    def change_loading_text():
        print(folder_path.strip())
        if folder_path is None or folder_path.strip() == "":
            messagebox.showerror(title="Error", message="No Folder Selected")
        else:
            waiting_text.set("Loading...")
            # Needs to add wait statement to ensure waiting text UI change
            gui.after(10, load_photo_and_change_page)

    def load_photo_and_change_page():
        path_list = glob.glob(folder_path)
        for file in path_list:
            path = file
            head, tail = os.path.split(path)
            print(tail)
            try:
                img = Image.open(path)
                width, height = img.size

                newHeight = 1000
                factor = newHeight / height

                newWidth = width * factor
                resized_dimensions[tail] = [newWidth, newHeight]
                # PIL solution
                img = img.resize((int(newWidth), int(newHeight)), Image.ANTIALIAS)  # The (250, 250) is (width, height)
                new_img = ImageTk.PhotoImage(img)
                photo = MyImage(img, new_img, tail)
                img_list.append(photo)
            except:
                None

        image_indicator.set(str(image_number + 1) + "/" + str(len(img_list)))
        image_name.set(str(img_list[image_number]))
        changepage()

    folderPath = StringVar()
    find_folder_label = Label(gui, text="Find Folder")
    find_folder_label.grid(row=0, column=0)
    folderpath_entry = Entry(gui, textvariable=folderPath)
    folderpath_entry.grid(row=0, column=1)
    browse_button = Button(gui, text="Browse", command=getFolderPath)
    browse_button.grid(row=0, column=2)

    next_page_button = Button(gui, text="Next Page", command=change_loading_text)
    next_page_button.grid(row=4, column=0)


# This is the page where photo annotations will be made
def page2():
    def save_coords_and_paint(event):
        click_loc = [canvas.canvasx(event.x), canvas.canvasy(event.y)]
        # print("you clicked on", click_loc)
        coords.append(click_loc)
        dict[str(img_list[image_number])] = coords

        # Plotting part of code
        python_white = '#FFFFFF'
        x1, y1 = (canvas.canvasx(event.x) - 5), (canvas.canvasy(event.y) - 5)
        x2, y2 = (canvas.canvasx(event.x) + 5), (canvas.canvasy(event.y) + 5)
        canvas.create_rectangle(x1, y1, x2, y2, fill=python_white, outline=python_white, width=10, tags="dot")

    def backwards():
        global coords
        global image_number
        if image_number == 0:
            messagebox.showerror(title="Error", message="No More Photos")
        else:
            canvas.delete("dot")
            coords = []
            image_number = image_number - 1
            load()

        image_indicator.set(str(image_number + 1) + "/" + str(len(img_list)))
        image_name.set(str(img_list[image_number]))

    def forward():
        global coords
        global image_number
        if image_number < len(img_list) - 1:
            canvas.delete("dot")
            coords = []
            image_number = image_number + 1
            load()
        else:
            messagebox.showerror(title="Error", message="No More Photos")

        image_indicator.set(str(image_number + 1) + "/" + str(len(img_list)))
        image_name.set(str(img_list[image_number]))

    def load():
        img = img_list[image_number].processed_img
        canvas.itemconfig(image_on_canvas, image=img, anchor="nw")
        load_dots()

    def reset():
        global coords
        dict[str(img_list[image_number])] = []
        canvas.delete("dot")
        coords = []

    def reject():
        global image_number
        if image_number < len(img_list) - 1:
            reset()
            forward()
        else:
            reset()

    def save():
        # code to save stuff
        files = [('CSV Files', '*.csv'),
                 ('All Files', '*.*')]
        file = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
        if file is None:
            return
        csv_writer = csv.writer(open(file.name, "w"))
        csv_writer.writerow(["ID", "Coordinates"])
        for key, val in dict.items():
            keyWithoutExtension = os.path.splitext(key)[0]
            # This clears the text file from any previous usage of the program
            yolo_text_file = open(original_folder_path + keyWithoutExtension + ".txt", "a+")
            yolo_text_file.truncate(0)
            newlist = []
            # creates the coordinates for the box's vertices
            for coord in val:
                # The format for yolo is <object-class> <x> <y> <width> <height>
                # Everything is divided by factor to match with the original image size
                x_coordinate = coord[0]/resized_dimensions[key][0]
                y_coordinate = coord[1]/resized_dimensions[key][1]
                width = 10/resized_dimensions[key][0]
                height = 10/resized_dimensions[key][1]
                newlist.append([x_coordinate, y_coordinate])
                textToAppend = "0 " + str(x_coordinate) + " " + str(y_coordinate) + " " + str(width) + " " + str(height)
                yolo_text_file.write(textToAppend + "\n")

            csv_writer.writerow([key, newlist])
            yolo_text_file.close()

        gui.destroy()

    def undo():
        global coords
        if not coords:
            messagebox.showerror(title="Error", message="No Coordinates to Undo")

        else:
            coords.pop()
            dict[str(img_list[image_number])] = coords
            canvas.delete("dot")
            load_dots()

    def load_dots():
        global coords
        global dict
        if str(img_list[image_number]) in dict:
            coords = dict[str(img_list[image_number])]
            python_white = '#FFFFFF'
            for coord in coords:
                eventx, eventy = coord[0], coord[1]
                x1, y1 = (eventx - 5), (eventy - 5)
                x2, y2 = (eventx + 5), (eventy + 5)
                canvas.create_rectangle(x1, y1, x2, y2, fill=python_white, outline=python_white, width=10, tags="dot")
        else:
            coords = []

    img_name_label = Label(gui, textvariable=image_name)
    img_name_label.pack()
    canvas = Canvas(gui, width=600, height=600)
    canvas.pack(expand=YES, fill=BOTH, side="left")
    img = img_list[image_number].processed_img
    image_on_canvas = canvas.create_image(0, 0, image=img, anchor="nw")
    vertical_scrollbar = Scrollbar(gui)
    vertical_scrollbar.config(command=canvas.yview)
    horizontal_scrollbar = Scrollbar(gui, orient="horizontal")
    horizontal_scrollbar.config(command=canvas.xview)
    canvas.config(xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set,
                  scrollregion=canvas.bbox(ALL))
    vertical_scrollbar.pack(side="right", fill=Y)
    horizontal_scrollbar.pack(side="bottom", fill=X)
    canvas.bind("<Button-1>", save_coords_and_paint)
    # Buttons for the second page
    back_button = Button(gui, text="Back", command=backwards, pady=10)
    back_button.pack()
    next_button = Button(gui, text="Next", command=forward, pady=10)
    next_button.pack()
    reset_button = Button(gui, text="Reset", command=reset, pady=10)
    reset_button.pack()
    reject_button = Button(gui, text="Reject", command=reject, pady=10)
    reject_button.pack()
    undo_button = Button(gui, text="Undo", command=undo, pady=10)
    undo_button.pack()
    done_button = Button(gui, text="Done", command=save, pady=10)
    done_button.pack()
    image_number_label = Label(gui, textvariable=image_indicator)
    image_number_label.pack()


page1()
gui.mainloop()