from pydantic import BaseModel
from datetime import date

class Student(BaseModel):
    first_name: str
    last_name:str
    middle_name:str | None = None
    age: int
    city:str
    
class Classinfo(BaseModel):
    class_name: str
    description: str
    start_date : date
    end_date: date
    hours: int    
    
class registrationrequest(BaseModel):
    
    class_id : int   
    student_id :int 