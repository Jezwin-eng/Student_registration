from typing import List
from schemas import Student,Classinfo

student_db:List[Student] = []

classes_db:List[Classinfo] = []

registrations_db: dict[int,list[int]]={}

