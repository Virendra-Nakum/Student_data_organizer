print("Wlcome Student Data Organizer ")

students = []

while True :
    print()
    print("Select an option ")
    print("1 Add Student ")
    print("2 Display All Student ")
    print("3 Update Student Information ")
    print("4 Remove Student Data")
    print("5 Display Student Offered")
    print("6 Exit ")
    print()

    choice = int(input("Enter Your Choice:-"))

    if choice == 1 :
                 
                 id = int(input("Enter Student ID:-"))
                 name = input("Enter Student name:-")
                 age = int(input("Enter Student AGE:-"))
                 dob = input("Enter Date Of birth(YYYY-MM-DD):-")
                 subject = input("Enter Subject (comma - separate):-")
                 grade = input("Enter Grade :-")

                 student = (id,dob)
                 sett = set(subject.split(","))

                 data = {"name":name,
                         "age":age,
                         "grade":grade,
                         "info" : student,
                         "id" : id,
                         "subject":sett
                             }
                 students.append(data)
                 print("Student Added Successfully")

    elif choice == 2 :
                     
                     if len(students) != 0 :
                         for std in students :

                             print()
                             print  (f"Student ID: {std["info"][0]}| Name: {std["name"]}| Age: {std["age"]}| Grade: {std["grade"]}| Subjects: {std["subject"]}| DOB: {std["info"][1]}")
                             print()

                     else:
                        print("Student Data Not Found ")

                            
    elif choice == 3 :
                    print()
                    id = int(input("Enter Student ID:-"))
                    for std in students :
                        if std["info"][0] == id :
                            while True :
                                print("1 Update Name")
                                print("2 Update Age ")
                                print("3 Update Subject")
                                print("4 Update Grade")
                                print("5 Stop Update ")

                                ch = int(input("Enter Your Choice:-"))

                                if ch == 1 :
                                    name = input("New Name:-")
                                    std["name"]= name

                                elif ch == 2 :
                                    age = int(input("Update Age:-"))
                                    std["age"] = age

                                elif ch == 3 :
                                    sub = input("New Subjects:-")
                                    v = set(subject.split(","))
                                    std["subject"] = sub

                                elif ch == 4 :
                                    grade = input("Update Grade:-")
                                    std["grade"]= grade

                                elif ch == 5 :
                                    print("Stop Updating ")
                                    break
                                else :
                                    print("Enter Valid Choice")
              
                    else :
                        print("Student Data Not Found ")


    elif choice == 4 :
                    print()
                    id = int(input("Enter Student ID:-"))
                    for std in students :
                        if std["info"][0] == id :
                            students.remove(std)
                            print("Student Remove Successfully ! ")

 
          
    elif choice == 5 :
    
        a = set()

        for std in students :
            for sub in std["subject"] :
                a.add(sub)
        print()
        for s in a:
            print(s)

                                    
    elif choice == 6 :
             
                    print("Thank You For Using Student Data Organizer Project ! ")
                    break
                
    else:
                   print("Enter Valid Choice ! ")

                
                                     
         
