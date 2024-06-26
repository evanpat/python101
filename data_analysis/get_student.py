import mysql.connector

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
query = """select CONCAT(class.type, '.', class.ranking, class.code) class_name, subject.subjectName
from class
left join class_subject on class.Id = class_subject.classId
left join subject on subject.Id = class_subject.subjectId"""

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Iterate over the results and print them
for row in results:
  print(row)
  #print(row["class_name"],",", row["subjectName"])
  
#oneresult = cursor.fetchone()
#print(oneresult)

# Close the cursor and connection
cursor.close()
db_connection.close()