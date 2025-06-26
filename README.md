
# 🧑‍🎓 Student-Class Registration API

A RESTful API for managing students, classes, and registrations — built with **FastAPI** and deployed via **Uvicorn**. This project is part of a cloud computing assignment requiring full CRUD operations and deployment integration with GitHub and Azure.

---

## 🚀 Features

✅ Capture and manage student details  
✅ Create, update, and delete class information  
✅ Register students to classes  
✅ Retrieve list of students in a class  
✅ Fully tested with Postman  
✅ Ready for deployment to Azure using GitHub Actions

---

## 🛠️ Technologies Used

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Git & GitHub**
- (Optional) Azure App Service

---

## 📦 Installation & Running Locally

1. **Clone the repo**

```bash
git clone [https://github.com/Jezwin-eng/Student_registration.git]
cd student-class-api
```

2. **Create and activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the API**

```bash
uvicorn main:app --reload
```

5. **Visit Swagger docs**

Open your browser at:  
```
http://127.0.0.1:8000/docs
```

---

## 📬 API Endpoints

| Operation                    | Method | Endpoint                          |
|-----------------------------|--------|-----------------------------------|
| Add Student                 | POST   | `/students`                       |
| Update Student              | PUT    | `/students/{student_id}`          |
| Delete Student              | DELETE | `/students/{student_id}`          |
| Create Class                | POST   | `/classes`                        |
| Update Class                | PUT    | `/classes/{class_id}`             |
| Delete Class                | DELETE | `/classes/{class_id}`             |
| Register Student to Class   | POST   | `/register`                       |
| Get Students in a Class     | GET    | `/classes/{class_id}/students`    |

---

## 🧪 Testing

All endpoints tested using **Postman**. Screenshots are available in the `screenshots/` folder (if included) or attached with submission.

---

## 📄 Project Requirements

This project fulfills the following cloud computing assignment requirements:

- [x] 8 RESTful operations
- [x] API tested via Postman
- [x] Code pushed to GitHub
- [x] Screenshots submitted
- [ ] (Optional) GitHub Actions deployment to Azure

---

## 👨‍💻 Author

**Jezwin Ano**  
GitHub: [@Jezwin-eng](https://github.com/Jezwin-eng)

---

## 📜 License

MIT License – Use it freely for learning and academic purposes.
