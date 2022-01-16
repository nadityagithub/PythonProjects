import sqlite3

db_name = "students.db"

def connect_to_db():
	db_conn = sqlite3.connect(db_name)
	db_cursor = db_conn.cursor()
	print("Connected to DB.")
	return db_conn, db_cursor

def create_table(db_cursor):
	sql = "create table student(student_id integer, first_name text, last_name text, age integer, gpa real, class text)"
	db_cursor.execute(sql)
	print("Created Table.")

def drop_table(db_cursor):
	sql = "drop table if exists student"
	db_cursor.execute(sql)
	print("Dropped Table.")
def insert_row(db_cursor):
	sql = "insert into student (student_id, first_name, last_name, age, gpa, class) values (?, ?, ?, ?, ?, ?)"
	student_id = int(input("Enter your student_id (int): "))
	first_name = input("Enter your first name (str) : ")
	last_name = input("Enter your last name (str) : ")
	age = int(input("Enter your age (int) : "))
	gpa = float(input("Enter your current gpa (float) : "))
	grade = input("Enter your current class (freshman, sophomore, junior, senior) (str) : ")
	tuple_of_values = (student_id, first_name, last_name, age, gpa, grade)
	db_cursor.execute(sql, tuple_of_values)

	print("Inserted row into table.")


def select_all(db_cursor):
# select without where clause
	sql = "select * from student"
	result_set = db_cursor.execute(sql)
	print("\nTable now has the following rows:")
	for row in result_set:
		print(row)
	print()


def select_row(db_cursor):
# select with a where clause
	sql = "select * from  student where student_id = ?"
	student_id = input("Please enter the student_id (int) that you want to search for: ")
	tuple_of_value = (student_id, )
	db_cursor.execute(sql, tuple_of_value)
	result_set = db_cursor.execute(sql, tuple_of_value)
	print("\nHere is the row you have selected: ")
	for row in result_set:
		print(row)
	print()


def update_row(db_cursor):
	sql = "update student set first_name = ?, last_name = ? where student_id = ?"
	student_id = int(input("Enter the student_id (int) for the student you would like to update: "))
	first_name = input("Enter the new first name(str): ")
	last_name = input("Enter the new last name(str): ")
	tuple_of_values = (first_name, last_name, student_id)
	db_cursor.execute(sql, tuple_of_values)
	print("Row updated.")
	
def delete_row(db_cursor):
	sql = "delete from student where student_id = ?"
	student_id = int(input("Enter the student_id (int) that you want to delete: "))
	tuple_of_value = (student_id, )
	db_cursor.execute(sql, tuple_of_value)
	print("Row deleted.")


def display_menu(db_conn, db_cursor):
	while True:
		print("Menu:")
		print("Enter S to get started and create a new database")
		print("Enter C to create a new row")
		print("Enter R to retrieve data")
		print("Enter U to update a row")
		print("Enter D to delete a row")
		print("Enter Q to quit the program")
		choice = input("Enter your choice: ").upper()
		if choice == "S":
			drop_table(db_cursor)
			create_table(db_cursor)
		elif choice == "C":
			insert_row(db_cursor)
		elif choice == "R":
			select_row(db_cursor)
		elif choice == "U":
			update_row(db_cursor)
		elif choice == "D":
			delete_row(db_cursor)
		elif choice == "Q":
			print("Goodbye")
			break
		else:
			print("Invalid choice of", choice)
		db_conn.commit()
		select_all(db_cursor)
def main():
	# call connect_to_db
	db_conn, db_cursor = connect_to_db()
	# call display_menu
	display_menu(db_conn, db_cursor)
	# close the database
	db_conn.close()

main()
