
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hashir News Paper")
root.geometry("900x700")

# Title
f0 = Frame(root, width=800, height=70)
f0.pack()
Label(f0, text="Hashir News Paper", font=("Lucida", 33, "bold"), fg="black").pack()

# Read files & images
text_files = ["1.txt", "2.txt", "3.txt"]
image_files = ["1.png", "2.png", "3.png"]

articles = []
photos = []

for tfile, ifile in zip(text_files, image_files):
    with open(tfile, 'r', encoding='utf-8') as file:
        content = file.read()
        articles.append(content)

    image = Image.open(ifile)
    image = image.resize((170, 170))  # Resize for better layout
    photos.append(ImageTk.PhotoImage(image))

# Display news
for i in range(len(articles)):
    frame = Frame(root, pady=13)
    frame.pack(anchor="w")

    img_label = Label(frame, image=photos[i])
    img_label.pack(side=LEFT, padx=10)

    text_label = Label(frame, text=articles[i], wraplength=600, justify=LEFT, font=("Arial", 12))
    text_label.pack(side=LEFT)

root.mainloop()
