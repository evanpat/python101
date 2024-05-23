import mysql.connector

class Student: 
  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age

# Establish a database connection
db_connection = mysql.connector.connect(
  host="localhost",  # or your database host
  user="root",
  passwd="abc123",
  database="studentdb",
  auth_plugin='mysql_native_password'
)

# Create a cursor object
cursor = db_connection.cursor(dictionary=True)

# Define the query
query = """select id, name, age from student"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Create Employee objects
students = []
for row in results:
    print(row)
    emp = Student(**row)
    #emp = Student(id=row["id"], name=row["name"], age=row["age"])
    students.append(emp)

# Close the cursor and connection
cursor.close()
db_connection.close()


for emp in students:
    print(f"Student ID:{emp.id} Name:{emp.name} Age:{emp.age}")

