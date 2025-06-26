from fastapi import FastAPI
from schemas import Student,Classinfo,registrationrequest
from models import student_db,classes_db,registrations_db

app = FastAPI()


@app.get("/")
def read_root():
    return{"message": "Welcome to student-class"}

@app.post("/students")
def create_student(student:Student):
    student_db.append(student)
    return{"message": "Student added succesfully" , "student" : student}

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    if 0 <= student_id < len(student_db):
        student_db[student_id] = updated_student
        return {"message":"Student updated successfully","student": updated_student}
    else:
        return{"error" : "Student not found"}
    

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if 0 <= student_id < len(student_db):
        deleted_student = student_db.pop(student_id)
        return {"message" :"Student deleated successfully","student": deleted_student}
    else:
        return{"error":"Student not found"}
    
    
@app.post("/classes")
def create_class(class_info:Classinfo):
    classes_db.append(class_info)
    return{"message" : "Class created successfully", "class": class_info}
    
@app.put("/classes/{class_id}")
def update_class(class_id :int , updated_class: Classinfo):
    if 0 <= class_id < len(classes_db):
        classes_db[class_id] = updated_class
        return{"message":"Class successfully updated","class": updated_class}
    else:
        return{"error":"Class not found"}
    
    
@app.delete("/classes/{class_id}")
def delete_class(class_id:int):
    if 0 <= class_id < len(classes_db):
        deleted_class = classes_db.pop(class_id)
        return{"message":"Class is deleted successfully","class" : deleted_class}   
    else:
        return{"error":"Class not found"} 
    
@app.post("/register")
def register_student(registration: registrationrequest):
    class_id = registration.class_id
    student_id = registration.student_id
    
    if class_id > len(classes_db) and student_id > len(student_db):
        return{"error":"Invalid class or student ID"}
    
    if class_id not in registrations_db:
        registrations_db[class_id] = []
        
    if student_id not in registrations_db[class_id]:
        registrations_db[class_id].append(student_id)
        return{"message":"Student registerd Succesfully"}
    else:
        return{"error":"Student is alreday registerd in this class"}       
    
    
@app.get("/classes/{class_id}/students")
def get_students_in_class(class_id: int):
    if class_id not in registrations_db:
        return{"error":"No student in class or class does not exist"}
    student_ids=registrations_db[class_id]
    students = []
    for sid in student_ids:
        if sid< len(student_db):
            students.append(student_db[sid])
    return{"class_id": class_id, "students": students}        