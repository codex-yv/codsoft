import sqlite3
from tkinter import*
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk



def search_data(search_input):
    search_input=str(search_input).title()
    conn=sqlite3.connect('contact.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE NAME = ? OR PHONE = ?", (search_input, search_input))

    row=cursor.fetchone()
    
    if row:
        cursor.execute(f"SELECT NAME, PHONE, EMAIL, ADDRESS FROM contacts where PHONE=='{search_input}' or NAME=='{search_input}'")
        rows = cursor.fetchall()
        for item in datadip.get_children():
            datadip.delete(item)
            
        for data in rows :
            datadip.insert("",END,values=data)
        messagebox.showinfo('Search result',f'Contact Found:{search_input}')
    else:
        messagebox.showinfo('Search result',f'Contact Not Found:{search_input}')
    
    conn.close()
    
def update_data_by_phone(db_file, phone_number, new_data,value):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        update_query = f"UPDATE contacts SET {value} = ? WHERE PHONE = ?"
        cursor.execute(update_query, (new_data, phone_number))

        conn.commit()

        if cursor.rowcount > 0:
            display_data_tree()
            messagebox.showinfo('Contact','Contact Updated Successfully!')
        else:
            messagebox.showerror('Contact','No record found with the given phone number.')
        
    except sqlite3.Error as e:
        messagebox.showerror('Error',f"An error occurred: {e}")
    
    finally:
        conn.close()
        
def delete_data(phone_number):
    try:
        db_file = 'contact.db'
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        delete_query = "DELETE FROM contacts WHERE PHONE = ?"
        cursor.execute(delete_query, (phone_number,))

        conn.commit()
        
        if cursor.rowcount > 0:
            display_data_tree()
            messagebox.showinfo('Contact','Contact Deleted Successfully!')
        else:
            messagebox.showerror('Contact','No record found with the given phone number.')
        
    except sqlite3.Error as e:
        messagebox.showerror('Error',f"An error occurred: {e}")
    
    finally:
        conn.close()

def view_contact_tree():
    conn=sqlite3.connect('contact.db')  
    cursor=conn.cursor()

    cursor.execute("SELECT NAME, PHONE FROM contacts")

    rows=cursor.fetchall()
    for items in contactdip.get_children():
        contactdip.delete(items)
    for contacts in rows :
        contactdip.insert("",END,values=contacts)

    conn.close()

def display_data_tree():
    conn=sqlite3.connect('contact.db')
    cursor=conn.cursor()

    select_query="SELECT * FROM contacts;"
    cursor.execute(select_query)

    rows=cursor.fetchall()

    data_list=rows
    conn.close()
    for item in datadip.get_children():
        datadip.delete(item)
        
    for data in data_list :
        datadip.insert("",END,values=data)
 
def change(value):
    if value=='name':
        update__contact_frame.pack_forget()
        update__contact_frame_name.pack(fill=BOTH,expand=True)

    elif value=='phone':
        update__contact_frame.pack_forget()
        update__contact_frame_phone.pack(fill=BOTH,expand=True)
    
    elif value=='email':
        update__contact_frame.pack_forget()
        update__contact_frame_email.pack(fill=BOTH,expand=True)

    elif value=='address':
        update__contact_frame.pack_forget()
        update__contact_frame_address.pack(fill=BOTH,expand=True)
        
    

def final_update(value):
    if value=='name':
        db_file = 'contact.db'  
        phone_number = refval1.get()
        new_data = updatenameval.get() 

        update_data_by_phone(db_file, phone_number, new_data,value)

        
    elif value=='phone':
        db_file = 'contact.db'  
        phone_number = refval2.get()
        new_data = updatephoneval.get() 

        update_data_by_phone(db_file, phone_number, new_data,value)
    
    elif value=='email':
        db_file = 'contact.db'  
        phone_number = refval3.get()
        new_data = updateemailval.get() 

        update_data_by_phone(db_file, phone_number, new_data,value)
    elif value=='address':
        db_file = 'contact.db'  
        phone_number = refval4.get()
        new_data = updataddressval.get() 

        update_data_by_phone(db_file, phone_number, new_data,value)

   
def animation():
    global var_x, var_x1
    var_x1=var_x1-0.01
    var_x=var_x-0.01
    if var_x>0.31:
        contactframe.place(relx=var_x,rely=0.50,anchor='center')
        canvas.after(10, animation)
    if var_x1>0.97:
        infoframe.place(relx=var_x1,rely=0.5,anchor='e')
        canvas.after(10, animation)
         
def view_contact():
    update__contact_frame_name.pack_forget()
    update__contact_frame_phone.pack_forget()
    update__contact_frame_email.pack_forget()
    update__contact_frame_address.pack_forget()
    delete_contact_frame.pack_forget()
    update_contact_frame.pack_forget()
    update__contact_frame.pack_forget()
    search_contact_frame.pack_forget()
    new_contact_frame.pack_forget()
    view_contact_frame.pack(fill=BOTH,expand=True)
    view_contact_tree()

def search_contact():
    update__contact_frame_name.pack_forget()
    update__contact_frame_phone.pack_forget()
    update__contact_frame_email.pack_forget()
    update__contact_frame_address.pack_forget()
    view_contact_frame.pack_forget()
    update_contact_frame.pack_forget()
    update__contact_frame.pack_forget()
    delete_contact_frame.pack_forget()
    new_contact_frame.pack_forget()
    search_contact_frame.pack(fill=BOTH,expand=True)
    
    

def update_contact():
    update__contact_frame_name.pack_forget()
    update__contact_frame_phone.pack_forget()
    update__contact_frame_email.pack_forget()
    update__contact_frame_address.pack_forget()
    view_contact_frame.pack_forget()
    search_contact_frame.pack_forget()
    delete_contact_frame.pack_forget()
    new_contact_frame.pack_forget()
    update__contact_frame.pack_forget()
    update_contact_frame.pack(fill=BOTH,expand=True)

def delete_contact():
    update__contact_frame_name.pack_forget()
    update__contact_frame_phone.pack_forget()
    update__contact_frame_email.pack_forget()
    update__contact_frame_address.pack_forget()
    view_contact_frame.pack_forget()
    search_contact_frame.pack_forget()
    update_contact_frame.pack_forget()
    update__contact_frame.pack_forget()
    new_contact_frame.pack_forget()
    delete_contact_frame.pack(fill=BOTH,expand=True)
        

def new_contact():
    update_contact_frame.pack_forget()
    new_contact_frame.pack(fill=BOTH,expand=True)

def update__contact():
    update_contact_frame.pack_forget()
    update__contact_frame.pack(fill=BOTH,expand=True)

def save_contact():
    try:
        name_val=nameval.get().title()
        phone_val=int(phoneval.get())
        email_val=emialval.get()
        address_val=addressval.get()
        
        conn=sqlite3.connect('contact.db')
        cursor=conn.cursor()

        data=[
            (name_val, phone_val, email_val, address_val)
        ]
        
        insert_query='''
        INSERT INTO contacts (NAME, PHONE, EMAIL, ADDRESS)
        VALUES (?, ?, ?, ?)
        '''

        try:
            cursor.executemany(insert_query, data)
            conn.commit()
            
            display_data_tree()
                
            messagebox.showinfo('Contact info','Contact Saved')
        except sqlite3.IntegrityError as e:
            messagebox.showerror('Duplicate Data',f"Error: Duplicate phone number detected!\nError details: {e}")

        conn.close()
    except ValueError:
        messagebox.showerror('Phone Number',f'Wrong Phone Number:{phoneval.get()}\nONLY INDIAN NUMBERS ARE ALLOWED!')

def clear_inputs():
    nameval.set('')
    phoneval.set('')
    emialval.set('')
    addressval.set('')

def reset():
    search.set('')
    display_data_tree()

win=Tk()
win.geometry("1000x600+200+50")
win.title("Contact Book")
win.iconbitmap('logo.ico')

contentframe=Frame(win,height=600,width=1000,bg='red')
contentframe.propagate(False)
contentframe.pack()

canvas=Canvas(contentframe,height=600,width=1000,bg='black')
canvas.propagate(False)
canvas.pack()

imagepath='image1.png'
openphoto=Image.open(imagepath).resize((1000,600))
bgimage=ImageTk.PhotoImage(openphoto)
canvas.create_image(500,300, image=bgimage)

canvas.create_text(500,10, anchor='n',fill='#1b4f72',text='Contact Manager', font=("Arial Black", 30))
lineframe=Frame(canvas,height=2,width=500,bg='white')
lineframe.place(x=250,y=65)

# var_x=0.31
var_x=0.50

# ==========================contact frame starts from here =============================

contactframe=Frame(canvas,height=300,width=600,relief='ridge',bd=3)
contactframe.propagate(False)
contactframe.place(relx=var_x,rely=0.50,anchor='center')

col=('name', 'phone', 'email', 'address')
datadip=ttk.Treeview(contactframe,columns=col,show='headings')
datadip.heading('name',text='Name')
datadip.heading('phone',text='Phone')
datadip.heading('email',text='Email')
datadip.heading('address',text='Address')


display_data_tree()

datadip.place(x=0,y=0,width=580,height=293)
scrollbar = ttk.Scrollbar(contactframe, orient="vertical", command=datadip.yview)
datadip.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT,fill=Y,pady=3)

var_x1=1.40
# var_x1=0.98



infoframe=Frame(canvas,height=300,width=350,relief='ridge',bd=3)
infoframe.propagate(False)
infoframe.place(relx=var_x1,rely=0.5,anchor='e')

# ==========================view_contact_frame starts from here =============================

view_contact_frame=Frame(infoframe)
view_contact_frame.propagate(False)



col=('name', 'phone')
contactdip=ttk.Treeview(view_contact_frame,columns=col,show='headings')
contactdip.heading('name',text='Name')
contactdip.heading('phone',text='Phone')

contactdip.column('name',width=200)
contactdip.column('phone',width=150)

view_contact_tree()

contactdip.place(x=0,y=0,width=330,height=293)
    
scrollbar1 = ttk.Scrollbar(view_contact_frame, orient="vertical", command=contactdip.yview)
contactdip.configure(yscroll=scrollbar1.set)
scrollbar1.pack(side=RIGHT,fill=Y,pady=3)

# ==========================search_contact_frame starts from here =============================

search_contact_frame=Frame(infoframe,bg='#fef9e7')
search_contact_frame.propagate(False)

srclabel=Label(search_contact_frame,text='Phone/Name:',font=('Calibri (Body)',12),fg='#4a235a',bg='#fef9e7')
srclabel.pack(side=LEFT,anchor='nw',padx=(30,0),pady=(60,0))

search=StringVar()
srcentry=ctk.CTkEntry(search_contact_frame,font=('Calibri (Body)',15),height=40,width=200,
                      border_color='#4a235a',textvariable=search)
srcentry.pack(side=RIGHT,anchor='ne',padx=(0,30),pady=(50,0))

srcbtn=ctk.CTkButton(search_contact_frame,text='Search',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#4a235a',command=lambda:search_data(search.get()))
srcbtn.place(relx=0.5,rely=0.5,anchor='center')

resetbtn=ctk.CTkButton(search_contact_frame,text='Reset',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#e74c3c',command=reset)
resetbtn.place(relx=0.5,rely=0.65,anchor='center')

# ==========================update_contact_frame starts from here =============================

update_contact_frame=Frame(infoframe,bg='#fef9e7')
update_contact_frame.propagate(False)

newbtn=ctk.CTkButton(update_contact_frame,text='Create New Contact',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#2ecc71',cursor='hand2',command=new_contact)
newbtn.place(relx=0.5,rely=0.4,anchor='center')

updatebtn=ctk.CTkButton(update_contact_frame,text='Update Existing Contact',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#e74c3c',cursor='hand2',command=update__contact)
updatebtn.place(relx=0.5,rely=0.6,anchor='center')


# >>>>>>>>>>>>>>>>>>>>>>>>>NEW CONTACT>>>>>>>>>>>>>>>>>>>>>>>>>>
new_contact_frame=Frame(infoframe,bg='#fef9e7')
new_contact_frame.propagate(False)

name=Label(new_contact_frame,text='Name:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')
name.place(x=5,y=40)
nameval=StringVar()
nameentry=ctk.CTkEntry(new_contact_frame,font=('Calibri (Body)',15),height=40,width=250,
                   border_color='#4a235a',textvariable=nameval)
nameentry.place(x=90,y=30)

phone=Label(new_contact_frame,text='Phone:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')
phone.place(x=5,y=90)

phoneval=StringVar()
phoneentry=ctk.CTkEntry(new_contact_frame,font=('Calibri (Body)',15),height=40,width=250,
                   border_color='#4a235a',textvariable=phoneval)
phoneentry.place(x=90,y=80)

email=Label(new_contact_frame,text='Email:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')
email.place(x=5,y=140)

emialval=StringVar()
emailentry=ctk.CTkEntry(new_contact_frame,font=('Calibri (Body)',15),height=40,width=250,
                   border_color='#4a235a',textvariable=emialval)
emailentry.place(x=90,y=130)

address=Label(new_contact_frame,text='Address:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')
address.place(x=5,y=190)

addressval=StringVar()
addressentry=ctk.CTkEntry(new_contact_frame,font=('Calibri (Body)',15),height=40,width=250,
                   border_color='#4a235a',textvariable=addressval)
addressentry.place(x=90,y=180)

savebtn=ctk.CTkButton(new_contact_frame,text='Save Contact',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#2ecc71',cursor='hand2',command=save_contact)
savebtn.place(relx=0.26,rely=0.84,anchor='center')

clearbtn=ctk.CTkButton(new_contact_frame,text='Clear Contact',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#e74c3c',cursor='hand2',command=clear_inputs)
clearbtn.place(relx=0.75,rely=0.84,anchor='center')


# >>>>>>>>>>>>>>>>>>>>>>>>>Update CONTACT>>>>>>>>>>>>>>>>>>>>>>>>>>

update__contact_frame=Frame(infoframe,bg='#fef9e7')
update__contact_frame.propagate(False)



namebtn=ctk.CTkButton(update__contact_frame,text='Name',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#28b463',cursor='hand2',command=lambda:change('name'))
namebtn.place(relx=0.5,rely=0.25,anchor='center')

phonebtn=ctk.CTkButton(update__contact_frame,text='Phone',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#979a9a',text_color='Black',cursor='hand2',command=lambda:change('phone'))
phonebtn.place(relx=0.5,rely=0.40,anchor='center')


emailbtn=ctk.CTkButton(update__contact_frame,text='Email',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#d4ac0d',text_color='Black',cursor='hand2',command=lambda:change('email'))
emailbtn.place(relx=0.5,rely=0.55,anchor='center')

addressbtn=ctk.CTkButton(update__contact_frame,text='Address',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#a93226',text_color='White',cursor='hand2',command=lambda:change('address'))
addressbtn.place(relx=0.5,rely=0.70,anchor='center')


# -----------------------------------------------------------------------
update__contact_frame_name=Frame(infoframe,bg='#fef9e7')
update__contact_frame_name.propagate(False)

updatename=Label(update__contact_frame_name,text='New Name:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

updatenameval=StringVar()
updatenameentry=ctk.CTkEntry(update__contact_frame_name,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=updatenameval)
refval1=StringVar()
refphone1=Label(update__contact_frame_name,text='Phone:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

refphoneent1=ctk.CTkEntry(update__contact_frame_name,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=refval1)

updatenamebtn=ctk.CTkButton(update__contact_frame_name,text='Update',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#28b463',cursor='hand2',command=lambda:final_update('name'))

updatename.place(relx=0.25,rely=0.20,anchor='center')
updatenameentry.place(relx=0.6,rely=0.20,anchor='center')
refphone1.place(relx=0.25,rely=0.40,anchor='center')
refphoneent1.place(relx=0.6,rely=0.40,anchor='center')
updatenamebtn.place(relx=0.5,rely=0.60,anchor='center')

# -----------------------------------------------------------------------
update__contact_frame_phone=Frame(infoframe,bg='#fef9e7')
update__contact_frame_phone.propagate(False)

updatephone=Label(update__contact_frame_phone,text='New Phone:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

updatephoneval=StringVar()
updatephoneentry=ctk.CTkEntry(update__contact_frame_phone,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=updatephoneval)

refval2=StringVar()
refphone2=Label(update__contact_frame_phone,text='Phone:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

refphoneent2=ctk.CTkEntry(update__contact_frame_phone,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=refval2)

updatephonebtn=ctk.CTkButton(update__contact_frame_phone,text='Update',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#28b463',cursor='hand2',command=lambda:final_update('phone'))

updatephone.place(relx=0.25,rely=0.20,anchor='center')
updatephoneentry.place(relx=0.6,rely=0.20,anchor='center')
refphone2.place(relx=0.25,rely=0.40,anchor='center')
refphoneent2.place(relx=0.6,rely=0.40,anchor='center')
updatephonebtn.place(relx=0.5,rely=0.60,anchor='center')

# -----------------------------------------------------------------------
update__contact_frame_email=Frame(infoframe,bg='#fef9e7')
update__contact_frame_email.propagate(False)

updateemail=Label(update__contact_frame_email,text='New Email:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

updateemailval=StringVar()
updateemailentry=ctk.CTkEntry(update__contact_frame_email,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=updateemailval)

refval3=StringVar()
refphone3=Label(update__contact_frame_email,text='Phone:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

refphoneent3=ctk.CTkEntry(update__contact_frame_email,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=refval3)

updateemailbtn=ctk.CTkButton(update__contact_frame_email,text='Update',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#28b463',cursor='hand2',command=lambda:final_update('email'))

updateemail.place(relx=0.25,rely=0.20,anchor='center')
updateemailentry.place(relx=0.6,rely=0.20,anchor='center')
refphone3.place(relx=0.25,rely=0.40,anchor='center')
refphoneent3.place(relx=0.6,rely=0.40,anchor='center')
updateemailbtn.place(relx=0.5,rely=0.60,anchor='center')

# -----------------------------------------------------------------------

update__contact_frame_address=Frame(infoframe,bg='#fef9e7')
update__contact_frame_address.propagate(False)

updateaddress=Label(update__contact_frame_address,text='New Address:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

updataddressval=StringVar()
updateaddressentry=ctk.CTkEntry(update__contact_frame_address,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=updataddressval)

refval4=StringVar()
refphone4=Label(update__contact_frame_address,text='Phone:',font=('Bahnschrift',12),fg='Black',bg='#fef9e7')

refphoneent4=ctk.CTkEntry(update__contact_frame_address,font=('Calibri (Body)',15),height=40,width=150,
                   border_color='#4a235a',textvariable=refval4)

updateaddressbtn=ctk.CTkButton(update__contact_frame_address,text='Update',font=('Calibri (Body)',13,'bold'),
                     height=30,corner_radius=20,fg_color='#28b463',cursor='hand2',command=lambda:final_update('address'))

updateaddress.place(relx=0.23,rely=0.20,anchor='center')
updateaddressentry.place(relx=0.6,rely=0.20,anchor='center')
refphone4.place(relx=0.25,rely=0.40,anchor='center')
refphoneent4.place(relx=0.6,rely=0.40,anchor='center')
updateaddressbtn.place(relx=0.5,rely=0.60,anchor='center')

# ==========================delete_contact_frame starts from here =============================

delete_contact_frame=Frame(infoframe,bg='#fef9e7')
delete_contact_frame.propagate(False)

dellabel=Label(delete_contact_frame,text='Phone:',font=('Calibri (Body)',12),fg='#4a235a',bg='#fef9e7')
dellabel.pack(side=LEFT,anchor='nw',padx=(30,0),pady=(60,0))

dell=StringVar()
delentry=ctk.CTkEntry(delete_contact_frame,font=('Calibri (Body)',15),height=40,width=200,
                   border_color='#4a235a',textvariable=dell)
delentry.pack(side=RIGHT,anchor='ne',padx=(0,30),pady=(50,0))

delbtn=ctk.CTkButton(delete_contact_frame,text='Delete',font=('Calibri (Body)',13,'bold'),
                  height=30,corner_radius=20,fg_color='#4a235a',command=lambda:delete_data(dell.get()))
delbtn.place(relx=0.5,rely=0.5,anchor='center')


# ==========================buttonsframe starts from here =============================


buttonsframe=Frame(canvas,height=70,width=640,bg='#1b2631',relief='ridge',bd='3')
buttonsframe.propagate(False)
buttonsframe.place(x=180,y=500)

vcbtn=ctk.CTkButton(buttonsframe,text='View Contact',font=('Calibri (Body)',12,'bold'),
                    corner_radius=20,fg_color='#28b463',text_color='White',command=lambda:[animation(),view_contact()])
vcbtn.pack(side=LEFT,padx=10)

scbtn=ctk.CTkButton(buttonsframe,text='Search Contact',font=('Calibri (Body)',12,'bold'),
                    corner_radius=20,fg_color='white',text_color='Black',command=lambda:[animation(),search_contact()])
scbtn.pack(side=LEFT,padx=10)

ucbtn=ctk.CTkButton(buttonsframe,text='Update Contact',font=('Calibri (Body)',12,'bold'),
                    corner_radius=20,fg_color='#d4ac0d',text_color='Black',command=lambda:[animation(),update_contact()])
ucbtn.pack(side=LEFT,padx=10)

dcbtn=ctk.CTkButton(buttonsframe,text='Delete Contact',font=('Calibri (Body)',12,'bold'),
                    corner_radius=20,fg_color='#a93226',text_color='White',command=lambda:[animation(),delete_contact()])
dcbtn.pack(side=LEFT,padx=10)

win.mainloop()