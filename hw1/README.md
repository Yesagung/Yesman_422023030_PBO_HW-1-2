# **Requirement analysis**
### **Functionality**
- **Capability**: The system should support different user roles (students, professors, admin, superadmin) with role-specific functionalities. For students, this might include viewing grades and course materials. Professors would need to post grades and course materials, admins oversee system operations, operators handle technical issues, and parents access student progress.
- **Reusability**: Components like user authentication, data retrieval, and notification services should be designed for reuse across different modules.
- **Security**: User authentication, data encryption, and access control are essential. Sensitive data like student records and grades must be securely managed.

### **Usability**
- **Human Factors**: The interface should be intuitive for all user types, accommodating varied tech proficiency. It should have a responsive design for different devices.
- **Consistency**: The system should maintain a consistent look and feel across all modules and user roles.
- **Documentation**: Comprehensive user guides for each user role, FAQs, and system manuals are necessary.
### **Reliability**
- **Availability**: The system should be available 24/7, with minimal downtime.
- **Failure Rate & Duration**: It should have a low failure rate. Any system failures should be resolved quickly.
- **Predictability**: System behavior in response to user actions should be predictable and consistent.
### **Performance**
- **Speed**: Fast response times for user queries and actions.
- **Efficiency**: Optimized for minimal resource consumption without compromising functionality.
- **Resource Consumption**: Should be optimized to work smoothly on standard institutional hardware.
- **Scalability**: Capable of handling an increasing number of users and data volume.

### **Supportability**
- **Testability**: The system should be easily testable to find and fix bugs.
- **Extensibility**: It should be designed to allow easy updates and additions of new features.
- **Serviceability**: Problems within the system should be easy to diagnose and fix.
- **Configurability**: Allow easy configuration of features like user roles, permissions, and system settings.



# **UseCase  & User Story**
## User Story
**Portal/Sisfo**
= Sebagai seorang mahasiswa Ukrida, saya ingin saat mengakses portal/sisfo jadi lebih mudah dan efesien agar saya dapat tetap terinformasi selalu.
## UseCase
**User Roles (Actor)**
- Student (mahasiswa)
- Professor (Dosen)
- Super Admin
- Admin (administrasi)
![Usecase PBO (6)](https://github.com/Yesagung/Yesman_422023030_PBO_HW-1-2/assets/151461069/26437d0a-7329-47cd-b4ec-bedd86169731)




# **Class Diagram**
```mermaid
    classDiagram 
    class User {
    <<abstract>>
    +UserID
    +Password
    +Login()
    +Logout()
}

class Student {
    +EnrollmentID
    +CoursesList
    +GradesList
    +Absences
    +EnrollInCourse()
    +ViewGrades()
    +RecordAbsence()
    +ViewSchedule()
    +ViewPaymentBills()
}

class Professor {
    +FacultyID
    +CoursesTaught: List
    +UploadGrades()
    +MonitorAttendance()
    +UpdateSchedule()
}

class Admin {
    +AdminID  
    +ManageUserAccounts()
    +InformationBill()
}

class Super Admin {
    +OperatorID
    +ProvideTechnicalSupport()
    +MaintainSystem()
}

class Course {
    +CourseID
    +Name
    +Description
    +StudentsEnrolled: List
    +CourseMaterials: List
    +AddStudent()
    +RemoveStudent()
    +UpdateCourseMaterial()
}

class Payment {
    -PaymentID
    -Amount
    -Date
    +processPayment()
    +generateReceipt()
    +cancelPayment()
}

class Grade {
    +StudentID
    +CourseID
    +NumericScore
    +UpdateGrade()
}

class Attendance {
    +StudentID
    +CourseID
    +DatesAbsent
    +RecordAbsence()
    +CalculateAttendanceRate()
}

User <|-- Student
User <|-- Professor
User <|-- Admin 
User <|-- Super Admin 

Student "n" -- "n" Course : enrolls in >
Course "1" -- "n" Grade : has > 
Course "1" -- "n" Attendance : has >
Professor "1" -- "1" Course : teaches >
Student "n" -- "n" Payment : makes >
```



