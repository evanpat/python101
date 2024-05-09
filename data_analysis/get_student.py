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
cursor = db_connection.cursor()

# Define the query
query = "SELECT * FROM student"

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Iterate over the results and print them
for row in results:
  print(row)

# Close the cursor and connection
cursor.close()
db_connection.close()