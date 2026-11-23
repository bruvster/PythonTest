class Student:
	def __init__(self, height, weight, grade, first_name, last_name):
		self.height = height
		self.weight = weight
		self.grade = grade
		self.first_name = first_name
		self.last_name = last_name


while True:
	try:
		height = int(input("Height: "))
		weight = int(input("Weight: "))
		grade = input("Grade: ").strip()
		first_name = input("First name: ").strip()
		last_name = input("Last name: ").strip()
		if height <= 0 or weight <= 0:
			raise ValueError("height and weight must be positive")
		if not grade or not first_name or not last_name:
			raise ValueError("grade and names cannot be empty")
	except ValueError as error:
		print(f"Invalid input ({error}). Please try again.")
		continue

	candidate = Student(height, weight, grade, first_name, last_name)
	print(
		f"Student is: {candidate.first_name} {candidate.last_name}; "
		f"height: {candidate.height}, weight: {candidate.weight}, grade: {candidate.grade}"
	)
	confirmation = input("Keep these details? (yes/no): ").strip().lower()
	if confirmation in ("yes", "y"):
		student = candidate
		break
	if confirmation in ("no", "n"):
		print("Changes discarded. Please enter the details again.")
		continue
	print("Please answer yes or no; the details were not saved.")

print("Final student details:")
print(
    f"Student is: {student.first_name} {student.last_name}; "
    f"height: {student.height}, weight: {student.weight}, grade: {student.grade}"
)
