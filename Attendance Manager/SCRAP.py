import mysql.connector
from tkinter import messagebox
import csv
import sys

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
mycursor = mydb.cursor()



































"""
mycursor.execute("CREATE table Student_Data (Roll_No INT PRIMARY KEY, PRN_Number INT, Name VARCHAR(255), AM4 TINYINT, AM4_Tutorial TINYINT, AOA TINYINT, AOA_Practical TINYINT, CG TINYINT, CG_Practical TINYINT, OS TINYINT, OS_Practical TINYINT, COA TINYINT, COA_Practical TINYINT, OSTL TINYINT, OSTL_Practical TINYINT)")
#mycursor.execute("INSERT INTO student_data (PRN_Number, Name, AM4, AOA, CG, COA, OS, OSTL, AM4_Tutorial, AOA_Practical, CG_Practical, COA_Practical, OS_Practical, OSTL_Practical) VALUES (171041051, 'Aditya Abasaheb Zagade', 11, 6, 8, 11, 9, 8, 0, 6, 3, 1, 3, 4);")
#sql = "INSERT INTO student_data (PRN_Number, Name, AM4, AOA, CG, COA, OS, OSTL, AM4_Tutorial, AOA_Practical, CG_Practical, COA_Practical, OS_Practical, OSTL_Practical) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#values = (171041051, 'Siddhesh Dattatray Shinde', 11, 6, 8, 11, 9, 8, 0, 6, 3, 1, 3, 4)
#mycursor.execute(sql, values)
mydb.commit()
"""
"""
INSERT INTO `adi`.`student_data` (`PRN_Number`, `Name`, `AM4`, `AOA`, `CG`, `COA`, `OS`, `OSTL`, `AM4_Tutorial`, `AOA_Practical`, `CG_Practical`, `COA_Practical`, `OS_Practical`, `OSTL_Practical`) VALUES ('171041050', 'Adi', '11', '6', '8', '11', '9', '8', '0', '6', '3', '1', '3', '4')
mysql command
"""
"""
prn = 171041050
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="adi")
mycursor = mydb.cursor()
mycursor.execute("Select PRN_Number from attendance WHERE PRN_Number = prn")
details = mycursor.fetchall()
for i in details:
    print(i)
"""
""" prn=IntVar()
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
    ostll=IntVar()"""
"""
import tkinter as tk
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))
root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')
canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>', on_configure)
frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')
l = tk.Label(frame, text="Hello", font="-size 50")
l.pack()
l = tk.Label(frame, text="World", font="-size 50")
l.pack()
l = tk.Label(frame, text="Test text 1\nTest text 2\nTest text 3\nTest text 4\nTest text 5\nTest text 6\nTest text 7\nTest text 8\nTest text 9", font="-size 20")
l.pack()
root.mainloop()
"""
"""
from tkinter import *
top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20, cursor=arrow)
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack()
C2.pack()
top.mainloop()
"""
# mycursor.execute("SELECT* FROM attendance INTO OUTFILE 'F:/Mini_Project-master/Mini_Project/Using Classes/attendance.csv' FIELDS ENCLOSED BY '@' TERMINATED BY ';' ESCAPED BY '&' LINES TERMINATED BY '\r\n';")
# mycursor.execute("LOAD DATA LOCAL INFILE 'F:/Mini_Project-master/Mini_Project/Using Classes/attendance.txt' INTO table attendance")
# mycursor.execute("SELECT * INTO OUTFILE 'F:/Mini_Project-master/Mini_Project/Using Classes/attendance.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '@' LINES TERMINATED BY '\n' FROM adi.attendance;")
"""
mycursor.execute("SELECT * FROM attendance")
result = mycursor.fetchall()
mycursor.execute("DESCRIBE attendance")
column = mycursor.fetchall()
columns = []
for i in range(len(column)):
	columns.append(column[i][0])
print("Columns",columns)
c = csv.writer(open('F:/Mini_Project-master/Mini_Project/Using Classes/adi2.csv', 'w', newline=""), lineterminator="")
for i in columns:
	c.writerow([i])
c.writerow("\n")
c = csv.writer(open('F:/Mini_Project-master/Mini_Project/Using Classes/adi2.csv', 'a', newline=""), lineterminator="\n")
for x in result:
    c.writerow(x)
"""
"""
from tkinter import *


class LabeledEntry(Entry):
	def __init__(self, master=None, label="", **kwargs):
		Entry.__init__(self, master, **kwargs)
		self.label = label
		self.on_exit()
		self.bind('<FocusIn>', self.on_entry)
		self.bind('<FocusOut>', self.on_exit)

	def on_entry(self, event=None):
		if self.get() == self.label:
			self.delete(0, END)

	def on_exit(self, event=None):
		if not self.get():
			self.insert(0, self.label)


def start():
	print(adi.get())


root = Tk()
e = Entry(root)
e.insert(END, 'default text')
e.pack()
adi = IntVar()
adi.set('')
a=LabeledEntry(root, label='adi', textvariable=adi).pack()
Button(root, text='Submit', command=start).pack()

root.geometry("400x400+550+200")
root.mainloop()
"""