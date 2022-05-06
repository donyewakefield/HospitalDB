import psycopg2

# Connect to your postgres DB
connection = psycopg2.connect(
database = "Hospital Database",
user = "postgres",
password = "Donyewakefield1999!"
)

# Open a cursor to perform database operations
cur = connection.cursor()

# Execute a query (obtain results of a view)
### This will be what a financial analyst will have displayed to them
cur.execute("SELECT * FROM employee_financials")

# Retrieve query results
records = cur.fetchall()

# showcase records from the View to the Financial Analyst
for r in records:
    print(f" {r[0]}, {r[1]}, {r[2]}, {r[3]}")

print(" ")
print(" ")

# Execute another query (give an employee a raise)
### HR will modify the database by increasing Sonic Hedgehogs salary by 8%

# what is the percentage
raise_percentage = (1.000) * 0.08

# obtain Sonic's current salary
cur.execute("SELECT salary FROM doctor WHERE doctor_id = 91234")
salary = cur.fetchone()

# convert Sonic's current salary returned as a tuple into a string
salary = str(salary)

# eliminate noisy chars to get only the dollar amount and convert to a float
official_salary = float((str(salary[10:-4])))

# calculate the raise for Sonic's salary
new_salary = official_salary + (official_salary * raise_percentage)

# convert that raised salary to a string (to be put into the query)
string_new_salary = str(new_salary)

# execute update DML statement by changing Sonic's current salary to the new one
cur.execute(f"UPDATE doctor SET salary = {string_new_salary} WHERE doctor_id = 91234")

# showcase sonic's new salary along with all other doctor's same salary
cur.execute("SELECT first_name, last_name, salary FROM doctor")
records2 = cur.fetchall()
for r2 in records2:
    print(f" {r2[0]}, {r2[1]}, {r2[2]} ")

# close the cursor
cur.close()

# close the connection
connection.close()
