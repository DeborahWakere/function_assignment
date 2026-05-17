name = input("Enter Student name: ")
backend_marks = int(input("Enter Backend marks: "))
frontend_marks = int(input("Enter Frontend marks: "))
design_marks = int(input("Enter Design marks: "))

def average (backend_marks, frontend_marks, design_marks) :
    calculate = round(((backend_marks + frontend_marks + design_marks) / 3),2)
    return calculate

def grade (average):
    grademark = average (backend_marks, frontend_marks, design_marks) 
    properGradeMark = round(grademark,0)
    if properGradeMark >= 80 :
        return "A"
    elif properGradeMark >= 70 and properGradeMark <= 79:
        return "B"
    elif properGradeMark >= 60 and properGradeMark <= 69:
        return "C"
    elif properGradeMark >= 50 and properGradeMark <= 59:
        return "D"
    else :
        return "E"

average (backend_marks, frontend_marks, design_marks)
grade(average)

def student_report (name, backend_marks, frontend_marks, design_marks, average, grade):
    output = {
        'name':name,
        'Backend': backend_marks,
        'Frontend': frontend_marks, 
        'Design': design_marks,
        'average': average (backend_marks, frontend_marks, design_marks) ,
        'Grade': grade(average)
        }
    return output 

print(student_report (name, backend_marks, frontend_marks, design_marks, average, grade))