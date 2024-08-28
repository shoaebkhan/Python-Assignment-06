class Student:
    name:str
    id:int

    def __init__(self, n, i):
        self.name=n
        self.id=i
#check whether student name is duplicate or not
def isDuplicate(name, students_list):
    if any(name==n for _,n in students_list):
        return True
    return False
# manage student database    
def manage_student_database():
    students_list:list=[]
    i:int=1
    while True:   
        name=input("Please enter the student's name (or type 'stop' to finish):")
        if name.lower()=="stop":
            break
        elif isDuplicate(name, students_list)==True:
            print(f"Duplicate name found: {name} already exists in the database.")
        else:
            s=Student(name, i)
            i+=1
            students_list.append((s.id, s.name))
    print(f"Complete List of Students (Tuples):\n {students_list}")
    print(f"List of Students with IDs:")
    
    for x in students_list:
        print(f"ID: {x[0]}, Name: {x[1]}")
    
    print(f"Total number of students are {len(students_list)}")
    total_name_length = sum(len(name) for _, name in students_list)
    print(f"Total length of all student names combined: {total_name_length}")
    
    if students_list:
        longest_name_student = max(students_list, key=lambda s: len(s[1]))
        shortest_name_student = min(students_list, key=lambda s: len(s[1]))

        print(f"Student with the longest name: {longest_name_student[1]} (ID: {longest_name_student[0]})")
        print(f"Student with the shortest name: {shortest_name_student[1]} (ID: {shortest_name_student[0]})")


manage_student_database()