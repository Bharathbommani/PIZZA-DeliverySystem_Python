from tkinter import *
import sqlite3

db=sqlite3.connect("pizza.sqlite3")
def varr():
    cursor =db.cursor()
    cursor.execute("SELECT * FROM pizza")
    for order_Id,status,Name,mobile,Address,Email,Type in cursor:
        vf=order_Id
    return vf+1;
a=Tk()
a.title("CUSTOMER")
a.geometry('1380x1400')
C = Canvas(a, bg="blue", height=1000, width=1000)
filename = PhotoImage(file = "p2.png")
background_label = Label(a, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
def pizza():
    p=Tk()
    p.title("Order Pizza")
    p.geometry('1570x1400')
    l=Label(p,text="Name\n\nAddress\n\nPizza Type\n\nMobile no\n\nEmail id",font=20)
    l.pack()
    l.place(x=200,y=300)
    e=Entry(p)
    e.pack()
    e.place(x=300,y=300)
    e1=Entry(p)
    e1.pack()
    e1.place(x=300,y=350)
    e2=Entry(p)
    e2.pack()
    e2.place(x=300,y=445)
    e3=Entry(p)
    e3.pack()
    e3.place(x=300,y=485)
    var = IntVar()
    var.set(1)##
    R1 = Radiobutton(p, text="Small(95 rs)", variable=var, value=0,font=20)
    R1.pack()
    R1.place(x=300,y=385)
    R2 = Radiobutton(p, text="Medium(195 rs)", variable=var, value=1,font=20)
    R2.pack()
    R2.place(x=450,y=385)
    R3 = Radiobutton(p, text="Large(295 rs)", variable=var, value=2,font=20)
    R3.pack()
    R3.place(x=600,y=385)
    def yu():
        if  e.get() and e1.get() and e2.get() and e3.get():
            a=varr()
            db.execute("INSERT INTO pizza VALUES({},'Pending','{}','{}','{}','{}',{})".format(a,e.get(),e2.get(),e1.get(),e3.get(),var.get()))
            db.commit()
            las=Label(p,text="Ordered sucessfully \n Order Id="+str(a))
            las.pack()
    b7=Button(p,text="submit",font=20,command=yu)
    b7.pack()
    b7.place(x=450,y=500)
b=Button(a,text="Order Pizza",font=20,bg="sky blue",command=pizza)
b.pack()
b.place(x=400,y=550)
def cancel():
    c=Tk()
    c.title("Cancel Order")
    c.geometry('1470x1300')
    l1=Label(c,text="Name\n\nOrder Id",font=20)
    l1.pack()
    l1.place(x=200,y=300)
    e4=Entry(c)
    e4.pack()
    e4.place(x=300,y=300)
    e5=Entry(c)
    e5.pack()
    e5.place(x=300,y=340)
    def can():
        cursor =db.cursor()
        cursor.execute("SELECT * FROM pizza")
        for order_Id,status,Name,mobile,Address,Email,Type in cursor:
            
            
            if order_Id==int(e5.get()):
                if Name==e4.get():
                    update_sql="UPDATE pizza SET status='Cancelled' WHERE order_Id={}".format(e5.get())
                    update_cursor=db.cursor()
                    update_cursor.execute(update_sql)
                    update_cursor.connection.commit()
                    update_cursor.close()
                    lk=Label(c,text="order cancelled Id="+e5.get())
                    lk.pack()
                    break
                
    b7=Button(c,text="submit",font=20,command=can)
    b7.pack()
    b7.place(x=300,y=400)
b1=Button(a,text="Cancel Order",font=40,bg="sky blue",command=cancel)
b1.pack()
b1.place(x=570,y=550)
def track():
    t=Tk()
    t.title("Track Order")
    t.geometry('1470x1300')
    l2=Label(t,text="Order Id",font=20)
    l2.pack()
    l2.place(x=200,y=300)
    e6=Entry(t)
    e6.pack()
    e6.place(x=300,y=300)
    def ta():
        cursor =db.cursor()
        cursor.execute("SELECT * FROM pizza")
        for order_Id,status,Name,mobile,Address,Email,Type in cursor:
            if order_Id==int(e6.get()):
                lk=Label(t,text="order status="+status)
                lk.pack()
                break
    b8=Button(t,text="submit",font=40,command=ta)
    b8.pack()
    b8.place(x=300,y=350)
b2=Button(a,text="Track Order",font=40,bg="sky blue",command=track)
b2.pack()
b2.place(x=750,y=550)
def vendor():
    v=Tk()
    v.title("Vendor")
    v.geometry('1470x1300')
    def dl():
        d=Tk()
        d.title("Delivered")
        d.geometry('1470x1300')
        l21=Label(d,text="Order Id",font=40)
        l21.pack()
        l21.place(x=200,y=300)
        e16=Entry(d)
        e16.pack()
        e16.place(x=300,y=300)
        def taa():
            cursor =db.cursor()
            cursor.execute("SELECT * FROM pizza")
            for order_Id,status,Name,mobile,Address,Email,Type in cursor:
                if order_Id==int(e16.get()):
                    update_sql="UPDATE pizza SET status='Served' WHERE order_Id={}".format(e16.get())
                    update_cursor=db.cursor()
                    update_cursor.execute(update_sql)
                    update_cursor.connection.commit()
                    update_cursor.close()
                    lk1=Label(d,text="order delivered Id="+e16.get())
                    lk1.pack()
                    break
        b81=Button(d,text="submit",font=20,command=taa)
        b81.pack()
        b81.place(x=300,y=350)
    b21=Button(v,text="Delivered Order",font=20,bg="sky blue",command=dl)
    b21.pack()
    b21.place(x=700,y=200)
    def ca():
        ca=Tk()
        ca.title("Cancelled Order")
        ca.geometry('1470x1300')
        cursor =db.cursor()
        cursor.execute("SELECT * FROM pizza")
        for order_Id,status,Name,mobile,Address,Email,Type in cursor:
            if status=="Cancelled" :
                lc1=Label(ca,text="Order_Id="+str(order_Id),font=50)
                lc1.pack()
    b22=Button(v,text="Cancelled Order",font=20,bg="sky blue",command=ca)
    b22.pack()
    b22.place(x=400,y=200)
    def se():
        se=Tk()
        se.title("Served Order")
        se.geometry('1470x1300')
        cursor =db.cursor()
        cursor.execute("SELECT * FROM pizza")
        for order_Id,status,Name,mobile,Address,Email,Type in cursor:
            if status=="Served" :
                lc2=Label(se,text="Order_Id="+str(order_Id),font=20)
                lc2.pack()
    b23=Button(v,text="Served Order",font=50,bg="sky blue",command=se)
    b23.pack()
    b23.place(x=400,y=400)
    def pe():
        pe=Tk()
        pe.title("Pending Order")
        pe.geometry('1470x1300')
        cursor =db.cursor()
        cursor.execute("SELECT * FROM pizza")
        for order_Id,status,Name,mobile,Address,Email,Type in cursor:
            if status=="Pending" :
                lc3=Label(pe,text="Order_Id="+str(order_Id),font=20)
                lc3.pack()
    b24=Button(v,text="Pending Order",font=50,bg="sky blue",command=pe)
    b24.pack()
    b24.place(x=700,y=400)
b12=Button(a,text="Vendor",font=20,bg="sky blue",command=vendor)
b12.pack()
b12.place(x=900,y=550)

