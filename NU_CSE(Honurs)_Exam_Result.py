import math

total_sub = int(input("Total subject Numbers : "))
total_lab_sub = int(input("Total Lab_subject Numbers : "))

subCr_num = int(input("subject_Credit_number : "))
lab_Credit_num = float(input("lab_subject_Credit_number : "))
# main subject
total_sub_Ltr_Grade = []
for i in range(1, total_sub + 1):
    sub = input("Subject {number} Ltr. Grade = : ".format(number=i))
    total_sub_Ltr_Grade.append(sub)

total_sub_marks = 0.00
for i in total_sub_Ltr_Grade:
    if i == "A+" or i == "a+":
        total_sub_marks += 4.00
    elif i == "A" or i == "a":
        total_sub_marks += 3.75
    elif i == "A-" or i == "a-":
        total_sub_marks += 3.50
    elif i == "B+" or i == "b+":
        total_sub_marks += 3.25
    elif i == "B" or i == "b":
        total_sub_marks += 3.00
    elif i == "B-" or i == "b-":
        total_sub_marks += 2.75
    elif i == "C+" or i == "c+":
        total_sub_marks += 2.50
    elif i == "C" or i == "c":
        total_sub_marks += 2.25
    elif i == "D" or i == "d":
        total_sub_marks += 2.00

# lab subject
add_lab_Grade = []
for i in range(1, total_lab_sub + 1):
    lab = input("Lab {number} Ltr. Grade = : ".format(number=i))
    add_lab_Grade.append(lab)

total_lab_marks = 0.00
for i in add_lab_Grade:
    if i == "A+" or i == "a+":
        total_lab_marks += 4.00
    elif i == "A" or i == "a":
        total_lab_marks += 3.75
    elif i == "A-" or i == "a-":
        total_lab_marks += 3.50
    elif i == "B+" or i == "b+":
        total_lab_marks += 3.25
    elif i == "B" or i == "b":
        total_lab_marks += 3.00
    elif i == "B-" or i == "b-":
        total_lab_marks += 2.75
    elif i == "C+" or i == "c+":
        total_lab_marks += 2.50
    elif i == "C" or i == "c":
        total_lab_marks += 2.25
    elif i == "D" or i == "d":
        total_lab_marks += 2.00

# Calculation
total_sub_cre = total_sub * subCr_num
total_lab_cre = total_lab_sub * lab_Credit_num
both_cre = total_sub_cre + total_lab_cre

full_marks = (total_sub_marks * subCr_num) + (total_lab_marks * lab_Credit_num)
result = round(full_marks / both_cre, 2)

print("subject", total_sub_Ltr_Grade)
print("result : GPA ", result)
