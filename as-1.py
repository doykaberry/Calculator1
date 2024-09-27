#assignments of variables and prompts the user to imput their completed labs and quizzes or input their grade


completed_labs = int(input("Enter the number of labs completed: "))
completed_quizzes = int(input("Enter the number of quizzes completed: "))
grade_assignment1 = int(input("Enter grade for Assignment 1: "))
grade_assignment2 = int(input("Enter grade for Assignment 2: "))
grade_assignment3 = int(input("Enter grade for Assignment 3: "))
grade_assignment4 = int(input("Enter grade for Assignment 4: "))
grade_midterm1 = int(input("Enter grade for Midterm 1: "))
grade_midterm2 = int(input("Enter grade for Midterm 2: "))
grade_final_exam = int(input("Enter grade for Final Exam: "))
grade_midterms_final_preperation = int(input("Enter grade for Midterms and Final Preperation: "))


#calculation of final grade and more variable assignments


##restriction for completed labs and quizzes over and equal to 6 and under 6

completed_labs_grade = 100 if completed_labs >=6 else (completed_labs/6) * 100
completed_quizzes_grade = 100 if completed_quizzes >=6 else (completed_quizzes/6) * 100


##variable assignments for the grade multiplied by the weight
completed_labs_weight = completed_labs_grade * 0.20
completed_quizzes_weight = completed_quizzes_grade * 0.15
grade_assignments_weight = ((grade_assignment1 + grade_assignment2 + grade_assignment3 + grade_assignment4)/4) * (0.16)
grade_midterms_weight = ((grade_midterm1 + grade_midterm2)/2) * 0.25
grade_final_exam_weight = grade_final_exam * 0.18
grade_midterms_final_preperation_weight = grade_midterms_final_preperation * 0.06

#Final calculation
Final_grade = completed_labs_weight + completed_quizzes_weight + grade_assignments_weight
