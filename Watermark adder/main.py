import tkinter
import os
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, watermark_text, folder_name):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 32)
    width, height = image.size
    x = width - width/4
    y = height - height/4
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Save the image with the watermark in the specified folder
    image.save(os.path.join(folder_name, watermark_text + "_" + os.path.basename(image_path)))

def add_watermarks(image_list, watermark_text, folder_name):
    for image in image_list:
        add_watermark(image, watermark_text, folder_name)

window = tkinter.Tk()
window.config(padx=20,pady=20)
window.geometry("250x200")

def openfile():
    images = filedialog.askopenfilenames()
    if len(images) > 0:
        tick_label = tkinter.Label(text="✔")
        tick_label.pack()
        watermark_label = tkinter.Label(window, text="Enter the watermark text:")
        watermark_label.pack()
        watermark_entry = tkinter.Entry(window)
        watermark_entry.pack()
        folder_label = tkinter.Label(window, text="Enter the folder name:")
        folder_label.pack()
        folder_entry = tkinter.Entry(window)
        folder_entry.pack()
        enter_mark = tkinter.Button(window, text="Add watermark", command=lambda: add_watermarks(images, watermark_entry.get(), folder_entry.get()))
        enter_mark.pack()
    else:
        pass

btn = tkinter.Button(window, text="Import your images", command=openfile)
btn.pack()
window.mainloop()
