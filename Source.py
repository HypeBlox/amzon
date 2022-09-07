from tkinter import *
from PIL import ImageTk, Image
import requests
from io import BytesIO

win = Tk()
win.title("Amzon")
win.geometry('650x550')

responseico = requests.get("https://cdn.discordapp.com/attachments/986200496094183466/1017125339870273556/icon.png?size=4096")
ico = Image.open(BytesIO(responseico.content))
photo = ImageTk.PhotoImage(ico)
win.wm_iconphoto(True, photo)

yes = Label(win, borderwidth=0, bg="white")
yes.place(x = 0, y = 94)

response = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017118795187363881/bar.png?size=4096")
img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
label = Label(win, image = img, borderwidth=0)
label.place(x = 0, y = 0)
label.photo = img

response2 = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017119141901127720/Navbar.png?size=4096")
img2 = ImageTk.PhotoImage(Image.open(BytesIO(response2.content)))
label2 = Label(win, image = img2, borderwidth=0)
label2.place(x = 0, y = 54)
label2.photo = img2

response3 = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017121517911408711/Ad.png?size=4096")
img3 = ImageTk.PhotoImage(Image.open(BytesIO(response3.content)))
ad=Label(win, image = img3, borderwidth=0)
ad.place(x=87,y=94)

def scam(a,b,c,d,e,label):
   a.destroy()
   b.destroy()
   c.destroy()
   d.destroy()
   e.destroy()

   response_purchase = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017147997890560161/Getscam.png?size=4096")
   img_purchase = ImageTk.PhotoImage(Image.open(BytesIO(response_purchase.content)))
   label.configure(image=img_purchase)
   label.photo = img_purchase

def prescam(a,b,c, label):
   a.destroy()
   b.destroy()
   c.destroy()

   response_purchase = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017133920938102844/Purchase.png?size=4096")
   img_purchase = ImageTk.PhotoImage(Image.open(BytesIO(response_purchase.content)))
   label.configure(image=img_purchase)
   label.photo = img_purchase

   e = Entry(win)
   e.place(x=193, y=222)
   e2 = Entry(win)
   e2.place(x=193, y=249)
   e3 = Entry(win)
   e3.place(x=321, y=249)
   e4 = Entry(win)
   e4.place(x=195, y=316)

   biy = requests.get("https://cdn.discordapp.com/attachments/986200496094183466/1017141097673261076/Buy.png?size=4096")
   bay = ImageTk.PhotoImage(Image.open(BytesIO(biy.content)))
   buy=Button(win, image=bay, borderwidth=0)
   buy.configure(command=lambda:scam(e,e2,e3,e4,buy,label))
   buy.photo = bay
   buy.place(x=160, y=380)

response4 = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017122683881799690/Select1.png?size=4096")
img4 = ImageTk.PhotoImage(Image.open(BytesIO(response4.content)))
btn=Button(win, image=img4, borderwidth=0)
btn.configure(command=lambda:prescam(btn,btn2,ad,yes))
btn.place(x=87, y=335)

response5 = requests.get("https://cdn.discordapp.com/attachments/772470401057685544/1017123896970969118/Select2.png?size=4096")
img5 = ImageTk.PhotoImage(Image.open(BytesIO(response5.content)))
btn2=Button(win, image=img5, borderwidth=0)
btn2.configure(command=lambda:prescam(btn2,btn,ad,yes))
btn2.place(x=325, y=335)

win.configure(bg='white', highlightthickness=0)
win.resizable(False,False)
win.mainloop()