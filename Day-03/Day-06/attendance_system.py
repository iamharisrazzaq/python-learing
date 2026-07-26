total_students=8
boys=5
girls=3
present_boys=0
absent_boys=0
present_girls=0
absent_girls=0
boys_name=["Ali","Ahmad","Talha","Haris","Anas"]
girls_name=["Ayesha","Sana","Hina"]
# Boys Attendance
for boy in boys_name:
    attendance = input(f"{boy} Present or Absent (P/A): ").upper()

    if attendance == "P":
        present_boys += 1
    elif attendance == "A":
        absent_boys += 1
# Girls Attendance
for girl in girls_name:
    attendance = input(f"{girl} Present or Absent (P/A): ").upper()

    if attendance == "P":
        present_girls += 1
    elif attendance == "A":
        absent_girls += 1


# Total Attendance Calculation
total_present = present_boys + present_girls
total_absent = absent_boys + absent_girls

attendance_percentage = (total_present / total_students) * 100

# Display Attendance Summary
print("------ Attendance Report ------")
print("Total Students:", total_students)
print("Boys Present:", present_boys)
print("Boys Absent:", absent_boys)
print("Girls Present:", present_girls)
print("Girls Absent:", absent_girls)
print("Total Present:", total_present)
print("Total Absent:", total_absent)
print("Attendance Percentage:", attendance_percentage, "%")