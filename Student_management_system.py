students = []

while True:
    print("\n=== Student Management ===")
    print("1. Add student")
    print("2. View students")
    print("3. Delete")
    print("4. Update")
    print("5. Search")
    print("6. Exit")

    choice = input("Enter your choice: ")
    print("You Selected:", choice)

    if choice == "1":

        name = input("Enter student name: ")
        age = input("Enter your age: ")
        course = input("Enter course: ")

        student = {
            "name": name,
            "age": age,
            "course": course
        }

        students.append(student)

        print("\nStudent added successfully!")

    elif choice == "2":
        if len(students)==0:
            print("\nNo students found")

        print("\n===== Student Details =====")

        count=1
        for student in students:
            print(f"\nStudent {count}")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            count +=1
            print()

    elif choice == "3":
        if len(students) == 0:
            print("No students Found")

        else:
            count = 1
            for student in students:
                print(count,"-",student["name"])
                count +=1

            delete=int(input("Enter student number to delete: "))

        if delete >=1 and delete <= len(students):
         students.pop(delete -1)
         print("Deleted Succesfully..")
         
        else:
            print("Invalid student")

    elif choice == "4":
        if len(students) == 0:
            print("No students Found..")
        else:
            search=input("Enter student name to search :")
            found=False

            for student in students:
                if student["name"].lower() == search.lower():
                    print("student found")
                    student["name"] = input("Enter new Name :")
                    student["age"] = input("Enter new Age :")
                    student["course"] = input("Enter new Course :")

                    print("Student Updated Succesfully")
                    found=True
                    break

    elif choice =="5":
                if len(students) == 0:
                    print("No students found..")

                else:
                    search=input("Enter student name to search:")
                    found=False

                    for student in students:
                        if student["name"].lower() == search.lower():
                            
                            print("Name :",student["name"])
                            print("Age :",student["age"])
                            print("Course :",student["course"])
                            print("student found..")
                            found=True
                            break
                        

    elif choice =="6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
