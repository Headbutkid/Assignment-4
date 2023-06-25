#Author: Devin Robinson 2022000425
#Pledge of honor: This is my work, always 100% owned because that's me. 
#Purpose: This code is designed to bring up a small interface for a easy accessable database user-interface to show a table and the records.
    
import pyodbc

print("What do you want to do? (A, B, C OR D)")
print("A- diplay all, B- display growth, C- display by date or D- range of dates")

choice = input()

def connect_to_db():
    pass

def print_all_records():
    pass

def print_positive_growth():
    pass

def record_by_date():
    pass

def count_companies_between_dates():
    pass

if (choice == 'A'):

    print_all_records()

elif (choice == 'B'):

    print_positive_growth()

elif (choice == 'C'):

    record_by_date()

else: count_companies_between_dates()




