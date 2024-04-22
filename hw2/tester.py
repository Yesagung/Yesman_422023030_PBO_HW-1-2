from admin import Admin
from courses import Course
from attendance import Attendance
from grade import Grade


def main():
    admin = Admin("A1", "Chelsea", "Chelsea@si.ukrida.ac.id", "adminpass")
    print("\nAdmin Name:", admin.get_name())
    print("admin provides payment information to students")
    print("\n")

    student = admin.create_user_account("student", "Student", "Yesman", "Yesman@si.ukrida.ac.id", "studentpass", "E1234")
    professor = admin.create_user_account("professor", "Professor", "Hendrik", "hendrik@ukrida.ac.id", "professorpass", "F1212")
    superadmin = admin.create_user_account("superadmin", "SuperAdmin", "Tubagus", "tubagus@ukrida.ac.id", "superadminpass", "S111")
    for user in [student, professor, superadmin]:
        if user:
            print(f"User {user.get_user_id()} can log in: {user.login(user._email, user._password)}")
            

    print("\nSuperAdmin Name:", superadmin.get_name())
    print("Superadmin can provide Technical support provided.")
    print("Superadmin can perform System maintenance performed.")
    
    dsp_course = Course("siwp1001", "Algorithma", "Introduction to programming and algorithms fundamental")
    pbo_course = Course("siwp2005", "PBO", "Object-oriented programming")

    professor.teach_course(dsp_course)
    professor.teach_course(pbo_course)

    print("\nProfessor Name:", professor.get_name())
    print("Professor's Courses Taught:")
    if hasattr(professor, 'View_Course'):
        professor.View_Course()
    else:
        for course in professor.Courses_Taught:
            print(f"{course.course_id} - {course.name}")
    print("\n")

    print("Student Name:", student.get_name())
    student.Enroll_In_Course(dsp_course)
    student.Enroll_In_Course(pbo_course)
    student.View_Course()

    print("\nStudent Billing Information:")
    print(admin.get_student_billing(student))
    print("\n")
    
    print("View Absences:")
    attendance_yesman = Attendance(student.get_user_id(), dsp_course.course_id, [])

    attendance_yesman.Record_Absence("2024-04-15")
    attendance_yesman.Record_Absence("2024-04-18")
    attendance_yesman.Record_Absence("2024-04-22")

    attendance_percentage_yesman = attendance_yesman.Calculate_Attendance_Rate(total_classes=25)

    print("Attendance Record for Yesman:")
    print("Dates Absent:", attendance_yesman.Dates_Absent)
    print("Attendance Percentage for Yesman:", attendance_percentage_yesman)
    print("\n")

    print("View Grades:")
    grade_yesman_dsp = Grade(student.get_user_id(), dsp_course.course_id, 85)
    grade_yesman_pbo = Grade(student.get_user_id(), pbo_course.course_id, 90)
    grade_yesman_dsp.Update_Grade(80)
    grade_yesman_pbo.Update_Grade(95)

    print("grades uploaded by lecturers for Yesman:")
    print(f"DSP: {grade_yesman_dsp.Numeric_Score}")
    print(f"PBO: {grade_yesman_pbo.Numeric_Score}")
    print("\n")

if __name__ == "__main__":
    main()