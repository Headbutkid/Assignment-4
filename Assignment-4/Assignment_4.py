#Author: Devin Robinson 2022000425
#Pledge of honor: This is my work, always 100% owned because that's me. 
#Purpose: This code is designed to bring up a small interface for a easy accessable database user-interface to show a table and the records.
    
import pyodbc

print("What do you want to do? (A, B, C OR D)")
print("A - diplay all, B - display growth, C - display by date or D - range of dates")

choice = input()

def connect_to_db():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022000425\Downloads\Company-202200425.accdb;')
    cursor = conn.cursor()
    cursor.execute("SELECT * from Company_Data")

   

def print_all_records():
   conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022000425\Downloads\Company-202200425.accdb;')
   cursor = conn.cursor()
   cursor.execute("SELECT * from Company_Data")

   print(f'{"Company":<20}{"Industry":<20}{"Year revenue":<20}{"Revenue Growth":<20}{"Employees":<20}{"Found date":<15}{"Headquarter":<0}')
   print(f'{ "_"*130:<75}')

   for row in cursor.fetchall():
       record = f'{row.Company_Name:<20}{row.Industry:<20}{row.Year_revenue:<25}{row.Revenue_growth:<20}{row.Number_of_employees:<15}{row.Company_found_date:<15}{row.Headquarter:<0}'

       print(record)

def print_positive_growth():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022000425\Downloads\Company-202200425.accdb;')
    cursor = conn.cursor()
    cursor.execute("SELECT * from Company_Data WHERE Revenue_Growth >0")

    print(f'{"Company":<20}{"Revenue Growth":<20}')
    print(f'{ "_"*30:<75}')

    for row in cursor.fetchall():
       record = f'{row.Company_Name:<20}{row.Revenue_growth:<20}'

       print(record)

def record_by_date():
    
   conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022000425\Downloads\Company-202200425.accdb;')
   cursor = conn.cursor()
   choice = input("Enter company date (dd mm yy): ")
   cursor.execute("SELECT * from Company_Data WHERE Company_found_date = ?", (choice,))
   row = cursor.fetchall()
   while row: 
        print(row)
        row = cursor.fetchall()


def count_companies_between_dates():
  conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\2022000425\Downloads\Company-202200425.accdb;')
  cursor = conn.cursor()
  start_date = input("Enter your starting date for the company (dd mm yy): ")
  end_date = input("Enter your end date for the company (dd mm yy): ")
  cursor.execute("SELECT * from Company_Data WHERE Company_found_date BETWEEN ? AND ?", (start_date, end_date))
  rows = cursor.fetchall()
  count = len(rows)
    
  print(f"The number of entries between {start_date} and {end_date} is: {count}")

if (choice == 'A'):

    print_all_records()

elif (choice == 'B'):

    print_positive_growth()

elif (choice == 'C'):

    record_by_date()
    

else: count_companies_between_dates()




