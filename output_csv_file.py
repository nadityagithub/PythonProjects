filename = "output_students.csv"
def create_list():
    my_list = [["Joe", "Smith", 3.9],
               ["Jane", "Doe", 3.8]]
    return my_list
def write_to_file(the_list):
    file_ptr = open(filename, "a")
    file_ptr.write("First Name,Last Name,GPA\n")
    for row in the_list:
    	s = row[0] + "," \
            + row[1] + ","\
            + str(row[2]) + "\n"
    	file_ptr.write(s)
def main():
    student_list = create_list()
    write_to_file(student_list)
main()
