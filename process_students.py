import json
filename = "input.json"

def process_file():
	file_ptr = open(filename, "r")
	outer_dictionary = json.load(file_ptr)
	student_list = outer_dictionary.get("studentList")
	gpa_list = []
	for student_dictionary in student_list:
		id = student_dictionary.get("id")
		fname = student_dictionary.get("firstName")
		lname = student_dictionary.get("lastName")
		gpa = student_dictionary.get("gpa") 
		gpa_list.append(gpa)
		print("Keys of students are:",student_dictionary.keys())
		print("Id:", id)
		print("Name:", fname, lname)
		print("GPA:", gpa)
		print() 
	print("\nList of gpas before the sort is:", gpa_list)
	gpa_list.sort() 		#put all gpas in order
	print("List of gpas is:", gpa_list)
	print("Number of students:", len(gpa_list))
	print("Lowest GPA is:", min(gpa_list))
	print("Highest GPA is:", max(gpa_list))
	print()
def main():
	process_file()   # call to process_file function	
main()

