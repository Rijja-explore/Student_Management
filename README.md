# 🎓 Student Information Management System

A modern and intuitive **Tkinter-based Student Management System** built with Python and Oracle DB. This desktop app enables admins to manage students, departments, and course enrollments with a clean graphical interface powered by **CustomTkinter**.

---

## 🌟 Key Features

- 🔐 **Login System**
  - Admin-only login interface
- 👨‍🎓 **Student Management**
  - Add, view, update, and delete students
  - View and edit student profiles
- 📚 **Course Management**
  - Add/delete courses
  - View enrolled students per course
- 🏢 **Department Management**
  - Create and manage academic departments
- 🔄 **Enrollment System**
  - Enroll/withdraw students from courses
- 🎨 **Modern UI**
  - CustomTkinter-based elegant interface
  - Icon-driven design

---

## 📸 Screenshots


![image](https://github.com/user-attachments/assets/08aa00ee-05b8-4e94-98e3-1e6caf36d37e)

![image](https://github.com/user-attachments/assets/a984d9aa-6433-43cd-9833-dc6c15f2d569)


![image](https://github.com/user-attachments/assets/40f32a30-808f-40f0-bed9-af7bb539ef5a)

![image](https://github.com/user-attachments/assets/b5fccaf1-9857-4629-b8ad-72986b6f4246)


![image](https://github.com/user-attachments/assets/07a442a8-1b76-47c0-b898-35e705105a2c)

![image](https://github.com/user-attachments/assets/6c3248d5-3c4c-4bae-8a7d-9a6ac975b2ff)


![image](https://github.com/user-attachments/assets/895e818a-a055-4c29-aa37-1ad8b3188a81)


![image](https://github.com/user-attachments/assets/3bb8e662-29dd-40c6-9274-1d102ad4213f)


![image](https://github.com/user-attachments/assets/0b5a14a6-3d16-4d9d-9c79-9e83338ce107)


![image](https://github.com/user-attachments/assets/dc1e45b6-8c67-417e-8935-e3738f8b7f57)


![image](https://github.com/user-attachments/assets/8c72e818-af44-4649-b811-197de78e04f7)

---

## ⚙️ Tech Stack

| Technology       | Usage                               |
|------------------|--------------------------------------|
| Python           | Application Logic                    |
| CustomTkinter    | Enhanced GUI design                  |
| Oracle DB        | Persistent backend database          |
| PIL (Pillow)     | Image handling for UI                |
| Logging Module   | Runtime error tracking/logging       |



---

## 📁 Project Structure

student-management-system/
│
├── Student_Project.py # Main application
├── Data.sql # SQL schema and seed data
├── Student.jpg # UI element
├── new1.png # Login background image
├── email-icon.png # Icon used in login form
├── password-icon.png # Icon used in login form
├── course.png # Course visual
├── enroll.png # Enroll visual
├── Readme.pdf # Supporting document
└── README.md # This file

```bash

---

## 🛠️ Setup Instructions

### 🔄 Prerequisites
```bash
- Python 3.8 or above
- Oracle Database (XE or full)
- Python packages: `oracledb`, `customtkinter`, `Pillow`
```

### ✅ Install Dependencies
```bash
pip install oracledb customtkinter pillow
```
🧬 Set Up the Database
Open Oracle SQL Developer or SQL*Plus

Execute the Data.sql file to create tables:
```bash
@Data.sql
```
🚀 Run the Application
```bash
python Student_Project.py
```

⚠️ Ensure the image assets (like new1.png, email-icon.png, etc.) are in the same directory as the .py file.

🔒 Default Credentials
##Email: rijja2310119@ssn.edu.in
##Password: Rijja

🤝 Contributions
Feel free to fork the project and submit a pull request with enhancements!
Follow the standard Git workflow:
```bash
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
```
##📜 License
This project is open-source and available under the MIT License.


