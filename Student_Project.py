import oracledb
from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import logging

# Set appearance mode
set_appearance_mode("light")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Connect to the Oracle database
try:
    connection = oracledb.connect(
       user="SYSTEM", password="Rijja", dsn="localhost:1522/XEPDB1"
    )
    logging.info("Connected to Oracle Database")
except oracledb.Error as e:
    logging.error("Error connecting to Oracle Database:", exc_info=True)
    messagebox.showerror('Database Error', 'Unable to connect to Oracle Database.\n Please check the logs.')


set_appearance_mode("light")


class LoginWindow:
    def __init__(self):
        # Initialize the main login window
        self.window = CTk()
        self.window.geometry("725x500")
        self.window.title("Student Information System")
        self.window.resizable(0, 0)

        # Load images
        side_img_data = Image.open("new1.png")
        email_icon_data = Image.open("email-icon.png")
        password_icon_data = Image.open("password-icon.png")

        # Convert images for use in widgets
        self.side_img = CTkImage(light_image=side_img_data.resize((350, 600)), size=(350, 600))
        self.email_icon = CTkImage(light_image=email_icon_data, size=(20, 20))
        self.password_icon = CTkImage(light_image=password_icon_data, size=(17, 17))

        # Left side image
        CTkLabel(master=self.window, text="", image=self.side_img).pack(expand=True, side="left")

        # Right side frame
        frame = CTkFrame(master=self.window, width=600, height=600, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        # Labels and input fields
        CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email:", text_color="#601E88", font=("Arial Bold", 14), image=self.email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.email_entry.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#601E88", font=("Arial Bold", 14), image=self.password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.password_entry.pack(anchor="w", padx=(25, 0))

        CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.check_login).pack(anchor="w", pady=(40, 0), padx=(25, 0))

    def check_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email in ("rijja2310119@ssn.edu.in", "nilaa2310402@ssn.edu.in", "") and password in ("Rijja", "Nilaa", ""):
            self.logged_in() # Open the admin window
        else:
            messagebox.showerror('Invalid Login', 'Username or Password is incorrect.\n Try Again')

    def run(self):
        self.window.mainloop()

    def logged_in(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        # Sidebar Frame
        self.sidebar_frame = CTkFrame(self.window, width=180, height=500, corner_radius=0, fg_color="#4B0082")
        self.sidebar_frame.place(x=0, y=0)

        # Sidebar Title and Buttons
        self.dashboard_title = CTkLabel(self.sidebar_frame, text="Dashboard", font=("Arial", 18, "bold"), text_color="white")
        self.dashboard_title.place(x=30, y=20)

        self.student_details_button = CTkButton(self.sidebar_frame, text="Student Details", command=self.create_student_list_view, width=140, fg_color="white", text_color="#4B0082", font=("Arial", 12, "bold"))
        self.student_details_button.place(x=20, y=140)

        self.course_details_button = CTkButton(self.sidebar_frame, text="Course Details", command=self.create_course_list_view, width=140, fg_color="white", text_color="#4B0082", font=("Arial", 12, "bold"))
        self.course_details_button.place(x=20, y=200)

        self.dept_details_button = CTkButton(self.sidebar_frame, text="Department Details", command=self.create_department_list_view, width=140, fg_color="white", text_color="#4B0082", font=("Arial", 12, "bold"))
        self.dept_details_button.place(x=20, y=260)

        self.show_home_view()

    def clear_window(self):
        for widget in self.window.winfo_children():
            if widget not in [self.sidebar_frame, self.dashboard_title, self.student_details_button]:
                widget.destroy()

    def show_home_view(self):
        self.clear_window()
        home_label = CTkLabel(self.window, text="Welcome to the Admin Dashboard", font=("Arial", 18, "bold"), text_color="#4B0082")
        home_label.place(x=250, y=100)

    def create_student_list_view(self):
        self.clear_window()
        title_label = CTkLabel(self.window, text="Student Management System", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        self.filter_frame = CTkFrame(self.window, corner_radius=10, width=500, height=50, fg_color="#E44982")
        self.filter_frame.place(x=200, y=70)
        self.year_entry = CTkEntry(self.filter_frame, placeholder_text="Year", width=100)
        self.year_entry.place(x=10, y=10)
        self.department_entry = CTkEntry(self.filter_frame, placeholder_text="Department", width=150)
        self.department_entry.place(x=120, y=10)
        self.search_button = CTkButton(self.filter_frame, text="Search", command=self.filtered_student_list_view, width=100, fg_color="white", text_color="#E44982")
        self.search_button.place(x=380, y=10)

        self.students_frame = CTkFrame(self.window, corner_radius=10, width=500, height=250, fg_color="white")
        self.students_frame.place(x=200, y=130)
        self.scrollable_student_list = CTkScrollableFrame(self.students_frame, width=480, height=230, fg_color='white')
        self.scrollable_student_list.place(x=10, y=10)

        self.fetch_students_data()

        for index, Student in enumerate(self.students_data):
            student_button = CTkButton(self.scrollable_student_list, text=f"{Student[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_student_profile(i))
            student_button.pack(pady=2, padx=5)

        self.add_button = CTkButton(self.window, text="Add Student", command=lambda i=index:self.add_student(i), width=150, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=400)
        self.delete_button = CTkButton(self.window, text="Delete Student", command=lambda i=index:self.delete_student(i),  width=150, fg_color="#E44982", text_color="white")
        self.delete_button.place(x=500, y=400)

    def fetch_filtered_data(self,year,dept):
        try:
            cursor = connection.cursor()
            if year and dept:
                cursor.execute("SELECT s.* FROM students s JOIN departments d ON s.department_id = d.department_id WHERE s.year_of_study = :year AND d.department_name = :dept",{"year":int(year),"dept":dept})
            elif year and not dept:
                cursor.execute("SELECT * FROM students WHERE year_of_study = :year",{"year":int(year)})
            elif dept and not year:
                cursor.execute("SELECT s.* FROM students s JOIN departments d ON s.department_id = d.department_id WHERE d.department_name = :dept",{'dept':dept})
            else:
                cursor.execute("SELECT * FROM students")
            self.students_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching students data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching Student data.\n Please check the logs.')

    def filtered_student_list_view(self):
        year = self.year_entry.get()
        dept = self.department_entry.get()
        self.clear_window()
        title_label = CTkLabel(self.window, text="Student Management System", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        self.filter_frame = CTkFrame(self.window, corner_radius=10, width=500, height=50, fg_color="#E44982")
        self.filter_frame.place(x=200, y=70)
        self.year_entry = CTkEntry(self.filter_frame, placeholder_text="Year", width=100)
        self.year_entry.place(x=10, y=10)
        self.department_entry = CTkEntry(self.filter_frame, placeholder_text="Department", width=150)
        self.department_entry.place(x=120, y=10)
        self.search_button = CTkButton(self.filter_frame, text="Search", command=self.filtered_student_list_view, width=100, fg_color="white", text_color="#E44982")
        self.search_button.place(x=380, y=10)

        self.students_frame = CTkFrame(self.window, corner_radius=10, width=500, height=250, fg_color="white")
        self.students_frame.place(x=200, y=130)
        self.scrollable_student_list = CTkScrollableFrame(self.students_frame, width=480, height=230, fg_color='white')
        self.scrollable_student_list.place(x=10, y=10)

        self.fetch_filtered_data(year,dept)

        for index, Student in enumerate(self.students_data):
            student_button = CTkButton(self.scrollable_student_list, text=f"{Student[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_student_profile(i))
            student_button.pack(pady=2, padx=5)

        self.add_button = CTkButton(self.window, text="Add Student", command=lambda i=index:self.add_student(i), width=150, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=400)
        self.delete_button = CTkButton(self.window, text="Delete Student", command=lambda i=index:self.delete_student(i),  width=150, fg_color="#E44982", text_color="white")
        self.delete_button.place(x=500, y=400)


    def fetch_students_data(self):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")
            self.students_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching students data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching Student data.\n Please check the logs.')

    def open_student_profile(self, index):
        self.clear_window()
        Student = self.students_data[index]
        title_label = CTkLabel(self.window, text=f"{Student[1]}'s Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        back_button = CTkButton(self.window, text="Back", command=self.create_student_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=400, fg_color="white")
        profile_frame.place(x=200, y=70)

        self.id_label = CTkLabel(profile_frame, text="Id ")
        self.id_label.place(x=40, y=20)

        self.id_entry = CTkEntry(profile_frame, placeholder_text="ID", width=300, fg_color="#f3f3f3")
        self.id_entry.insert(0, Student[0])
        self.id_entry.place(x=150, y=20)


        self.name_label = CTkLabel(profile_frame, text="Name ")
        self.name_label.place(x=40, y=70)

        self.name_entry = CTkEntry(profile_frame, placeholder_text="Name", width=300, fg_color="#f3f3f3")
        self.name_entry.insert(0, Student[1])
        self.name_entry.place(x=150, y=70)

        self.email_label = CTkLabel(profile_frame, text="Email id ")
        self.email_label.place(x=40, y=120)

        self.email_entry = CTkEntry(profile_frame, placeholder_text="Email id", width=300, fg_color="#f3f3f3")
        self.email_entry.insert(0, Student[2])
        self.email_entry.place(x=150, y=120)


        self.dob_label = CTkLabel(profile_frame, text="DOB ")
        self.dob_label.place(x=40, y=170)

        self.dob_entry = CTkEntry(profile_frame, placeholder_text="DOB", width=300, fg_color="#f3f3f3")
        self.dob_entry.insert(0, Student[3])
        self.dob_entry.place(x=150, y=170)

        self.ph_label = CTkLabel(profile_frame, text="Phone No ")
        self.ph_label.place(x=40, y=220)

        self.ph_entry = CTkEntry(profile_frame, placeholder_text="Phone No", width=300, fg_color="#f3f3f3")
        self.ph_entry.insert(0, Student[4])
        self.ph_entry.place(x=150, y=220)

        self.dept_label = CTkLabel(profile_frame, text="Department ")
        self.dept_label.place(x=40, y=270)

        self.dept_entry = CTkEntry(profile_frame, placeholder_text="Department", width=300, fg_color="#f3f3f3")
        self.dept_entry.insert(0, Student[5])
        self.dept_entry.place(x=150, y=270)

        self.year_label = CTkLabel(profile_frame, text="Year ")
        self.year_label.place(x=40, y=320)

        self.year_entry = CTkEntry(profile_frame, placeholder_text="Year", width=300, fg_color="#f3f3f3")
        self.year_entry.insert(0, Student[6])
        self.year_entry.place(x=150, y=320)

        save_button = CTkButton(profile_frame, text="Save Changes", command=self.save_student_changes, width=150, fg_color="#4B0082", text_color="white")  
        save_button.place(x=75, y=360)
        enroll_button = CTkButton(profile_frame, text="Enrolled", command=lambda i=Student[0]:self.enroll(i), width=150, fg_color="#4B0082", text_color="white")  
        enroll_button.place(x=275, y=360)


    def save_student_changes(self):
        updated_id = self.id_entry.get()
        updated_name = self.name_entry.get()
        updated_email = self.email_entry.get()
        updated_dob = self.dob_entry.get()
        updated_phone = self.ph_entry.get()
        updated_dept = self.dept_entry.get()
        updated_year = self.year_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE students
                SET student_name = :student_name,
                    email = :email_id,
                    date_of_birth = :date_of_birth,
                    phone_number = :phone_number,
                    department_id = :department_id,
                    year_of_study = :year_of_study
                WHERE student_id = :id
            """, {
                'student_name': updated_name,
                'email_id': updated_email,
                'date_of_birth': updated_dob,
                'phone_number': updated_phone,
                'department_id': updated_dept,
                'year_of_study': updated_year,
                'id': updated_id
            })
            connection.commit()
            messagebox.showinfo('Success', 'Student data updated successfully.')
        except oracledb.Error as e:
            logging.error("Error updating Student data:", exc_info=True)
            messagebox.showerror('Database Error', 'Error updating Student data.\n Please check the logs.')

    def fetch_student_course(self,sid):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT c.course_name FROM Courses c join enrollment e on c.course_id = e.course_id where e.student_id = {sid}")
            self.courses_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching courses data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching course data.\nPlease check the logs.')

    def enroll(self, sid):
        """Displays the Course list view with options to view, add, and delete courses."""
        self.clear_window()

        # Title and Filter Frame
        title_label = CTkLabel(self.window, text="Enrolled Courses", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        # Course List
        self.courses_frame = CTkFrame(self.window, corner_radius=10, width=500, height=280, fg_color="white")
        self.courses_frame.place(x=200, y=70)
        self.scrollable_course_list = CTkScrollableFrame(self.courses_frame, width=480, height=250, fg_color='white')
        self.scrollable_course_list.place(x=10, y=10)

        self.fetch_student_course(sid)

        for index, course in enumerate(self.courses_data):
            course_button = CTkButton(self.scrollable_course_list, text=f"{course[0]}", width=450, fg_color="white", text_color="#4B0082", anchor="w")
            course_button.pack(pady=2, padx=5)
        self.add_button = CTkButton(self.window, text="Enroll", width=150, fg_color="#E44982", text_color="white", command = lambda i=sid :self.enroll_course(i))
        self.add_button.place(x=250, y=400)
        self.delete_button_button = CTkButton(self.window, text="Withdraw", width=150, fg_color="#E44982", text_color="white", command = lambda i=sid :self.withdraw_course(i))
        self.delete_button_button.place(x=500, y=400)
    
    def enroll_course(self,sid):
        cid_dialog = CTkInputDialog(text = 'Input Course ID to enroll in : ', title = 'Enroll Course')
        cid = cid_dialog.get_input()
        try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO enrollment (student_id, course_id)
                    VALUES (:student_id,:course_id)
                """, {
                    'student_id':sid,
                    'course_id' :cid
                })
                connection.commit()
                res = messagebox.showinfo('Success', 'Student enrolled successfully.')
                if res:
                    self.enroll(sid)

        except oracledb.Error as e:
                logging.error("Error adding Student to Oracle Database:", exc_info=True)
                messagebox.showerror('Database Error', 'Error enrolling to course.\n Please check the logs.')

    def withdraw_course(self,sid):
        cid_dialog = CTkInputDialog(text = 'Input Course ID to withdraw from : ', title = 'Withdraw Course')
        cid = cid_dialog.get_input()
        try:
                cursor = connection.cursor()
                cursor.execute("""
                    DELETE FROM Enrollment 
                    WHERE student_id = :student_id AND course_id = :course_id
                """, {
                    'student_id':sid,
                    'course_id' :cid
                })
                connection.commit()
                res = messagebox.showinfo('Success', 'Student withdrawn successfully.')
                if res:
                    self.enroll(sid)

        except oracledb.Error as e:
                logging.error("Error adding Student to Oracle Database:", exc_info=True)
                messagebox.showerror('Database Error', 'Error withdrawing from course.\n Please check the logs.')


    def add_student(self, index):
        self.clear_window()
        Student = self.students_data[index]
        title_label = CTkLabel(self.window, text="New Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        back_button = CTkButton(self.window, text="Back", command=self.create_student_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=400, fg_color="white")
        profile_frame.place(x=200, y=70)

        self.id_label = CTkLabel(profile_frame, text="Id        : ")
        self.id_label.place(x=40, y=20)

        self.id_entry = CTkEntry(profile_frame, placeholder_text="ID", width=300, fg_color="#f3f3f3")
        self.id_entry.place(x=150, y=20)


        self.name_label = CTkLabel(profile_frame, text="Name             : ")
        self.name_label.place(x=40, y=70)

        self.name_entry = CTkEntry(profile_frame, placeholder_text="Name", width=300, fg_color="#f3f3f3")
        self.name_entry.place(x=150, y=70)

        self.email_label = CTkLabel(profile_frame, text="Email id            : ")
        self.email_label.place(x=40, y=120)

        self.email_entry = CTkEntry(profile_frame, placeholder_text="Email id", width=300, fg_color="#f3f3f3")
        self.email_entry.place(x=150, y=120)


        self.dob_label = CTkLabel(profile_frame, text="DOB                    : ")
        self.dob_label.place(x=40, y=170)

        self.dob_entry = CTkEntry(profile_frame, placeholder_text="DOB", width=300, fg_color="#f3f3f3")
        self.dob_entry.place(x=150, y=170)

        self.ph_label = CTkLabel(profile_frame, text="Phone No :                ")
        self.ph_label.place(x=40, y=220)

        self.ph_entry = CTkEntry(profile_frame, placeholder_text="Phone No", width=300, fg_color="#f3f3f3")
        self.ph_entry.place(x=150, y=220)

        self.dept_label = CTkLabel(profile_frame, text="Department :            ")
        self.dept_label.place(x=40, y=270)

        self.dept_entry = CTkEntry(profile_frame, placeholder_text="Department", width=300, fg_color="#f3f3f3")
        self.dept_entry.place(x=150, y=270)

        self.year_label = CTkLabel(profile_frame, text="Year :                 ")
        self.year_label.place(x=40, y=320)

        self.year_entry = CTkEntry(profile_frame, placeholder_text="Year", width=300, fg_color="#f3f3f3")
        self.year_entry.place(x=150, y=320)

        add_button = CTkButton(profile_frame, text="Add Student", command=self.add_student_to_db, width=150, fg_color="#4B0082", text_color="white")  
        add_button.place(x=175, y=360)

    def add_student_to_db(self):
        updated_id = self.id_entry.get()
        updated_name = self.name_entry.get()
        updated_email = self.email_entry.get()
        updated_dob = self.dob_entry.get()
        updated_phone = self.ph_entry.get()
        updated_dept = self.dept_entry.get()
        updated_year = self.year_entry.get()

        try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO students (student_id, student_name, email, date_of_birth, phone_number, department_id, year_of_study)
                    VALUES (:student_id,:student_name, :email_id, :date_of_birth, :phone_number, :department_id, :year_of_study)
                """, {
                    'student_id':updated_id,
                    'student_name': updated_name,
                    'email_id': updated_email,
                    'date_of_birth': updated_dob,
                    'phone_number': updated_phone,
                    'department_id': updated_dept,
                    'year_of_study': updated_year
                })
                connection.commit()
                messagebox.showinfo('Success', 'Student added successfully.')
        except oracledb.Error as e:
                logging.error("Error adding Student to Oracle Database:", exc_info=True)
                messagebox.showerror('Database Error', 'Error adding Student.\n Please check the logs.')

    def delete_student(self,index):
        self.clear_window()
        title_label = CTkLabel(self.window, text="Delete Student", font=("Arial", 18, "bold"), text_color="#4B0082")
        back_button = CTkButton(self.window, text="Back", command=self.create_student_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        delete_frame = CTkFrame(self.window, corner_radius=10, width=500, height=200, fg_color="white")
        delete_frame.place(x=200, y=70)

        # Student ID Entry
        self.del_id_label = CTkLabel(delete_frame, text="Student ID : ")
        self.del_id_label.place(x=40, y=40)

        self.del_id_entry = CTkEntry(delete_frame, placeholder_text="Enter Student ID", width=300, fg_color="#f3f3f3")
        self.del_id_entry.place(x=150, y=40)

        # Delete Button
        delete_button = CTkButton(delete_frame, text="Delete Student", command=self.delete_student_from_db, width=150, fg_color="#E44982", text_color="white")
        delete_button.place(x=175, y=100)
            

    def delete_student_from_db(self):
        student_id = self.del_id_entry.get()
        try:
                cursor = connection.cursor()
                # Deleting the student from the database
                cursor.execute("""
                    DELETE FROM students
                    WHERE student_id = :student_id
                """, {
                    'student_id': student_id
                })
                connection.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo('Success', 'Student deleted successfully.')
                else:
                    messagebox.showwarning('Not Found', 'Student ID not found.')

        except oracledb.Error as e:
                logging.error("Error deleting Student from Oracle Database:", exc_info=True)
                messagebox.showerror('Database Error', 'Error deleting Student.\n Please check the logs.')


                

    def fetch_Courses_data(self):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Courses")
            self.courses_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching courses data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching course data.\nPlease check the logs.')

    def fetch_Course_data(self,course_id):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM Courses WHERE course_id = {course_id}")
            self.courses_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching courses data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching course data.\nPlease check the logs.')


    def create_course_list_view(self):
        """Displays the Course list view with options to view, add, and delete courses."""
        self.clear_window()

        # Title and Filter Frame
        title_label = CTkLabel(self.window, text="Course Management System", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        self.course_filter_frame = CTkFrame(self.window, corner_radius=10, width=500, height=50, fg_color="#E44982")
        self.course_filter_frame.place(x=200, y=70)
        self.course_department_entry = CTkEntry(self.course_filter_frame, placeholder_text="Department", width=150)
        self.course_department_entry.place(x=10, y=10)
        self.course_entry = CTkEntry(self.course_filter_frame, placeholder_text="Course Name", width=150)
        self.course_entry.place(x=175, y=10)
    
        self.course_search_button = CTkButton(self.course_filter_frame, text="Search", command=self.filtered_course_list_view, width=100, fg_color="white", text_color="#E44982")
        self.course_search_button.place(x=380, y=10)

        # Course List
        self.courses_frame = CTkFrame(self.window, corner_radius=10, width=500, height=250, fg_color="white")
        self.courses_frame.place(x=200, y=130)
        self.scrollable_course_list = CTkScrollableFrame(self.courses_frame, width=480, height=230, fg_color='white')
        self.scrollable_course_list.place(x=10, y=10)

        self.fetch_Courses_data()

        for index, course in enumerate(self.courses_data):
            course_button = CTkButton(self.scrollable_course_list, text=f"{course[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_course_profile(i))
            course_button.pack(pady=2, padx=5)
        self.add_button = CTkButton(self.window, text="Add Course", command=lambda i=index:self.add_course(i), width=100, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=400)
        self.delete_button_button = CTkButton(self.window, text="Delete Course", command=lambda i=index:self.delete_course(i), width=100, fg_color="#E44982", text_color="white")
        self.delete_button_button.place(x=400, y=400)

    def fetch_filtered_course_data(self,cname,dept):
        try:
            cursor = connection.cursor()
            if cname and dept:
                cursor.execute("SELECT c.* FROM courses c JOIN departments d ON c.department_id = d.department_id WHERE c.couse_name = :name AND d.department_name = :dept",{"name":cname,"dept":dept})
            elif cname and not dept:
                cursor.execute("SELECT * FROM courses WHERE course_name = :name",{"name":cname})
            elif dept and not cname:
                cursor.execute("SELECT c.* FROM courses c JOIN departments d ON c.department_id = d.department_id WHERE d.department_name = :dept",{'dept':dept})
            else:
                cursor.execute("SELECT * FROM courses")
            self.courses_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching students data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching Student data.\n Please check the logs.')

    def filtered_course_list_view(self):
        dept = self.course_department_entry.get()
        cname = self.course_entry.get()
        self.clear_window()
        
        title_label = CTkLabel(self.window, text="Course Management System", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        self.course_filter_frame = CTkFrame(self.window, corner_radius=10, width=500, height=50, fg_color="#E44982")
        self.course_filter_frame.place(x=200, y=70)
        self.course_department_entry = CTkEntry(self.course_filter_frame, placeholder_text="Department", width=150)
        self.course_department_entry.place(x=10, y=10)
        self.course_entry = CTkEntry(self.course_filter_frame, placeholder_text="Course Name", width=150)
        
        self.course_entry.place(x=175, y=10)
    
        self.course_search_button = CTkButton(self.course_filter_frame, text="Search", command=self.filtered_course_list_view, width=100, fg_color="white", text_color="#E44982")
        self.course_search_button.place(x=380, y=10)

        # Course List
        self.courses_frame = CTkFrame(self.window, corner_radius=10, width=500, height=250, fg_color="white")
        self.courses_frame.place(x=200, y=130)
        self.scrollable_course_list = CTkScrollableFrame(self.courses_frame, width=480, height=230, fg_color='white')
        self.scrollable_course_list.place(x=10, y=10)

        self.fetch_filtered_course_data(cname,dept)

        for index, course in enumerate(self.courses_data):
            course_button = CTkButton(self.scrollable_course_list, text=f"{course[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_course_profile(i))
            course_button.pack(pady=2, padx=5)
        self.add_button = CTkButton(self.window, text="Add Course", command=lambda i=index:self.add_course(i), width=100, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=400)
        self.delete_button_button = CTkButton(self.window, text="Delete Course", command=lambda i=index:self.delete_course(i), width=100, fg_color="#E44982", text_color="white")
        self.delete_button_button.place(x=400, y=400)


        
    def open_course_profile(self, index):
        """Displays selected Course's profile with editable fields."""
        self.clear_window()
       

        course = self.courses_data[index]
        profile_title_label = CTkLabel(self.window, text=f"{course[1]}'s Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        profile_title_label.place(x=200, y=60)

        back_button = CTkButton(self.window, text="Back", command=self.create_course_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=400, fg_color="white")
        profile_frame.place(x=200, y=100)

        # Display Course Fields
        self.id_label = CTkLabel(profile_frame, text="Course ID:")
        self.id_label.place(x=40, y=20)
        self.id_entry = CTkEntry(profile_frame, placeholder_text="Course ID", width=300, fg_color="#f3f3f3")
        self.id_entry.insert(0, course[0])
        self.id_entry.place(x=150, y=20)

        self.name_label = CTkLabel(profile_frame, text="Course Name:")
        self.name_label.place(x=40, y=70)
        self.name_entry = CTkEntry(profile_frame, placeholder_text="Course Name", width=300, fg_color="#f3f3f3")
        self.name_entry.insert(0, course[1])
        self.name_entry.place(x=150, y=70)

        self.d_id_label = CTkLabel(profile_frame, text="Department ID:")
        self.d_id_label.place(x=40, y=120)
        self.d_id_entry = CTkEntry(profile_frame, placeholder_text="Department ID", width=300, fg_color="#f3f3f3")
        self.d_id_entry.insert(0, course[2])
        self.d_id_entry.place(x=150, y=120)

        save_button = CTkButton(profile_frame, text="Save Changes", command=lambda: self.save_course_changes(course[0], self.name_entry.get(), self.d_id_entry.get()), width=150, fg_color="#4B0082", text_color="white")
        save_button.place(x=75, y=190)

        enrolled_button = CTkButton(profile_frame, text="Enrolled Students", command=lambda: self.enrolled_students(course[0]), width=150, fg_color="#4B0082", text_color="white")
        enrolled_button.place(x=250, y=190)

    def fetch_course_students(self,cid):
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT s.* FROM students s join enrollment e on s.student_id = e.student_id where e.course_id = {cid}")
            self.students_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching courses data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching course data.\nPlease check the logs.')

    def enrolled_students(self, cid):
        """Displays the Course list view with options to view, add, and delete courses."""
        self.clear_window()

        # Title and Filter Frame
        title_label = CTkLabel(self.window, text="Enrolled Students", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        # Course List
        self.students_frame = CTkFrame(self.window, corner_radius=10, width=500, height=250, fg_color="white")
        self.students_frame.place(x=200, y=75)
        self.scrollable_student_list = CTkScrollableFrame(self.students_frame, width=480, height=230, fg_color='white')
        self.scrollable_student_list.place(x=10, y=10)

        self.fetch_course_students(cid)

        for index, Student in enumerate(self.students_data):
            student_button = CTkButton(self.scrollable_student_list, text=f"{Student[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_student_profile_in_course(i))
            student_button.pack(pady=2, padx=5)

        self.add_button = CTkButton(self.window, text="Enroll Student", command=lambda i=cid:self.enroll_student(i), width=150, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=400)
        self.delete_button = CTkButton(self.window, text="Withdraw Student", command=lambda i=cid:self.withdraw_student(i),  width=150, fg_color="#E44982", text_color="white")
        self.delete_button.place(x=500, y=400)

    def open_student_profile_in_course(self, index):
        self.clear_window()
        Student = self.students_data[index]
        title_label = CTkLabel(self.window, text=f"{Student[1]}'s Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=400, fg_color="white")
        profile_frame.place(x=200, y=70)

        self.id_label = CTkLabel(profile_frame, text="Id ")
        self.id_label.place(x=40, y=20)

        self.id_entry = CTkEntry(profile_frame, placeholder_text="ID", width=300, fg_color="#f3f3f3")
        self.id_entry.insert(0, Student[0])
        self.id_entry.place(x=150, y=20)


        self.name_label = CTkLabel(profile_frame, text="Name ")
        self.name_label.place(x=40, y=70)

        self.name_entry = CTkEntry(profile_frame, placeholder_text="Name", width=300, fg_color="#f3f3f3")
        self.name_entry.insert(0, Student[1])
        self.name_entry.place(x=150, y=70)

        self.email_label = CTkLabel(profile_frame, text="Email id ")
        self.email_label.place(x=40, y=120)

        self.email_entry = CTkEntry(profile_frame, placeholder_text="Email id", width=300, fg_color="#f3f3f3")
        self.email_entry.insert(0, Student[2])
        self.email_entry.place(x=150, y=120)


        self.dob_label = CTkLabel(profile_frame, text="DOB ")
        self.dob_label.place(x=40, y=170)

        self.dob_entry = CTkEntry(profile_frame, placeholder_text="DOB", width=300, fg_color="#f3f3f3")
        self.dob_entry.insert(0, Student[3])
        self.dob_entry.place(x=150, y=170)

        self.ph_label = CTkLabel(profile_frame, text="Phone No ")
        self.ph_label.place(x=40, y=220)

        self.ph_entry = CTkEntry(profile_frame, placeholder_text="Phone No", width=300, fg_color="#f3f3f3")
        self.ph_entry.insert(0, Student[4])
        self.ph_entry.place(x=150, y=220)

        self.dept_label = CTkLabel(profile_frame, text="Department ")
        self.dept_label.place(x=40, y=270)

        self.dept_entry = CTkEntry(profile_frame, placeholder_text="Department", width=300, fg_color="#f3f3f3")
        self.dept_entry.insert(0, Student[5])
        self.dept_entry.place(x=150, y=270)

        self.year_label = CTkLabel(profile_frame, text="Year ")
        self.year_label.place(x=40, y=320)

        self.year_entry = CTkEntry(profile_frame, placeholder_text="Year", width=300, fg_color="#f3f3f3")
        self.year_entry.insert(0, Student[6])
        self.year_entry.place(x=150, y=320)

        save_button = CTkButton(profile_frame, text="Save Changes", command=self.save_student_changes, width=150, fg_color="#4B0082", text_color="white")  
        save_button.place(x=75, y=360)
        enroll_button = CTkButton(profile_frame, text="Enrolled", command=lambda i=Student[0]:self.enroll(i), width=150, fg_color="#4B0082", text_color="white")  
        enroll_button.place(x=275, y=360)

    
    def enroll_student(self,cid):
        sid_dialog = CTkInputDialog(text = 'Input Student ID to enroll : ', title = 'Enroll Student')
        sid = sid_dialog.get_input()
        try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO enrollment (student_id, course_id)
                    VALUES (:student_id,:course_id)
                """, {
                    'student_id':sid,
                    'course_id' :cid
                })
                connection.commit()
                res = messagebox.showinfo('Success', 'Student enrolled successfully.')
                if res:
                    self.enrolled_students(cid)

        except oracledb.Error as e:
                logging.error("Error adding Student to Oracle Database:", exc_info=True)
                messagebox.showerror('Database Error', 'Error enrolling to course.\n Please check the logs.')

    def withdraw_student(self,cid):
        sid_dialog = CTkInputDialog(text = 'Input Student ID to withdraw from : ', title = 'Withdraw Student')
        sid = sid_dialog.get_input()
        try:
                cursor = connection.cursor()
                cursor.execute("""
                    DELETE FROM Enrollment 
                    WHERE student_id = :student_id AND course_id = :course_id
                """, {
                    'student_id':sid,
                    'course_id' :cid
                })
                connection.commit()
                res = messagebox.showinfo('Success', 'Student withdrawn successfully.')
                if res:
                    self.enrolled_students(cid)

        except oracledb.Error as e:
                logging.error("Error adding Student to Oracle Database:", exc_info=True)
                messagebox.showerror('Database Error', 'Error withdrawing from course.\n Please check the logs.')



    def save_course_changes(self, course_id, new_course_name=None, new_dept_id=None):
    # Method to update a course

        updated_id = self.id_entry.get()
        updated_name = self.name_entry.get()
        updated_dept = self.d_id_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE courses
                SET course_name = :course_name,
                    department_id = :department_id
                WHERE course_id = :course_id
            """, {
                'course_name': updated_name,
                'department_id': updated_dept,
                'course_id': updated_id
            })
            connection.commit()
            messagebox.showinfo('Success', 'Course data updated successfully.')
        except oracledb.Error as e:
            logging.error("Error updating course data:", exc_info=True)
            messagebox.showerror('Database Error', 'Error updating course data.\n Please check the logs.')

# Method to fetch courses data
    def fetch_courses_data(self):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM courses")
            self.courses_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching courses data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching courses data.\n Please check the logs.')

        # Refresh the course list view to reflect changes
        self.create_course_list_view()

    def add_course(self,index):
        self.clear_window()

        course = self.courses_data[index]
        title_label = CTkLabel(self.window, text="New Course Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        back_button = CTkButton(self.window, text="Back", command=self.create_course_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=300, fg_color="white")
        profile_frame.place(x=200, y=70)

        # Course ID
        self.id_label = CTkLabel(profile_frame, text="Course ID : ")
        self.id_label.place(x=40, y=20)
        self.id_entry = CTkEntry(profile_frame, placeholder_text="Course ID", width=300, fg_color="#f3f3f3")
        self.id_entry.place(x=150, y=20)

        # Course Name
        self.name_label = CTkLabel(profile_frame, text="Course Name : ")
        self.name_label.place(x=40, y=70)
        self.name_entry = CTkEntry(profile_frame, placeholder_text="Course Name", width=300, fg_color="#f3f3f3")
        self.name_entry.place(x=150, y=70)

        # Department ID
        self.dept_label = CTkLabel(profile_frame, text="Department ID : ")
        self.dept_label.place(x=40, y=120)
        self.dept_entry = CTkEntry(profile_frame, placeholder_text="Department ID", width=300, fg_color="#f3f3f3")
        self.dept_entry.place(x=150, y=120)

        # Add Course Button
        add_button = CTkButton(profile_frame, text="Add Course", command=self.add_course_to_db, width=150, fg_color="#4B0082", text_color="white")  
        add_button.place(x=175, y=180)

# Method to insert course into the database
    def add_course_to_db(self):
        course_id = self.id_entry.get()
        course_name = self.name_entry.get()
        department_id = self.dept_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO courses (course_id, course_name, department_id)
                VALUES (:course_id, :course_name, :department_id)
            """, {
                'course_id': course_id,
                'course_name': course_name,
                'department_id': department_id
            })
            connection.commit()
            messagebox.showinfo('Success', 'Course added successfully.')
        except oracledb.Error as e:
            logging.error("Error adding course to Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error adding course.\n Please check the logs.')

    def delete_course(self,index):
        self.clear_window()

        title_label = CTkLabel(self.window, text="Delete Course", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        back_button = CTkButton(self.window, text="Back", command=self.create_course_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        delete_frame = CTkFrame(self.window, corner_radius=10, width=500, height=200, fg_color="white")
        delete_frame.place(x=200, y=70)

        # Course ID Entry
        self.del_id_label = CTkLabel(delete_frame, text="Course ID : ")
        self.del_id_label.place(x=40, y=40)
        self.del_id_entry = CTkEntry(delete_frame, placeholder_text="Enter Course ID", width=300, fg_color="#f3f3f3")
        self.del_id_entry.place(x=150, y=40)

        # Delete Course Button
        delete_button = CTkButton(delete_frame, text="Delete Course", command=self.delete_course_from_db, width=150, fg_color="#E44982", text_color="white")
        delete_button.place(x=175, y=100)

    def delete_course_from_db(self):
        course_id = self.del_id_entry.get()

        try:
            cursor = connection.cursor()
            # Deleting the course from the database
            cursor.execute("""
                DELETE FROM courses
                WHERE course_id = :course_id
            """, {
                'course_id': course_id
            })
            connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo('Success', 'Course deleted successfully.')
            else:
                messagebox.showwarning('Not Found', 'Course ID not found.')

        except oracledb.Error as e:
            logging.error("Error deleting course from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error deleting course.\n Please check the logs.')

    def fetch_departments_data(self):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM departments ORDER BY department_id")
            self.departments_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching departments data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching department data.\nPlease check the logs.')

    def create_department_list_view(self):
        """Displays the Department list view with options to view, add, and delete departments."""
        self.clear_window()

        title_label = CTkLabel(self.window, text="Department Management System", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        self.filter_frame = CTkFrame(self.window, corner_radius=10, width=500, height=50, fg_color="#E44982")
        self.filter_frame.place(x=200, y=70)
        self.dept_search_entry = CTkEntry(self.filter_frame, placeholder_text="Department", width=150)
        self.dept_search_entry.place(x=10, y=10)

        self.course_dept_search_entry = CTkEntry(self.filter_frame, placeholder_text="Course Name", width=150)
        self.course_dept_search_entry.place(x=175, y=10)

        self.search_button = CTkButton(self.filter_frame, text="Search", command=self.filtered_dept_list_view, width=100, fg_color="white", text_color="#E44982")
        self.search_button.place(x=380, y=10)


        self.departments_frame = CTkFrame(self.window, corner_radius=10, width=500, height=280, fg_color="white")
        self.departments_frame.place(x=200, y=130)

        self.scrollable_department_list = CTkScrollableFrame(self.departments_frame, width=480, height=250, fg_color='white')
        self.scrollable_department_list.place(x=10, y=10)

        self.fetch_departments_data()

        for index, department in enumerate(self.departments_data):
            department_button = CTkButton(self.scrollable_department_list, text=f"{department[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_department_profile(i))
            department_button.pack(pady=2, padx=5)
        
        self.add_button = CTkButton(self.window, text="Add Department", command=lambda i=index: self.add_department(i), width=100, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=440)
        
        self.delete_button = CTkButton(self.window, text="Delete Department", command=lambda i=index: self.delete_department(i), width=100, fg_color="#E44982", text_color="white")
        self.delete_button.place(x=400, y=440)

    def fetch_filtered_dept_data(self,dname,cname):
        try:
            cursor = connection.cursor()
            if dname and not cname:
                cursor.execute("SELECT * FROM departments WHERE department_name = :name",{"name":dname})
            elif cname and not dname:
                cursor.execute("SELECT d.* FROM departments d JOIN courses c ON c.department_id = d.department_id WHERE c.course_name = :name",{"name":cname})
            elif cname and dname:
                cursor.execute("SELECT d.* FROM departments d JOIN courses c ON c.department_id = d.department_id WHERE c.course_name = :name AND d.department_name = :dname",{"name":cname,"dname":dname})
            else:
                cursor.execute("SELECT * FROM departments")
            self.departments_data = cursor.fetchall()
        except oracledb.Error as e:
            logging.error("Error fetching students data from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error fetching Student data.\n Please check the logs.')

    def filtered_dept_list_view(self):
        dname = self.dept_search_entry.get()
        cname = self.course_dept_search_entry.get()
        self.clear_window()

        title_label = CTkLabel(self.window, text="Department Management System", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=220, y=20)

        self.filter_frame = CTkFrame(self.window, corner_radius=10, width=500, height=50, fg_color="#E44982")
        self.filter_frame.place(x=200, y=70)
        self.dept_search_entry = CTkEntry(self.filter_frame, placeholder_text="Department", width=150)
        self.dept_search_entry.place(x=10, y=10)

        self.course_dept_search_entry = CTkEntry(self.filter_frame, placeholder_text="Course Name", width=150)
        self.course_dept_search_entry.place(x=175, y=10)

        self.search_button = CTkButton(self.filter_frame, text="Search", command=self.filtered_dept_list_view, width=100, fg_color="white", text_color="#E44982")
        self.search_button.place(x=380, y=10)


        self.departments_frame = CTkFrame(self.window, corner_radius=10, width=500, height=280, fg_color="white")
        self.departments_frame.place(x=200, y=130)

        self.scrollable_department_list = CTkScrollableFrame(self.departments_frame, width=480, height=250, fg_color='white')
        self.scrollable_department_list.place(x=10, y=10)

        self.fetch_filtered_dept_data(dname,cname)

        for index, department in enumerate(self.departments_data):
            department_button = CTkButton(self.scrollable_department_list, text=f"{department[1]}", width=450, fg_color="white", text_color="#4B0082", anchor="w", command=lambda i=index: self.open_department_profile(i))
            department_button.pack(pady=2, padx=5)
        
        self.add_button = CTkButton(self.window, text="Add Department", command=lambda i=index: self.add_department(i), width=100, fg_color="#E44982", text_color="white")
        self.add_button.place(x=250, y=440)
        
        self.delete_button = CTkButton(self.window, text="Delete Department", command=lambda i=index: self.delete_department(i), width=100, fg_color="#E44982", text_color="white")
        self.delete_button.place(x=400, y=440)



    def open_department_profile(self, index):
        """Displays selected Department's profile with editable fields."""
        self.clear_window()

        department = self.departments_data[index]
        profile_title_label = CTkLabel(self.window, text=f"{department[1]}'s Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        profile_title_label.place(x=200, y=60)

        back_button = CTkButton(self.window, text="Back", command=self.create_department_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=200, fg_color="white")
        profile_frame.place(x=200, y=100)

        # Display Department Fields
        self.id_label = CTkLabel(profile_frame, text="Department ID:")
        self.id_label.place(x=40, y=20)
        self.id_entry = CTkEntry(profile_frame, placeholder_text="Department ID", width=300, fg_color="#f3f3f3")
        self.id_entry.insert(0, department[0])
        self.id_entry.place(x=150, y=20)

        self.name_label = CTkLabel(profile_frame, text="Department Name:")
        self.name_label.place(x=40, y=70)
        self.name_entry = CTkEntry(profile_frame, placeholder_text="Department Name", width=300, fg_color="#f3f3f3")
        self.name_entry.insert(0, department[1])
        self.name_entry.place(x=150, y=70)

        save_button = CTkButton(profile_frame, text="Save Changes", command=lambda: self.save_department_changes(department), width=150, fg_color="#4B0082", text_color="white")
        save_button.place(x=175, y=130)

    def save_department_changes(self, old_department):
        updated_id = self.id_entry.get()
        updated_name = self.name_entry.get()

        try:
            cursor = connection.cursor()
            cursor.callproc('SaveDepartmentChanges', [
                old_department[0],
                old_department[1],
                updated_id,
                updated_name
            ])
            connection.commit()
            messagebox.showinfo('Success', 'Department data updated successfully.')
        except oracledb.Error as e:
            logging.error("Error updating department data:", exc_info=True)
            messagebox.showerror('Database Error', 'Error updating department data.\n Please check the logs.')


    def add_department(self, index):
        self.clear_window()

        title_label = CTkLabel(self.window, text="New Department Profile", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        back_button = CTkButton(self.window, text="Back", command=self.create_department_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        profile_frame = CTkFrame(self.window, corner_radius=10, width=500, height=200, fg_color="white")
        profile_frame.place(x=200, y=70)


        # Department Name
        self.name_label = CTkLabel(profile_frame, text="Department Name:")
        self.name_label.place(x=40, y=25)
        self.name_entry = CTkEntry(profile_frame, placeholder_text="Department Name", width=300, fg_color="#f3f3f3")
        self.name_entry.place(x=150, y=25)

        add_button = CTkButton(profile_frame, text="Add Department", command=self.add_department_to_db, width=150, fg_color="#4B0082", text_color="white")
        add_button.place(x=175, y=90)

    def add_department_to_db(self):
        department_name = self.name_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO departments (department_name)
                VALUES (:department_name)
            """, {
                'department_name': department_name
            })
            connection.commit()
            messagebox.showinfo('Success', 'Department added successfully.')
        except oracledb.Error as e:
            logging.error("Error adding department to Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error adding department.\n Please check the logs.')


    def delete_department(self, index):
        self.clear_window()

        title_label = CTkLabel(self.window, text="Delete Department", font=("Arial", 18, "bold"), text_color="#4B0082")
        title_label.place(x=200, y=20)

        back_button = CTkButton(self.window, text="Back", command=self.create_department_list_view, width=70, fg_color="#E44982", text_color="white")
        back_button.place(x=610, y=20)

        delete_frame = CTkFrame(self.window, corner_radius=10, width=500, height=200, fg_color="white")
        delete_frame.place(x=200, y=70)

        # Department ID Entry
        self.del_id_label = CTkLabel(delete_frame, text="Department ID:")
        self.del_id_label.place(x=40, y=40)
        self.del_id_entry = CTkEntry(delete_frame, placeholder_text="Enter Department ID", width=300, fg_color="#f3f3f3")
        self.del_id_entry.place(x=150, y=40)

        # Delete Button
        delete_button = CTkButton(delete_frame, text="Delete Department", command=self.delete_department_from_db, width=150, fg_color="#E44982", text_color="white")
        delete_button.place(x=175, y=100)

    def delete_department_from_db(self):
        department_id = self.del_id_entry.get()

        try:
            cursor = connection.cursor()
            cursor.execute("""
                DELETE FROM departments
                WHERE department_id = :department_id
            """, {
                'department_id': department_id
            })
            connection.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo('Success', 'Department deleted successfully.')
            else:
                messagebox.showwarning('Not Found', 'Department ID not found.')

        except oracledb.Error as e:
            logging.error("Error deleting department from Oracle Database:", exc_info=True)
            messagebox.showerror('Database Error', 'Error deleting department.\n Please check the logs.')



if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.run()
