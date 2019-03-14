from tkinter import *
from tkinter.font import Font
import mysql.connector

root = Tk()
frame = Frame(root)
AddStudentFrame=Frame(root)

prn=IntVar()
name=StringVar()
m4=IntVar()
m4t=IntVar()
aoa=IntVar()
aoal=IntVar()
cg=IntVar()
cgl=IntVar()
os=IntVar()
osl=IntVar()
coa=IntVar()
coal=IntVar()
ostl=IntVar()
ostll=IntVar()

def FetchStudentData():
    a= prn.get()
    b=name.get()
    c=m4.get()
    d=m4t.get()
    e=aoa.get()
    f=aoal.get()
    g=cg.get()
    h=cgl.get()
    i=os.get()
    j=osl.get()
    k=coa.get()
    l=coal.get()
    m=ostl.get()
    n=ostll.get()
    values=[]
    values.append(a)
    values.append(b)
    values.append(c)
    values.append(d)
    values.append(e)
    values.append(f)
    values.append(g)
    values.append(h)
    values.append(i)
    values.append(j)
    values.append(k)
    values.append(l)
    values.append(m)
    values.append(n)

    mysqlvalues=tuple(values)
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
    mycursor=mydb.cursor()
    sql="INSERT INTO attendance (PRN_Number, Name, Am4, AM4_Tutorial, AOA, AOA_Practical, CG, CG_Practical, OS, OS_Practical, COA, COA_Practical, OSTL, OSTL_Practical) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, mysqlvalues)
    mydb.commit()
    print("Student added successfully : ", mysqlvalues)




def AddStudent():
    frame.destroy()
    """
    prn=IntVar()
    name=StringVar()
    m4=IntVar()
    m4t=IntVar()
    aoa=IntVar()
    aoal=IntVar()
    cg=IntVar()
    cgl=IntVar()
    os=IntVar()
    osl=IntVar()
    coa=IntVar()
    coal=IntVar()
    ostl=IntVar()
    ostll=IntVar()
    """
    label=Label(AddStudentFrame, text="Enter student details", font=Font(size=12)).grid(row=0, column=1)
    prn_label=Label(AddStudentFrame, text="PRN").grid(row=1, column=0, stick=W)
    name_label=Label(AddStudentFrame, text="Name").grid(row=2, column=0, stick=W)
    note_label=Label(AddStudentFrame, text="Enter Previous attendance if any", font=Font(size=12)).grid(row=3, column=1)
    m4_label=Label(AddStudentFrame, text="AM4").grid(row=4, column=0, stick=W)
    m4t_label=Label(AddStudentFrame, text="AM4 Tutorial").grid(row=5, column=0, stick=W)
    aoa_label=Label(AddStudentFrame, text="AOA").grid(row=6, column=0, stick=W)
    aoal_label=Label(AddStudentFrame, text="AOA Lab").grid(row=7, column=0, stick=W)
    cg_label=Label(AddStudentFrame, text="CG").grid(row=8, column=0, stick=W)
    cgl_label=Label(AddStudentFrame, text="CG LAb").grid(row=9, column=0, stick=W)
    os_label=Label(AddStudentFrame, text="OS").grid(row=10, column=0, stick=W)
    osl_label=Label(AddStudentFrame, text="OS Lab").grid(row=11, column=0, stick=W)
    coa_label=Label(AddStudentFrame, text="COA").grid(row=12, column=0, stick=W)
    coal_label=Label(AddStudentFrame, text="COA Lab").grid(row=13, column=0, stick=W)
    ostl_label=Label(AddStudentFrame, text="OSTL Theory").grid(row=14, column=0, stick=W)
    osltll_label=Label(AddStudentFrame, text="OSTL").grid(row=15, column=0, stick=W)

    prn_entry=Entry(AddStudentFrame, width=20, textvariable=prn).grid(row=1, column=1)
    name_entry=Entry(AddStudentFrame, width=20, textvariable=name).grid(row=2, column=1)
    m4_entry=Entry(AddStudentFrame, width=20, textvariable=m4).grid(row=4, column=1)
    m4l_entry=Entry(AddStudentFrame, width=20, textvariable=m4t).grid(row=5, column=1)
    aoa_entry=Entry(AddStudentFrame, width=20, textvariable=aoa).grid(row=6, column=1)
    aoal_entry = Entry(AddStudentFrame, width=20, textvariable=aoal).grid(row=7, column=1)
    cg_entry = Entry(AddStudentFrame, width=20, textvariable=cg).grid(row=8, column=1)
    cgl_entry = Entry(AddStudentFrame, width=20, textvariable=cgl).grid(row=9, column=1)
    os_entry = Entry(AddStudentFrame, width=20, textvariable=os).grid(row=10, column=1)
    osl_entry = Entry(AddStudentFrame, width=20, textvariable=osl).grid(row=11, column=1)
    coa_entry = Entry(AddStudentFrame, width=20, textvariable=coa).grid(row=12, column=1)
    coal_entry = Entry(AddStudentFrame, width=20, textvariable=coal).grid(row=13, column=1)
    ostl_entry = Entry(AddStudentFrame, width=20, textvariable=ostl).grid(row=14, column=1)
    ostll_entry = Entry(AddStudentFrame, width=20, textvariable=ostll).grid(row=15, column=1)

    Submit_Button=Button(AddStudentFrame, text="Save", font=Font(size=12), padx=10, pady=2, bg="BLUE", fg="WHITE", command=FetchStudentData)
    Submit_Button.grid(row=18, column=1)
    AddStudentFrame.pack()




def Start(root):
    fontchange = Font(family="Courier", size=12)
    add = Button(frame, font=fontchange, text="Add Student", relief=RAISED, padx=10, pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1, command=AddStudent).pack()
    mark = Button(frame, font=fontchange, text="Mark Attendance", relief=RAISED, padx=10, pady=3, bg="YELLOW",fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1).pack()
    check = Button(frame, font=fontchange, text="Check attendace of paticular student", relief=RAISED, padx=10,pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1).pack()
    check_class = Button(frame, font=fontchange, text="Mark Attendance of whole class", relief=RAISED, padx=10,pady=3, bg="YELLOW", fg="RED", bd=2, activebackground="BLUE", activeforeground="WHITE", height=1).pack()
    frame.pack(side=TOP, fill="both", expand=True)




Start(root)
#root.geometry("1280x650+35+25")
root.mainloop()