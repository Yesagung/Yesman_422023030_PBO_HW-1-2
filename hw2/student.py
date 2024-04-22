from sisfo.User import User
# from courses import Course

class Student(User):
    def __init__(self, user_id, name, email, password, enrollment_id):
        super().__init__(user_id, name, email, password)
        self.Enrollment_ID = enrollment_id
        self.Courses = []
        self.Grades = []
        self.Absences = {}
        self.viewpayment = []
    
    def get_name(self):
        return self._name
    
    def Enroll_In_Course(self, course):
        self.Courses.append(course)
        course.add_student(self)

    def View_Course(self):
        print(f"{self._name} has class in: " )
        for course in self.Courses: 
           print(f"{course.name}")
        
    def View_Grade(self, course):
        grades = course.get_student_grades(self)
        self.Grades.extend(grades)  

    def record_attendance(self, student_name, date):
        print(f"Attendance recorded for {student_name} on {date}")

    def View_Schedule(self, course):
        schedule = course.get_schedule()
        print(schedule)

    def calculate_billing(self):
        total_billing = 0  
        return total_billing




