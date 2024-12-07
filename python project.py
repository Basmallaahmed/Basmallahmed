import csv
import os
import re

CSV_FILE = 'employees.csv'

class Employee:
    def __init__(self, id, name, position, salary, email):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def to_list(self):
        return [self.id, self.name, self.position, self.salary, self.email]

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"


class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load_from_csv()

    def load_from_csv(self):
        if not os.path.exists(CSV_FILE):
            return
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    self.employees.append(Employee(*row))

    def save_to_csv(self):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            for employee in self.employees:
                writer.writerow(employee.to_list())

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email)

    def validate_salary(self, salary):
        return salary.isdigit() and int(salary) > 0

    def add_employee(self):
        id = input("Enter Employee ID ")
        name = input("Enter Name ")
        position = input("Enter Position ")

        while True:
            salary = input("Enter Salary")
            if self.validate_salary(salary):
                break
            else:
                print("Invalid salary.enter numeric value")

        while True:
            email = input("Enter Email ")
            if self.validate_email(email):
                break
            else:
                print("Invalid email .enter a valid email")

        self.employees.append(Employee(id, name, position, salary, email))
        self.save_to_csv()
        print("Employee added successfully")

    def update_employee(self):
        id = input("Enter Employee ID to update")
        for emp in self.employees:
            if emp.id == id:
                print("Leave blank")

                emp.name = input(f"Enter Name ({emp.name})") or emp.name
                emp.position = input(f"Enter Position ({emp.position}) ") or emp.position

                while True:
                    salary_input = input(f"Enter Salary ({emp.salary}) ")
                    if not salary_input:
                        break
                    if self.validate_salary(salary_input):
                        emp.salary = salary_input
                        break
                    else:
                        print("Invalid salary.enter numeric value")

                while True:
                    email_input = input(f"Enter Email ({emp.email}) ")
                    if not email_input:
                        break
                    if self.validate_email(email_input):
                        emp.email = email_input
                        break
                    else:
                        print("Invalid email.enter a valid email")

                self.save_to_csv()
                print("Employee updated successfully")
                return

        print("not found")

    def view_employees(self):
        if not self.employees:
            print("No employees")
            return
        for emp in self.employees:
            print(emp)

    def delete_employee(self):
        id = input("Enter Employee ID to delete ")
        for i, emp in enumerate(self.employees):
            if emp.id == id:
                del self.employees[i]
                self.save_to_csv()
                print("Employee deleted successfully")
                return
        print("Employee not found.")

    def search_employee(self):
        id = input("Enter Employee ID to search ")
        for emp in self.employees:
            if emp.id == id:
                print(emp)
                return
        print("not found")


def main():
    manager = EmployeeManager()
    while True:
        print("\n*** Employee Data Management System ***")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")
        choice = input("Select from (1-6)")

        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            manager.update_employee()
        elif choice == '4':
            manager.delete_employee()
        elif choice == '5':
            manager.search_employee()
        elif choice == '6':
            print("Exit")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
