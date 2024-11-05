from tkinter import*
import customtkinter as ctk
from PIL import Image, ImageTk
import random
from tkinter import messagebox


up=0
rp=0
c=0
def playagain():
    global c, rp, up
    wname.pack_forget()
    wpicr.pack_forget()
    wpicu.pack_forget()
    wtitler.pack_forget()
    wtitleu.pack_forget()
    pag.pack_forget()
    winnerframe.pack_forget()
    robochlbl.place_forget()
    userchlbl.place_forget()
    up=0
    rp=0
    c=0
    
    rockbtn.config(state=NORMAL)
    paperbtn.config(state=NORMAL)
    scibtn.config(state=NORMAL)
    rplbl.config(text=f"Robot Point:{rp}")
    uplbl.config(text=f"User Point:{up}")
    statuslbl1.place_forget()
    statuslbl2.place_forget()
    dashframe.pack()
    contentframe.pack()
    rc=f'R o u n d : {0}'
    rounder.configure(text=rc)
    
def winner():
    global c, rp, up
    contentframe.pack_forget()
    winnerframe.pack()
    wname.pack(side=TOP,pady=(70,10))
    if int(rp)==int(up):
        wname.pack(pady=200)
        wname.config(text='Match-Draw')
        pag.pack()

    elif int(rp)>int(up):
        wpicr.pack(pady=(5,10))
        wtitler.pack()
        pag.pack()


    elif int(rp)<int(up):
        wpicu.pack(pady=(5,10))
        wtitleu.pack()
        pag.pack()

def count():
    global c, rp, up
    c=c+1
    rc=f'R o u n d : {c}'
    rounder.configure(text=rc)
    if c==int(bstval.get()):
        rc=f'R o u n d : {c}'
        rounder.configure(text=rc)
        rockbtn.config(state=DISABLED)
        paperbtn.config(state=DISABLED)
        scibtn.config(state=DISABLED)
        
        if int(rp)==int(up):
            statuslbl1.config(text="MATCH DRAW",fg="white",bg="#bb8fce")
            statuslbl2.config(text="MATCH DRAW",fg="white",bg="#bb8fce")
            winnerframe.after(1000,winner)
        elif int(rp)>int(up):
            statuslbl1.config(text="WON",fg="white",bg="Green")
            statuslbl2.config(text="LOST",fg="white",bg="red")
            winnerframe.after(1000,winner)
        elif int(rp)<int(up):
            statuslbl1.config(text="LOST",fg="white",bg="red")
            statuslbl2.config(text="WON",fg="white",bg="green")
            winnerframe.after(1000,winner)

def resize_image(image_path, new_width, new_height=None):

    image = Image.open(image_path)

    if new_height is None:
        width, height = image.size
        new_height = int((new_width / width) * height)

    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)
    return photo

def compare(rp,up):
    if int(rp)==int(up):
        statuslbl1.place(x=150,y=400)
        statuslbl1.config(text="Tie",bg="blue",fg="white")

        statuslbl2.place(x=550,y=400)
        statuslbl2.config(text="Tie",bg="blue",fg="white")
    elif int(rp)>int(up):
        statuslbl1.place(x=150,y=400)
        statuslbl1.config(text="Wining",bg="Green",fg="white")

        statuslbl2.place(x=550,y=400)
        statuslbl2.config(text="Losing",bg="red",fg="white")
    elif int(rp)<int(up):
        statuslbl1.place(x=150,y=400)
        statuslbl1.config(text="Losing",bg="red",fg="white")

        statuslbl2.place(x=550,y=400)
        statuslbl2.config(text="Wining",bg="green",fg="white")
    
def change_button_color():

    colors = [ "green", "blue", "purple", "pink", "brown"]

    new_color = random.choice(colors)

    playbtn.config(bg=new_color)

    playbtn.after(500, change_button_color)


def play():
    try:
        int(bstval.get())
        dashframe.pack_forget()

        win.config(bg="#bb8fce")
        rounder.pack(pady=10)
        seperator.pack(pady=(10,0))

        robolbl.place(x=150,y=30)
        userlbl.place(x=550,y=30)

        rockbtn.place(x=300,y=455)
        paperbtn.place(x=380,y=455)
        scibtn.place(x=460,y=455)

        rplbl.place(y=130,x=120)

        uplbl.place(y=130,x=520)
    except ValueError:
        messagebox.showerror("Error", "Best of only accepts INTEGER value!")

def r():
    global rp, up
    robopt=['rocks.png','paper.png','scissors.png']
    roboimage=random.choice(robopt)
    image_path = roboimage
    new_width = 100
    new_height = 100

    roboimagech=resize_image(image_path,new_width,new_height)
    
    robochlbl.config(image=roboimagech)
    robochlbl.image=roboimagech
    robochlbl.place(x=120,y=170)
    user=rockval.get()
    
    if user==roboimage:
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        statuslbl1.config(text="Choosen the same thought!!",fg="white",bg="blue")
        statuslbl2.config(text="Choosen the same thought!!",fg="white",bg="blue")
    
    elif user=='rocks.png' and roboimage=='paper.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        rp=rp+1
        rp=str(rp)
        rplbl.config(text=f"Robot Point:{rp}")
        rp=int(rp)

        compare(rp,up)            

    elif user=='rocks.png' and roboimage=='scissors.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        up=up+1
        up=str(up)
        uplbl.config(text=f"User Point:{up}")
        up=int(up)
        compare(rp,up) 

def p():
    global rp, up

    robopt=['rocks.png','paper.png','scissors.png']
    roboimage=random.choice(robopt)
    image_path = roboimage
    new_width = 100
    new_height = 100

    roboimagech=resize_image(image_path,new_width,new_height)
    robochlbl.config(image=roboimagech)
    robochlbl.image=roboimagech
    robochlbl.place(x=120,y=170)
    user=paperval.get()

    if user==roboimage:
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        statuslbl1.config(text="Choosen the same thought!!",fg="white",bg="blue")
        statuslbl2.config(text="Choosen the same thought!!",fg="white",bg="blue")
    
    elif user=='paper.png' and roboimage=='rocks.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        up=up+1
        up=str(up)
        uplbl.config(text=f"User Point:{up}")
        up=int(up)
        compare(rp,up) 

    elif user=='paper.png' and roboimage=='scissors.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        rp=rp+1
        rp=str(rp)
        rplbl.config(text=f"Robot Point:{rp}")
        rp=int(rp)
        compare(rp,up) 

def s():
    global rp, up

    robopt=['rocks.png','paper.png','scissors.png']
    roboimage=random.choice(robopt)
    image_path = roboimage
    new_width = 100
    new_height = 100

    roboimagech=resize_image(image_path,new_width,new_height)
    
    robochlbl.config(image=roboimagech)
    robochlbl.image=roboimagech
    robochlbl.place(x=120,y=170)
    user=scival.get()

    if user==roboimage:
        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)

        statuslbl1.config(text="Choosen the same thought!!",fg="white",bg="blue")
        statuslbl2.config(text="Choosen the same thought!!",fg="white",bg="blue")

    elif user=='scissors.png' and roboimage=='rocks.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        rp=rp+1
        rp=str(rp)
        rplbl.config(text=f"Robot Point:{rp}")
        rp=int(rp)
        compare(rp,up) 

    elif user=='scissors.png' and roboimage=='paper.png':

        image_path1 = user
        new_width1 = 100
        new_height1 = 100

        userimagech=resize_image(image_path1,new_width1,new_height1) 

        userchlbl.config(image=userimagech)
        userchlbl.image=userimagech
        userchlbl.place(x=520,y=170)
        up=up+1
        up=str(up)
        uplbl.config(text=f"User Point:{up}")
        up=int(up)
        compare(rp,up) 


win =Tk()
win.title("Rock,Paper,Scissor")
win.geometry("800x500")
win.config(bg="#bb8fce")
win.iconbitmap("title.ico")

dashframe=Frame(win,height=500,width=800,bg='#bb8fce')
dashframe.propagate(False)
dashframe.pack()


gname=Label(dashframe,text="Rock,Paper,Scissor!",font=("Jokerman",30),fg="#4a235a",bg="#bb8fce")
gname.pack(side=TOP,pady=(70,60))

bstlbl=Label(dashframe,text="Best of:",font=("Bahnschrift",14,'bold'),bg="#bb8fce",fg='#4a235a')
bstlbl.place(x=280,y=150)

bstval=StringVar()
bsten=ctk.CTkEntry(dashframe,textvariable=bstval,font=('Calibri (Body)',12,'bold'),border_color='#4a235a')
bsten.place(x=360,y=150)

image_path = "robot.png"
roboimage=Image.open(image_path)
resized_image = roboimage.resize((100,100))
roboimg_1=ImageTk.PhotoImage(resized_image)

label1 = Label(dashframe, image=roboimg_1,bg='#bb8fce')
label1.pack()
label1.image = roboimg_1

playbtn=Button(dashframe,text="PLAY",font=("ROG Fonts",12),bg="green",fg="white",cursor="hand2",command=play)
playbtn.pack(pady=20)
change_button_color()

contentframe=Frame(win,height=500,width=800,bg='#bb8fce')
contentframe.propagate(False)
contentframe.pack()

rounder=ctk.CTkLabel(contentframe,text="R o u n d: 0",font=("ROG Fonts",12),fg_color='white',
                    text_color='Black',height=30,width=80,corner_radius=20)

seperator=Frame(contentframe,bg="#4a235a",height=410,width=2)

robolbl=Label(contentframe,image=roboimg_1,bg="#bb8fce")

image_path11 = "man.png"
manimage=Image.open(image_path11)
resized_image1 = manimage.resize((100,100))
manimg_1=ImageTk.PhotoImage(resized_image1)


userlbl=Label(contentframe,image=manimg_1,bg="#bb8fce")

image_path2 = "rocks.png"
rkimage=Image.open(image_path2)
resized_image2 = rkimage.resize((40,40))
rkimg_1=ImageTk.PhotoImage(resized_image2)

rockval=StringVar()
rockbtn=Button(contentframe,image=rkimg_1,relief="raised",textvariable=rockval,command=lambda:(r(),count()))
rockval.set(value="rocks.png")

image_path3 = "paper.png"
paperimage=Image.open(image_path3)
resized_image3 = paperimage.resize((40,40))
paperimg_1=ImageTk.PhotoImage(resized_image3)

paperval=StringVar()
paperbtn=Button(contentframe,image=paperimg_1,relief="raised",textvariable=paperval,command=lambda:(p(),count()))
paperval.set(value="paper.png")

image_path4 = "scissors.png"
scciimage=Image.open(image_path4)
resized_image4 = scciimage.resize((40,40))
scciimg_1=ImageTk.PhotoImage(resized_image4)

scival=StringVar()
scibtn=Button(contentframe,image=scciimg_1,relief="raised",textvariable=scival,command=lambda:(s(),count()))
scival.set(value="scissors.png")

robochlbl=Label(contentframe,bg="#bb8fce")

userchlbl=Label(contentframe,bg="#bb8fce")


rplbl=Label(contentframe,text="Robot Point:0",font=("ROG Fonts",12),bg="#bb8fce")

uplbl=Label(contentframe,text="User Point:0",font=("ROG Fonts",12),bg="#bb8fce")


statuslbl1=Label(contentframe,text="Bahnschrift",font=("Bahnschrift",12),bg="#bb8fce")
statuslbl2=Label(contentframe,text="Bahnschrift",font=("Bahnschrift",12),bg="#bb8fce")

winnerframe=Frame(win,height=500,width=800,bg='#bb8fce')
winnerframe.propagate(False)

wname=Label(winnerframe,text="Winner",font=("Jokerman",30),fg="#4a235a",bg="#bb8fce")


wpicr=Label(winnerframe,image=roboimg_1,bg='#bb8fce')
wtitler=Label(winnerframe,text='R o b o t',font=("ROG Fonts",14),bg="#bb8fce",fg='white')
wpicu=Label(winnerframe,image=manimg_1,bg='#bb8fce')
wtitleu=Label(winnerframe,text='U s e r',font=("ROG Fonts",14),bg="#bb8fce",fg='white')
pag=Button(winnerframe,text='Play again',font=('Calibri (Body)',12,'bold'),bg='Blue',fg='white',command=playagain)
    
win.mainloop()
