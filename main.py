print("Welcome Student Data Organizer")

students = []

while True:
    print()
    print("Select an option")
    print("1. Add Student")
    print("2. Display All Student")
    print("3. Update Student Information")
    print("4. Remove Student Data")
    print("5. Display Student Offered")
    print("6. Exit")
    print()

    choice = int(input("Enter Your Choice:- "))
 
    if choice == 1:
        id = int(input("Enter Student ID:- "))

        for std in students:
            if std["id"] == id:
                print("Student ID Already Exists!")
                break

        else:
            name = input("Enter Student Name:- ")
            age = int(input("Enter Student Age:- "))
            dob = input("Enter Date Of Birth (YYYY-MM-DD):- ")
            subject = input("Enter Subject (comma-separated):- ")
            grade = input("Enter Grade:- ")

            student = (id, dob)

            sett = set(subject.split(","))

            data = {
                "name": name,
                "age": age,
                "grade": grade,
                "info": student,
                "id": id,
                "subject": sett
            }

            students.append(data)

            print("Student Added Successfully!")

    elif choice == 2:

        if len(students) != 0:

            for std in students:
                print(f"Student ID: {std['info'][0]} | Student Name: {std['name']} | Age: {std['age']} | Grade: {std['grade']} | Subjects: {std['subject']} | DOB: {std['info'][1]}")
 
                print()
        else:
            print("Student Data Not Found!")
 
    elif choice == 3:

        print()

        id = int(input("Enter Student ID:- "))

        for std in students:

            if std["id"] == id:
                while True:

                    print()
                    print("1. Update Name")
                    print("2. Update Age")
                    print("3. Update Subject")
                    print("4. Update Grade")
                    print("5. Stop Update")
                    print()

                    ch = int(input("Enter Your Choice:- "))

                    if ch == 1:

                        name = input("New Name:- ")
                        std["name"] = name
                        print("Name Updated Successfully!")

                    elif ch == 2:

                        age = int(input("Update Age:- "))
                        std["age"] = age
                        print("Age Updated Successfully!")

                    elif ch == 3:

                        sub = input("New Subjects (comma-separated):- ")
                        v = set(sub.split(","))
                        std["subject"] = v
                        print("Subjects Updated Successfully!")

                    elif ch == 4:

                        grade = input("Update Grade:- ")
                        std["grade"] = grade
                        print("Grade Updated Successfully!")

                    elif ch == 5:
                        print("Stop Updating")
                        break

                    else:
                        print("Enter Valid Choice!")

                break
        else:
            print("Student Data Not Found!")



    elif choice == 4:

        id = int(input("Enter Student ID:- "))

        for std in students:

            if std["id"] == id:
                students.remove(std)
                print("Student Remove Successfully!")
                break

        else:
            print("Student Data Not Found!")

    elif choice == 5:

        a = set()
        for std in students:
            for sub in std["subject"]:

                a.add(sub.strip())

        print()

        if len(a) != 0:

            print("Subjects Offered:")
            for s in a:
                print(s)

        else:
            print("No Subjects Found!")

    elif choice == 6:

        print()
        print("Thank You For Using Student Data Organizer Project!")
        break

    else:

        print("Enter Valid Choice!")
