"""
Date: Started on 28.01.2022 [Thursday] {10:00 AM} - Completed on 20.03.2022 [Sunday] {01:37 AM}
Programmer: Prakash Kushwaha
Purpose: Creating a GUI program based on databases
"""


import mysql.connector
from tkinter import *
from tkinter import font as tkFont
import os


def btn_click_i(val):
    global name, roll_no, cls, section, s_id, gender, dob, phy, chem, maths, cs, eng, p_edu, O_id, O_phy, O_chem, O_maths, O_cs, O_eng, O_p_edu, host, user, passwd, database, table, output_i

    mydb = mysql.connector.connect(
        host=f"{host.get()}", user=f"{user.get()}", password=f"{passwd.get()}")
    mycursor = mydb.cursor()
    if val == "Create Database":
        mycursor.execute("Show databases")
        if (database.get(),) not in mycursor.fetchall():
            mycursor.execute(f"CREATE DATABASE {database.get()}")
            mycursor.execute(f"USE {database.get()}")
            output_i.set("Database Created Successfully!")
        else:
            mycursor.execute(f"USE {database.get()}")
            output_i.set("Database Selected Successfully!")

    elif val == "Create Table":
        mycursor.execute(f"USE {database.get()}")
        mycursor.execute("Show tables")
        tables = mycursor.fetchall()
        if (table.get(),) not in tables:
            mycursor.execute(
                f"Create table {table.get()}(Rollno varchar(5),Name varchar(30),Id varchar(30) Primary Key,Class varchar(2), Section char, Gender char, DOB date)")
            mydb.commit()
            output_i.set(f"Table '{table.get()}' Created Successfully!")
        if ("marks",) not in tables:
            mycursor.execute(
                "Create table marks (Id varchar(30) Primary Key,Physics int,Chemistry int,Maths int,CS int,English int,PEd int)")
            mydb.commit()
            output_i.set("Table 'Marks' Created Successfully!")
        elif (table.get(),) in tables and ("marks",) in tables:
            output_i.set("Both table already exists!!")

    elif val == "Insert":
        mycursor.execute(f"USE {database.get()}")
        mycursor.execute(
            f"Insert into {table.get()} values('{roll_no.get()}','{name.get()}','{s_id.get()}','{cls.get()}','{section.get()}','{gender.get()}','{dob.get()}')")

        mycursor.execute(
            f"Insert into Marks values('{s_id.get()}','{phy.get()}','{chem.get()}','{maths.get()}','{cs.get()}','{eng.get()}','{p_edu.get()}')")
        output_i.set("Data feeded succesfully!")

        mydb.commit()

    elif val == "Clear_Input":
        name.set("")
        roll_no.set("")
        cls.set("")
        section.set("")
        s_id.set("")
        gender.set("")
        dob.set("")

        phy.set("")
        chem.set("")
        maths.set("")
        cs.set("")
        eng.set("")
        p_edu.set("")
    mydb.close()


def btn_click_o(val):
    global name, roll_no, cls, section, s_id, gender, dob, phy, chem, maths, cs, eng, p_edu, O_s_id, O_phy, O_chem, O_maths, O_cs, O_eng, O_p_edu, host, user, passwd, database, table, O_output

    mydb = mysql.connector.connect(
        host=f"{host.get()}", user=f"{user.get()}", password=f"{passwd.get()}")
    mycursor = mydb.cursor()
    if val == "Search":
        mycursor.execute(f"Use {database.get()}")
        mycursor.execute(f"Select * from marks where Id = '{O_s_id.get()}'")
        data = mycursor.fetchall()
        for i in data:
            O_phy.set(i[1])
            O_chem.set(i[2])
            O_maths.set(i[3])
            O_cs.set(i[4])
            O_eng.set(i[5])
            O_p_edu.set(i[6])
        if data == []:
            O_output.set("No data found!")
        else:
            O_output.set("Data found!")
    elif val == "Clear":
        O_s_id.set("")
        O_phy.set("")
        O_chem.set("")
        O_maths.set("")
        O_cs.set("")
        O_eng.set("")
        O_p_edu.set("")
        O_output.set("")


def main():
    global name, roll_no, cls, section, s_id, gender, dob, phy, chem, maths, cs, eng, p_edu, bhv, com_skills, sports, punctual, sincerity
    global O_s_id, O_phy, O_chem, O_maths, O_cs, O_eng, O_p_edu, host, user, passwd, database, table, output_i, O_output
    root = Tk()
    # root.geometry("1600x750")
    root.title(f"DBMS - {os.getcwd()}")
    root.iconbitmap(r"E:\Programming_Data\VS_code\Python\Cs Project\Project DBMS\icon\icon.ico")

    # General Font Variable
    ubuntu = tkFont.Font(family='fira code', size=11)
    lfont = tkFont.Font(family="Century", size=13)

    """
    Variable for data input
    """
    # Variables to store student's data
    name = StringVar()
    roll_no = StringVar()
    cls = StringVar()
    section = StringVar()
    s_id = StringVar()
    gender = StringVar()
    dob = StringVar()

    # Variables to store academic data
    phy = IntVar()
    chem = IntVar()
    maths = IntVar()
    cs = IntVar()
    eng = IntVar()
    p_edu = IntVar()
    phy.set("")
    chem.set("")
    maths.set("")
    cs.set("")
    eng.set("")
    p_edu.set("")

    # Variables to store co-scholastic data
    # bhv = StringVar()
    # com_skills = StringVar()
    # sports = StringVar()
    # punctual = StringVar()
    # sincerity = StringVar()

    """
    Variables for data output
    """
    O_s_id = StringVar()
    O_phy = IntVar()
    O_chem = IntVar()
    O_maths = IntVar()
    O_cs = IntVar()
    O_eng = IntVar()
    O_p_edu = IntVar()
    O_phy.set("")
    O_chem.set("")
    O_maths.set("")
    O_cs.set("")
    O_eng.set("")
    O_p_edu.set("")

    # Behaviour
    # O_bhv = StringVar()
    # O_com_skills = StringVar()
    # O_sports = StringVar()
    # O_punctual = StringVar()
    # O_sincerity = StringVar()

    # Variables for sql connection
    host = StringVar()
    user = StringVar()
    passwd = StringVar()
    database = StringVar()
    table = StringVar()
    output_i = StringVar()
    O_output = StringVar()

    f1 = Frame(root, pady=10)
    f1.grid(row=0, column=2)

    title = Label(f1, text="Student's Record DBMS", fg="white",
                  bg="black", font="Helvetica 30 bold", bd=14, relief=RIDGE)
    title.grid(row=0, column=1, ipadx=20, ipady=5)
    my_canvas = Canvas(f1, width=455, height=20)
    my_canvas.grid(row=1, column=1)

    my_canvas.create_line(100, 10, 365, 10, fill="slateblue1", width=4)

    f2 = Frame(root, bd=8, relief=RAISED, bg="cornflower blue")
    f2.grid(row=2, column=1, padx=10, ipadx=10, ipady=10)

    Label(f2, text="Name : ", font=lfont,
          bg="cornflower blue").grid(row=0, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=name)
    input1.grid(row=0, column=2, pady=3)

    Label(f2, text="Roll Number : ", font=lfont,
          bg="cornflower blue").grid(row=1, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=roll_no)
    input1.grid(row=1, column=2, pady=3)

    Label(f2, text="Class : ", font=lfont,
          bg="cornflower blue").grid(row=2, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=cls)
    input1.grid(row=2, column=2, pady=3)

    Label(f2, text="Section: ", font=lfont,
          bg="cornflower blue").grid(row=3, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=section)
    input1.grid(row=3, column=2, pady=3)

    Label(f2, text="ID : ", font=lfont,
          bg="cornflower blue").grid(row=4, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=s_id)
    input1.grid(row=4, column=2, pady=3)

    Label(f2, text="Gender : ", font=lfont,
          bg="cornflower blue").grid(row=5, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=gender)
    input1.grid(row=5, column=2, pady=3)

    Label(f2, text="D.O.B. : ", font=lfont,
          bg="cornflower blue").grid(row=6, column=1)
    input1 = Entry(f2, font=ubuntu, textvariable=dob)
    input1.grid(row=6, column=2, pady=3)

    f3 = Frame(root, bd=8, relief=RAISED, bg="gainsboro")
    f3.grid(row=2, column=2, ipadx=10, ipady=10)

    title = Label(f3, text="Academic", font="Stix 16 bold",
                  fg="white", bg="Slate blue2", bd=6, relief=GROOVE)
    title.grid(row=0, column=2, pady=10, ipadx=40, ipady=5)

    Label(f3, text="Physics : ", font=lfont,
          bg="gainsboro").grid(row=1, column=1)
    input1 = Entry(f3, font=ubuntu, textvariable=phy)
    input1.grid(row=1, column=2, pady=3)

    Label(f3, text="Chemistry : ", font=lfont,
          bg="gainsboro").grid(row=2, column=1)
    input1 = Entry(f3, font=ubuntu, textvariable=chem)
    input1.grid(row=2, column=2, pady=3)

    Label(f3, text="Maths : ", font=lfont,
          bg="gainsboro").grid(row=3, column=1)
    input1 = Entry(f3, font=ubuntu, textvariable=maths)
    input1.grid(row=3, column=2, pady=3)

    Label(f3, text="Computer Science : ", font=lfont,
          bg="gainsboro").grid(row=4, column=1)
    input1 = Entry(f3, font=ubuntu, textvariable=cs)
    input1.grid(row=4, column=2, pady=3)

    Label(f3, text="English : ", font=lfont,
          bg="gainsboro").grid(row=5, column=1)
    input1 = Entry(f3, font=ubuntu, textvariable=eng)
    input1.grid(row=5, column=2, pady=3)

    Label(f3, text="Physical Education : ", font=lfont,
          bg="gainsboro").grid(row=6, column=1)
    input1 = Entry(f3, font=ubuntu, textvariable=p_edu)
    input1.grid(row=6, column=2, pady=3)

    # f4 = Frame(root, bd=8, relief=RAISED)
    # f4.grid(row=2, column=3, ipadx=10, ipady=10)

    # title = Label(f4, text="Co-Scholastic", font="Stix 16 bold",
    #               fg="white", bg="slateblue", bd=6, relief=GROOVE)
    # title.grid(row=0, column=2, pady=10, ipadx=20)

    # Label(f4, text="Behavior : ", font=lfont).grid(row=1, column=1)
    # input1 = Entry(f4, font=ubuntu, textvariable=bhv)
    # input1.grid(row=1, column=2, pady=3)

    # Label(f4, text="Communication Skills : ", font=lfont).grid(row=2, column=1)
    # input1 = Entry(f4, font=ubuntu, textvariable=com_skills)
    # input1.grid(row=2, column=2, pady=3)

    # Label(f4, text="Sports : ", font=lfont).grid(row=3, column=1)
    # input1 = Entry(f4, font=ubuntu, textvariable=sports)
    # input1.grid(row=3, column=2, pady=3)

    # Label(f4, text="Punctual : ", font=lfont).grid(row=4, column=1)
    # input1 = Entry(f4, font=ubuntu, textvariable=punctual)
    # input1.grid(row=4, column=2, pady=3)

    # Label(f4, text="Sincerity : ", font=lfont).grid(row=5, column=1)
    # input1 = Entry(f4, font=ubuntu, textvariable=sincerity)
    # input1.grid(row=5, column=2, pady=3)

    f5 = Frame(root)
    f5.grid(row=6, column=2)
    Button(f5, text="Commit", font="arial 16", bg="green", width="6",
           command=lambda: btn_click_i("Insert"), relief=GROOVE, bd=8).grid(row=2, column=1, padx=4, ipadx=10)
    Button(f5, text="Clear", font="arial 16", bg="pale violet red", width="6",
           command=lambda: btn_click_i("Clear_Input"), relief=GROOVE, bd=8).grid(row=2, column=2, padx=4, ipadx=10)

    f6 = Frame(root)
    f6.grid(row=7, column=2)

    my_canvas2 = Canvas(f6, width=455, height=20)
    my_canvas2.grid(row=0, column=1, ipady=4)

    my_canvas2.create_line(100, 10, 365, 10, fill="black", width=1, dash=(
        4, 4), capstyle=ROUND, smooth=TRUE, splinesteps=36)

    f7 = Frame(root)
    f7.grid(row=8, column=2)
    title = Label(f7, text="Search Records", font="Arial 22 bold",
                  fg="white", bg="dodger blue", bd=12, relief=RIDGE)
    title.grid(row=2, column=1, pady=10, ipadx=60, ipady=5)

    # f8 = Frame(root)
    # f8.grid(row=9, column=2)

    # my_canvas2 = Canvas(f8, width=455, height=20)
    # my_canvas2.grid(row=0, column=1, ipady=4)

    # my_canvas2.create_line(100, 10, 365, 10, fill="black", width=1, dash=(
    #     4, 4), capstyle=ROUND, smooth=TRUE, splinesteps=36)

    f9 = Frame(root, bd=8, relief=RAISED, bg="LightSteelBlue2")
    f9.grid(row=10, column=1, padx=10, ipadx=10, ipady=10)
    text = Label(f9, text="Fetch Records via ID",
                 font="Arial 14 bold", fg="white", bg="Purple", bd=6, relief=GROOVE)
    text.grid(row=0, column=2, pady=5, ipadx=4, ipady=2)
    Label(f9, text="ID : ", font=lfont,
          bg="LightSteelBlue2").grid(row=4, column=1)
    input1 = Entry(f9, font=ubuntu, textvariable=O_s_id)
    input1.grid(row=4, column=2)

    f10 = Frame(root, bd=8, relief=RAISED, bg="PeachPuff3")
    f10.grid(row=10, column=2, ipadx=10, ipady=10)
    Label(f10, text="Chemistry: ", font=lfont,
          bg="PeachPuff3").grid(row=0, column=1, pady=5)
    input1 = Entry(f10, font=ubuntu, textvariable=O_phy, state=DISABLED)
    input1.config(disabledforeground="black")
    input1.grid(row=0, column=2, pady=3)

    Label(f10, text="Physics : ", font=lfont,
          bg="PeachPuff3").grid(row=1, column=1)
    input1 = Entry(f10, font=ubuntu, textvariable=O_chem, state=DISABLED)
    input1.config(disabledforeground="black")
    input1.grid(row=1, column=2, pady=3)

    Label(f10, text="Maths: ", font=lfont,
          bg="PeachPuff3").grid(row=2, column=1)
    input1 = Entry(f10, font=ubuntu, textvariable=O_maths, state=DISABLED)
    input1.config(disabledforeground="black")
    input1.grid(row=2, column=2, pady=3)

    Label(f10, text="Computer Science: ", font=lfont,
          bg="PeachPuff3").grid(row=3, column=1)
    input1 = Entry(f10, font=ubuntu, textvariable=O_cs, state=DISABLED)
    input1.config(disabledforeground="black")
    input1.grid(row=3, column=2, pady=3)

    Label(f10, text="English: ", font=lfont,
          bg="PeachPuff3").grid(row=4, column=1)
    input1 = Entry(f10, font=ubuntu, textvariable=O_eng, state=DISABLED)
    input1.config(disabledforeground="black")
    input1.grid(row=4, column=2, pady=3)

    Label(f10, text="Physical Education: ", font=lfont,
          bg="PeachPuff3").grid(row=5, column=1)
    input1 = Entry(f10, font=ubuntu, textvariable=O_p_edu, state=DISABLED)
    input1.config(disabledforeground="black")
    input1.grid(row=5, column=2, pady=3)

    # f11 = Frame(root, bd=8, relief=RAISED)
    # f11.grid(row=10, column=3, ipadx=10, ipady=10)

    # Label(f11, text="Behavior : ", font=lfont).grid(row=1, column=1)
    # input1.config(disabledforeground="black")
    # input1 = Entry(f11, font=ubuntu, textvariable=O_bhv, state=DISABLED)
    # input1.grid(row=1, column=2, pady=3)

    # Label(f11, text="Communication Skills : ",
    #       font=lfont).grid(row=2, column=1)
    # input1.config(disabledforeground="black")
    # input1 = Entry(f11, font=ubuntu, textvariable=O_com_skills, state=DISABLED)
    # input1.grid(row=2, column=2, pady=3)

    # Label(f11, text="Sports : ", font=lfont).grid(row=3, column=1)
    # input1.config(disabledforeground="black")
    # input1 = Entry(f11, font=ubuntu, textvariable=O_sports, state=DISABLED)
    # input1.grid(row=3, column=2, pady=3)

    # Label(f11, text="Punctual : ", font=lfont).grid(row=4, column=1)
    # input1.config(disabledforeground="black")
    # input1 = Entry(f11, font=ubuntu, textvariable=O_punctual, state=DISABLED)
    # input1.grid(row=4, column=2, pady=3)

    # Label(f11, text="Sincerity : ", font=lfont).grid(row=5, column=1)
    # input1 = Entry(f11, font=ubuntu, textvariable=O_sincerity, state=DISABLED)
    # input1.config(disabledforeground="black")
    # input1.grid(row=5, column=2, pady=3)

    f12 = Frame(root)
    f12.grid(row=12, column=2, pady=10)
    Button(f12, text="Search", font="arial 16", bg="green", width="8",
           command=lambda: btn_click_o("Search"), relief=GROOVE, bd=8).grid(row=2, column=1, padx=4, ipadx=10)
    Button(f12, text="Clear", font="arial 16", bg="pale violet red", width="8",
           command=lambda: btn_click_o("Clear"), relief=GROOVE, bd=8).grid(row=2, column=2, padx=4, ipadx=10)

    f13 = Frame(root, bd=8, relief=RAISED, padx=10, bg="snow4")
    f13.grid(row=10, column=3, padx=10, ipadx=4, ipady=4)

    Label(f13, text="OUTPUT : ", font=lfont,
          bg="snow4").grid(row=8, column=1)
    input1 = Entry(f13, font=ubuntu, textvariable=O_output,
                   state=DISABLED, insertwidth=1, bd=15)
    input1.config(disabledforeground="black")
    input1.grid(row=8, column=2, pady=15, ipadx=50, ipady=20)

    f14 = Frame(root, bd=8, relief=RAISED, padx=10, bg="seashell3")
    f14.grid(row=2, column=3, padx=10, ipadx=4, ipady=4)

    Label(f14, text="SQL Connection", font="Arial 14 bold", fg="white", bg="Dodger Blue2",
          bd=6, relief=GROOVE).grid(row=0, column=2, padx=10, pady=5, ipadx=10, ipady=4)

    Label(f14, text="Host : ", font=lfont,
          bg="seashell3").grid(row=1, column=1)
    input1 = Entry(f14, font=ubuntu, textvariable=host)
    input1.grid(row=1, column=2, pady=3)
    Label(f14, text="User : ", font=lfont,
          bg="seashell3").grid(row=2, column=1)
    input1 = Entry(f14, font=ubuntu, textvariable=user)
    input1.grid(row=2, column=2, pady=3)
    Label(f14, text="Password : ", font=lfont,
          bg="seashell3").grid(row=3, column=1)
    input1 = Entry(f14, font=ubuntu, textvariable=passwd)
    input1.grid(row=3, column=2, pady=3)

    Label(f14, text="Database name : ", font=lfont,
          bg="seashell3").grid(row=4, column=1)
    input1 = Entry(f14, font=ubuntu, textvariable=database)
    input1.grid(row=4, column=2, pady=3)

    Label(f14, text="Table name : ", font=lfont,
          bg="seashell3").grid(row=5, column=1)
    input1 = Entry(f14, font=ubuntu, textvariable=table)
    input1.grid(row=5, column=2, pady=3)

    Button(f14, text="Create Database", font="arial 13 bold", width="12",
           command=lambda: btn_click_i("Create Database"), relief=GROOVE, bd=6).grid(row=6, column=1, pady=10, padx=4, ipadx=10)
    Button(f14, text="Create Table", font="arial 13 bold", width="12",
           command=lambda: btn_click_i("Create Table"), relief=GROOVE, bd=6).grid(row=6, column=2, pady=10, padx=4, ipadx=10)

    f15 = Frame(root, bd=8, relief=RAISED, padx=10, bg="sky blue3")
    f15.grid(row=6, column=3, padx=10, pady=10, ipadx=4, ipady=4)

    Label(f15, text="OUTPUT : ", font=lfont,
          bg="sky blue3").grid(row=8, column=1)
    input1 = Entry(f15, font=ubuntu, textvariable=output_i,
                   state=DISABLED, insertwidth=1, bd=15)
    input1.config(disabledforeground="black")
    input1.grid(row=8, column=2, pady=15, ipadx=60, ipady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
