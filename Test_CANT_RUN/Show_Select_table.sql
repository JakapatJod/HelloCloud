SELECT students.student_id , students.f_name 
, students.l_name , subjects.subject_id , subjects.subject_name
, registrations.grade , teachers.f_name , teachers.l_name
 FROM students
join registrations 
    on students.student_id = registrations.student_id
join subjects
    on registrations.subject_id = subjects.subject_id
join teachers
    on subjects.teacher_id = teachers.teacher_id
;