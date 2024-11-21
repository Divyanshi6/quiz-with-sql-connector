# ALERT: FOR PROPER OUTPUT OF BELOW CODE TRY TO RUN IN TERMINAL OR IDLE

import random
import mysql.connector

# Database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="mysqldiv6114@", 
        database="quiz"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

users = []
passwords = []
quizzes = {
    'python': [
    {
        "question": "What is the output of the following code?\n\nx = [1, 2, 3, 4]\nprint(x[::-1])",
        "options": [ "[1, 2, 3, 4]","[4, 3, 2, 1]","Error","None"],
        "answer": "[4, 3, 2, 1]"
    },
    {
        "question": "Which of the following is a mutable data type in Python?",
        "options": ["Tuple","String","List","Integer"],
        "answer": "List"
    },
    {
        "question": "What is the correct way to create a function in Python?",
        "options": ["function myFunc():","def myFunc():","create myFunc():","def myFunc:"],
        "answer": "def myFunc():"
    },
    {
        "question": "What will be the output of the following code?\n\ndef add(x, y=5):\n    return x + y\nprint(add(3))",
        "options": [ "3", "5", "8", "Error"],
        "answer": "8"
    },
    {
        "question": "What is the purpose of the 'self' parameter in a class method?",
        "options": ["It refers to the instance of the class.","It refers to a global variable.","It refers to the class itself.","It is used to return a value."],
        "answer": "It refers to the instance of the class."
    },
    {
        "question": "What will be the output of the following code?\nx = [1, 2, 3]\nprint(len(x))",
        "options": ["3","2","1","Error"],
        "answer": "3"
    },
    {
        "question": "What does the 'lambda' keyword in Python define?",
        "options": ["A normal function","An anonymous function","A class","A module"],
        "answer": "An anonymous function"
    },
    {
        "question": "What will the following code print?\na = 5\nb = 10\na, b = b, a\nprint(a, b)",
        "options": ["5 10","10 5","Error","None"],
        "answer": "10 5"
    },
    {
        "question": "What is the output of the following code?\n\nprint(bool(0), bool(3.14), bool(-5))",
        "options": ["False True False","False True True","True False True","True True True"],
        "answer": "False True True"
    },
    {
        "question": "Which of the following will raise an error?",
        "options": ["x = 10/2","x = 10//2","x = 10 % 3","x = 10 ++ 2"],
        "answer": "x = 10 ++ 2"
    }
],
    'oopm': [
    {
        "question": "What are the four pillars of Object-Oriented Programming?",
        "options": ["Inheritance, Encapsulation, Abstraction, Polymorphism","Class, Object, Method, Constructor",    "Data hiding, Overloading, Overriding, Interfaces"],
        "answer": "Inheritance, Encapsulation, Abstraction, Polymorphism"
    },
    {
        "question": "What is the difference between an abstract class and an interface?",
        "options": ["An abstract class can have both concrete and abstract methods, while an interface can only have abstract methods.","Interfaces support multiple inheritance, but abstract classes do not.","Both (a) and (b)"],
        "answer": "Both (a) and (b)"
    },
    {
        "question": "What is method overriding in OOP?",
        "options": ["Defining a method in a subclass with the same signature as in the parent class.","Defining multiple methods with the same name in the same class.","Changing the return type of a method in the subclass."],
        "answer": "Defining a method in a subclass with the same signature as in the parent class."
    },
    {
        "question": "What is polymorphism in OOP?",
        "options": ["The ability to take many forms, allowing objects of different classes to be treated as objects of a common superclass.","Creating multiple constructors in a class.","The process of creating objects."],
        "answer": "The ability to take many forms, allowing objects of different classes to be treated as objects of a common superclass.*"
    },
    {
        "question": "Which of the following best describes encapsulation in OOP?",
        "options": ["Bundling the data and methods that operate on the data into a single unit (class).","Using inheritance to reuse code.","The ability of a function to handle different data types."],
        "answer": "Bundling the data and methods that operate on the data into a single unit (class)."
    },
    {
        "question": "What is the purpose of a constructor in object-oriented programming?",
        "options": ["To initialize the state of an object.","To destroy an object.","To implement polymorphism." ],
        "answer": "To initialize the state of an object."
    },
    {
        "question": "What is the difference between `==` and `===` in programming languages like JavaScript?",
        "options": ["`==` compares values, while `===` compares both values and types.","`==` compares memory addresses, while `===` compares values.","Both `==` and `===` work the same in JavaScript."],
        "answer": "`==` compares values, while `===` compares both values and types."
    },
    {
        "question": "What is recursion in programming?",
        "options": ["A process in which a function calls itself.","A loop that runs indefinitely.","A function that is called multiple times in a program."],
        "answer": "A process in which a function calls itself."
    },
    {
        "question": "What is a stack overflow error?",
        "options": ["When too many recursive calls are made, causing the stack memory to exceed its limit.","When a program has too many variables.","When a loop runs indefinitely."],
        "answer": "When too many recursive calls are made, causing the stack memory to exceed its limit."
    },
    {
        "question": "What is the purpose of exception handling in programming?",
        "options": ["To handle runtime errors and prevent the program from crashing.","To handle compilation errors.","To handle syntax errors."],
        "answer": "To handle runtime errors and prevent the program from crashing."
    }
],
    'dbms': [
    {
        "question": "What is a Database Management System (DBMS)?",
        "options": ["A collection of interrelated data","A set of programs to access and manage databases","Both A and B","None of the above"],
        "answer": "Both A and B"
    },
    {
        "question": "Which of the following is a primary key?",
        "options": ["A field that can have multiple values","A field that uniquely identifies each record","A field that allows duplicates","A field with missing values"],
        "answer": "A field that uniquely identifies each record"
    },
    {
        "question": "Which SQL command is used to remove a table from the database?",
        "options": ["DELETE","DROP","REMOVE","CLEAR"],
        "answer": "DROP"
    },
    {
        "question": "What does ACID stand for in the context of a transaction in DBMS?",
        "options": ["Atomicity, Consistency, Isolation, Durability","Accuracy, Consistency, Information, Durability","Availability, Concurrency, Isolation, Durability","Atomicity, Communication, Isolation, Data"],
        "answer": "Atomicity, Consistency, Isolation, Durability"
    },
    {
        "question": "What is a foreign key?",
        "options": ["A key used to uniquely identify a table","A key that is a primary key in another table","A key used for encryption","A key that contains NULL values"],
        "answer": "A key that is a primary key in another table"
    },
    {
        "question": "Which of the following is NOT a type of database model?",
        "options": ["Hierarchical","Network","Relational","Sequential"],
        "answer": "Sequential"
    },
    {
        "question": "Which normal form eliminates partial dependency?",
        "options": ["First Normal Form (1NF)","Second Normal Form (2NF)","Third Normal Form (3NF)","Boyce-Codd Normal Form (BCNF)"],
        "answer": "Second Normal Form (2NF)"
    },
    {
        "question": "In SQL, which command is used to retrieve data from a database?",
        "options": ["INSERT","UPDATE","SELECT","DELETE"],
        "answer": "SELECT"
    },
    {
        "question": "What is a JOIN in SQL?",
        "options": ["A command to combine records from two or more tables","A command to delete records","A command to update records","A command to insert new records"],
        "answer": "A command to combine records from two or more tables"
    },
    {
        "question": "Which of the following ensures that no duplicate rows are returned in SQL?",
        "options": ["DISTINCT","UNIQUE","PRIMARY","GROUP BY"],
        "answer": "DISTINCT"
    }
  ]
}

def username_checker(username):
    if not (6 <= len(username) <= 15):
        return "NOT MATCHED: Username must be between 6 and 15 characters long."

    lower = upper = digit = spchar = 0

    for char in username:
        if char.isalpha():
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
        elif char.isdigit():
            digit += 1
        elif char in "!@#$%^&*()-_+=<>?":
            spchar += 1
        else:
            return "NOT MATCHED: Username can only contain letters, numbers, and special characters (!@#$%^&*()-_+=<>?)."

    if lower > 0 and upper > 0 and digit > 0 and spchar > 0:
        return "MATCHED: Username is VALID ^_^"

    criteria = []
    if lower == 0:
        criteria.append("at least one lowercase letter")
    if upper == 0:
        criteria.append("at least one uppercase letter")
    if digit == 0:
        criteria.append("at least one digit")
    if spchar == 0:
        criteria.append("at least one special character")

    return "NOT MATCHED CRITERIA: Username must contain " + ", ".join(criteria) + "."

def password_checker(password):
    if not (8 <= len(password) <= 20):
        return "NOT MATCHED: Password must be between 8 and 20 characters long."
    
    lower = upper = digit = spchar = 0

    for char in password:
        if char.isalpha():
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
        elif char.isdigit():
            digit += 1
        else:
            spchar += 1

    if lower > 0 and upper > 0 and digit > 0 and spchar > 0:
        return "MATCHED: Password is STRONG ^=^"
    
    criteria = []
    if lower == 0:
        criteria.append("at least one lowercase letter")
    if upper == 0:
        criteria.append("at least one uppercase letter")
    if digit == 0:
        criteria.append("at least one digit")
    if spchar == 0:
        criteria.append("at least one special character")

    return "NOT MATCHED CRITERIA: Password must contain " + ", ".join(criteria) + "."

def clear_screen():
    print("\033[H\033[J")

def register():
    clear_screen()
    print("^^^^^^^^^^^^^^^^^^^^^^^^=== REGISTER ===^^^^^^^^^^^^^^^^^^^^^^^^")
    username = input("Enter username: ")
    
    cursor.execute("SELECT username FROM detail WHERE username = %s", (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose a different one.")
        return

    validation_result = username_checker(username)
    if validation_result.startswith("NOT MATCHED"):
        print(validation_result)  
        return
    
    password = input("Enter password: ")
    validation_result = password_checker(password)
    if validation_result.startswith("NOT MATCHED"):
        print(validation_result)  
        return

    cursor.execute("INSERT INTO detail (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    print("Registration successful!")

def login():
    clear_screen()
    print("^^^^^^^^^^^^^^^^^^^^^^^^=== LOGIN ===^^^^^^^^^^^^^^^^^^^^^^^^")
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM detail WHERE username = %s AND password = %s", (username, password))
    if cursor.fetchone():
        print("Login successful!")
        subject = input("Enter the subject for the quiz: ").lower()
        take_quiz(subject, username)
    else:
        print("Invalid username or password.")

def take_quiz(subject, username):
    clear_screen()
    print(f"\n--- {subject} Quiz ---")
    questions = random.sample(quizzes[subject], 5)
    score = 0
    for idx, q in enumerate(questions, 1):
        print(f"\nQ{idx}: {q['question']}")
        for i, option in enumerate(q["options"], 1):
            print(f"{i}. {option}")
        while True:
            try:
                answer = int(input("Enter your answer (1-4): "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Invalid input. Choose between 1 and 4.")
            except ValueError:
                print("Please enter a number.")
        if q["options"][answer - 1] == q["answer"]:
            score += 1
    print(f"\nYou scored {score} out of 5!")

    cursor.execute("UPDATE detail SET score = %s, subject = %s WHERE username = %s", (score, subject, username))
    conn.commit()

def main_menu():
    while True:
        clear_screen()
        print("^^^^^^^^^^^^^^^^^^^^^^^^=== MAIN MENU ===^^^^^^^^^^^^^^^^^^^^^^^^")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Thank you for using the Quiz System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

cursor.close()
conn.close()
