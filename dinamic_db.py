import postgres_conn


def create_student():
    student_id = input("enter student id")
    student_name = input("enter student first name")
    student_last_name = input("enter student last name")
    phone_number = input("enter phone number")
    email = input("enter email")
    return [student_id, student_name, student_last_name, phone_number, email]


student_info = create_student()
if not any(student_info):
    print("Please fill all fields")
    create_student()


postgres_conn.database_conn()
postgres_conn.POSTGRES_CURSOR.execute("INSERT INTO students (student_id, first_name, "
                                      "last_name,phone_number, email_adress) VALUES (%s,%s,%s,%s,%s)",(student_info[0],
                                                                                                       student_info[1],
                                                                                                       student_info[2],
                                                                                                       student_info[3],
                                                                                                       student_info[4]))







