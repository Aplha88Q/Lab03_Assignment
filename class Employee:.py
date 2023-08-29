class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = [
            Employee("161E90", "Raman", 41, 56000),
            Employee("161F91", "Himadri", 38, 67500),
            Employee("161F99", "Jaya", 51, 82100),
            Employee("171E20", "Tejas", 30, 55000),
            Employee("171G30", "Ajay", 45, 44000)
        ]
    
    def search_by_age(self, age):
        result = []
        for emp in self.employees:
            if emp.age == age:
                result.append(emp)
        return result
    
    def search_by_name(self, name):
        result = []
        for emp in self.employees:
            if name.lower() in emp.name.lower():
                result.append(emp)
        return result
    
    def search_by_salary(self, operator, salary):
        result = []
        for emp in self.employees:
            if operator == ">" and emp.salary > salary:
                result.append(emp)
            elif operator == ">=" and emp.salary >= salary:
                result.append(emp)
            elif operator == "<" and emp.salary < salary:
                result.append(emp)
            elif operator == "<=" and emp.salary <= salary:
                result.append(emp)
        return result

def main():
    db = EmployeeDatabase()
    
    while True:
        print("Search Options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            age = int(input("Enter age: "))
            results = db.search_by_age(age)
            if results:
                print("Search Results:")
                for emp in results:
                    print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
            else:
                print("No results found.")
        
        elif choice == "2":
            name = input("Enter name: ")
            results = db.search_by_name(name)
            if results:
                print("Search Results:")
                for emp in results:
                    print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
            else:
                print("No results found.")
        
        elif choice == "3":
            operator = input("Enter salary operator (> < <= >=): ")
            salary = int(input("Enter salary: "))
            results = db.search_by_salary(operator, salary)
            if results:
                print("Search Results:")
                for emp in results:
                    print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
            else:
                print("No results found.")
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
