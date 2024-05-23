# Import necessary modules
from pymysql import connect
#import xlwt
import pandas.io.sql as sql

# Connect to MySQL
con = connect(  
  host="localhost",
  user="root",
  password="abc123",
  database="studentdb"
  )

# Read data from MySQL into a DataFrame
query = "SELECT * FROM student"
df = sql.read_sql(query, con)

# Print the data frame (optional)
print(df)

# Export the data to an Excel sheet (ds.xls)
df.to_excel('ds.xlsx')