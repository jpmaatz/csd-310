from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list_info = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list_info:
    print("  Student ID: " + doc["student_id"] + " First Name: " + doc["first_name"] + " Last Name: " + doc["last_name"])

bilbo = students.find_one({"student_id": "1007","student_id": "1008","student_id": "1009"})

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + bilbo["student_id"] + " First Name: " + bilbo["first_name"] + " Last Name: " + bilbo["last_name"])

input("-- End of program, press any key to continue...")