from tkinter import *
import pymysql
from tkinter import ttk
class NHStudentsData:
    def __init__(self,root):
        self.root = root
        self.root.title('NH')
        self.root.geometry('1400x700')
        title = Label(self.root,
                      text='NH Public School',
                      bd=4,
                      relief=GROOVE,bg='green',fg='white',font=("Comic Sana MS",20,'bold'))
        title.pack(fill=X,side=TOP)


        self.roll_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.course_var = StringVar()
        self.fee_var = StringVar()
        self.contact_var = StringVar()
        self.trainer_var = StringVar()
        self.emailid_var = StringVar()
        self.start_date_var = StringVar()
        self.gender_var = StringVar()

        self.searchby = StringVar()
        self.searchtxt = StringVar()






#================ DataEntryFrame =============================================

        DataEntryFrame = Frame(self.root,bg='green',bd=5,relief=GROOVE)
        DataEntryFrame.place(x=10,y=50,width=400,height=600)

        title = Label(DataEntryFrame,text='NH Public School Data',bg='green',fg='white',font=('times new roman',20,'bold'))
        title.grid(row=0,columnspan=2,padx=50,pady=10)


#  ID, FirstName,LastName,Course_Nmae,Fee,Contact,Trainer,Start_Date,Gender
#================ ID ============================================

        lbl_roll_no = Label(DataEntryFrame,text='ROLL NO:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_roll_no.grid(row=1,column=0,sticky='W')

        txt_roll_no = Entry(DataEntryFrame,textvariable=self.roll_no_var,font=('times new roman',15,'bold'))
        txt_roll_no.grid(row=1,column=1,pady=10)

#================== FirstName =========================================

        lbl_firstname = Label(DataEntryFrame,text='FIRST NAME:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_firstname.grid(row=2,column=0,sticky='w')

        txt_first_name = Entry(DataEntryFrame,textvariable=self.first_name_var,font=('times new roman',15,'bold'))
        txt_first_name.grid(row=2,column=1,pady=10)

#================== LastName =======================================

        lbl_last_name = Label(DataEntryFrame,text='LAST NAME:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_last_name.grid(row=3,column=0,sticky='w')

        txt_last_name = Entry(DataEntryFrame,textvariable=self.last_name_var,font=('times new roman',15,'bold'))
        txt_last_name.grid(row=3,column=1,pady=10)

#=================== Course =========================================

        lbl_course = Label(DataEntryFrame,text='COURSE:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_course.grid(row=4,column=0,sticky='w')

        txt_course = Entry(DataEntryFrame,textvariable=self.course_var,font=('times new roman',15,'bold'))
        txt_course.grid(row=4,column=1,pady=10)

#================= Fee ================================
        lbl_fee = Label(DataEntryFrame,text='FEE:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_fee.grid(row=5,column=0,sticky='w')

        txt_fee = Entry(DataEntryFrame,textvariable=self.fee_var,font=('times new roman',15,'bold'))
        txt_fee.grid(row=5,column=1,pady=10)

#================== Contact ==============================

        lbl_contact = Label(DataEntryFrame,text='CONTACT:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_contact.grid(row=6,column=0,sticky='w')

        txt_contact = Entry(DataEntryFrame,textvariable=self.contact_var,font=('times new roman',15,'bold'))
        txt_contact.grid(row=6,column=1,pady=10)

#================== Trainer ================================

        lbl_trainer = Label(DataEntryFrame,text='TRAINER:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_trainer.grid(row=7,column=0,sticky='w')

        txt_trainer = Entry(DataEntryFrame,textvariable=self.trainer_var,font=('times new roman',15,'bold'))
        txt_trainer.grid(row=7,column=1,pady=10)
#===================== Email ID =============================

        lbl_emailid = Label(DataEntryFrame,text='Email ID',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_emailid.grid(row=8,column=0,sticky='w')

        txt_emailid = Entry(DataEntryFrame,textvariable=self.emailid_var,font=('times new roman',15,'bold'))
        txt_emailid.grid(row=8,column=1,pady=10)

#================== start_date ==============================

        lbl_start_date = Label(DataEntryFrame,text='START_DATE:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_start_date.grid(row=9,column=0,sticky='w')

        txt_start_date = Entry(DataEntryFrame,textvariable=self.start_date_var,font=('times new roman',15,'bold'))
        txt_start_date.grid(row=9,column=1,pady=10)

#================== Gender =========================================

        lbl_genger = Label(DataEntryFrame,text='GENDER:',bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_genger.grid(row=10,column=0,sticky='w')

        txt_gender = Entry(DataEntryFrame,textvariable=self.gender_var,font=('times new roman',15,'bold'))
        txt_gender.grid(row=10,column=1,pady=10)

#==================== Button ======================================

        btn_frame = Frame(DataEntryFrame,bd=4,relief=GROOVE,bg='green')
        btn_frame.place(x=10,y=532,width=370,height=50)

        btn_add = Button(btn_frame,command=self.adding_data,text='Add',font=('times new roman',11,'bold'),width=8,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=10,pady=7)

        btn_update = Button(btn_frame,command=self.update_data,text='Update',font=('times new roman',11,'bold'),width=7,bg='yellow',fg='red')
        btn_update.grid(row=0,column=1,padx=5,pady=7)

        btn_clear = Button(btn_frame,command=self.clear,text='Clear',font=('times new roman',11,'bold'),width=8,bg='pink',fg='red')
        btn_clear.grid(row=0,column=2,padx=5,pady=7)

        btn_delete = Button(btn_frame,command=self.delete_data,text='Delete',font=('times new roman',11,'bold'),width=7,bg='red',fg='black')
        btn_delete.grid(row=0,column=3,padx=5,pady=7)



#================ DataDisplayFrame ===========================================

        DataDisplayFrame = Frame(self.root,bg='green',bd=5,relief=GROOVE)
        DataDisplayFrame.place(x=420,y=50,width=970,height=600)


        lbl_search = Label(DataDisplayFrame,text='Search BY:',width=15,bg='green',fg='white',font=('times new roman',15,'bold'))
        lbl_search.grid(row=0,column=0,padx=10,pady=20)

        combo_search = ttk.Combobox(DataDisplayFrame,textvariable=self.searchby,font=('times new roman',15,'bold'),width=15)
        combo_search['values']=('Course','Trainer','Gender')
        combo_search.grid(row=0,column=1,sticky='w')

        txt_search = Entry(DataDisplayFrame,textvariable=self.searchtxt,font=('times new roman',15,'bold'),width=15)
        txt_search.grid(row=0,column=2,padx=30)

        btn_search = Button(DataDisplayFrame,command=self.search_data,text='Search',bg='blue',fg='white',font=('times new roman',15,'bold'),width=10)
        btn_search.grid(row=0,column=3,padx=20)

        btn_show = Button(DataDisplayFrame,command=self.fetch_data,text='Show All',bg='yellow',fg='red',font=('times new roman',15,'bold'),width=10)
        btn_show.grid(row=0,column=4,padx=20)


        #=========================== Table Frame ===========================


        table_frame = Frame(DataDisplayFrame,bd=5,relief=GROOVE)
        table_frame.place(x=20,y=70,width=920,height=500)

        self.Student_Table = ttk.Treeview(table_frame,column=('roll_no','first_name','last_name','course','fee','contact','trainer','emailid','start_date','gender'))


        self.Student_Table.heading('roll_no',text='Roll No')
        self.Student_Table.heading('first_name',text='First Name')
        self.Student_Table.heading('last_name',text='Last Name')
        self.Student_Table.heading('course',text='Course')
        self.Student_Table.heading('fee',text='Fee')
        self.Student_Table.heading('contact',text='Contact')
        self.Student_Table.heading('trainer',text='Trainer')
        self.Student_Table.heading('emailid',text='Email ID')
        self.Student_Table.heading('start_date',text='Start Date')
        self.Student_Table.heading('gender',text='Gender')

        self.Student_Table['show']='headings'

        self.Student_Table.column('roll_no',width=70,anchor=CENTER)
        self.Student_Table.column('first_name',width=100,anchor=CENTER)
        self.Student_Table.column('last_name',width=100,anchor=CENTER)
        self.Student_Table.column('course',width=80,anchor=CENTER)
        self.Student_Table.column('fee',width=70,anchor=CENTER)
        self.Student_Table.column('contact',width=90,anchor=CENTER)
        self.Student_Table.column('trainer',width=100,anchor=CENTER)
        self.Student_Table.column('emailid',width=100,anchor=CENTER)
        self.Student_Table.column('start_date',width=100,anchor=CENTER)
        self.Student_Table.column('gender',width=70,anchor=CENTER)

        self.Student_Table.pack()
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def adding_data(self):
        connection = pymysql.connect(host='localhost', user='root', password='2425', db='nhstudentsdb')
        cursor = connection.cursor()
        cursor.execute('insert into nhstudentsinfo values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s )',
                       (self.roll_no_var.get(),
                        self.first_name_var.get(),
                        self.last_name_var.get(),
                        self.course_var.get(),
                        self.fee_var.get(),
                        self.contact_var.get(),
                        self.trainer_var.get(),
                        self.emailid_var.get(),
                        self.start_date_var.get(),
                        self.gender_var.get(),
                        ))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def fetch_data(self):
        connection = pymysql.connect(host='localhost',user='root',password='2425',db='nhstudentsdb')
        cursor = connection.cursor()
        cursor.execute('select * from nhstudentsinfo')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
                connection.commit()
            connection.close()

    def clear(self):
        self.roll_no_var.set('')
        self.first_name_var.set('')
        self.last_name_var.set('')
        self.course_var.set('')
        self.fee_var.set('')
        self.contact_var.set('')
        self.trainer_var.set('')
        self.emailid_var.set('')
        self.start_date_var.set('')
        self.gender_var.set('')

    def get_cursor(self,var):
        cursor_row = self.Student_Table.focus()
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.roll_no_var.set(row[0])
        self.first_name_var.set(row[1])
        self.last_name_var.set(row[2])
        self.course_var.set(row[3])
        self.fee_var.set(row[4])
        self.contact_var.set(row[5])
        self.trainer_var.set(row[6])
        self.emailid_var.set(row[7])
        self.start_date_var.set(row[8])
        self.gender_var.set(row[9])

    def update_data(self):
        connection = pymysql.connect(host='localhost',user='root',password='2425',db='nhstudentsdb')
        cursor = connection.cursor()
        cursor.execute('update nhstudentsinfo set first_name=%s,'
                       'last_name=%s, '
                       'course=%s, '
                       'fee=%s, '
                       'contact=%s, '
                       'trainer=%s, '
                       'emailid=%s, '
                       'start_date=%s, '
                       'gender=%s where roll_no=%s',
                       (self.first_name_var.get(),
                        self.last_name_var.get(),
                        self.course_var.get(),
                        self.fee_var.get(),
                        self.contact_var.get(),
                        self.trainer_var.get(),
                        self.emailid_var.get(),
                        self.start_date_var.get(),
                        self.gender_var.get(),
                         self.roll_no_var.get(),))
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()


    def delete_data(self):
        connection = pymysql.connect(host='localhost',user='root',password='2425',db='nhstudentsdb')
        cursor = connection.cursor()
        cursor.execute('delete from nhstudentsinfo where roll_no=%s',self.roll_no_var.get())
        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def search_data(self):
        connection = pymysql.connect(host='localhost',user='root',password='2425',db='nhstudentsdb')
        cursor = connection.cursor()
        cursor.execute("select * from nhstudentsinfo "
                       "where "+str(self.searchby.get())+" like '%"+str(self.searchtxt.get())+"%'")
        rows = cursor.fetchall()

        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            connection.commit()
        connection.close()




root = Tk()
obj = NHStudentsData(root)
root.mainloop()