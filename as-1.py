#assignments of variables and prompts the user to imput their completed labs and quizzes or input their grade


completed_labs = int(input("Enter the number of labs completed: "))
completed_quizzes = int(input("Enter the number of quizzes completed: "))
grade_assignment1 = input("Enter grade for Assignment 1: ")
grade_assignment2 = input("Enter grade for Assignment 2: ")
grade_assignment3 = input("Enter grade for Assignment 3: ")
grade_assignment4 = input("Enter grade for Assignment 4: ")
grade_midterm1 = input("Enter grade for Midterm 1: ")
grade_midterm2 = input("Enter grade for Midterm 2: ")
grade_final_exam = input("Enter grade for Final Exam: ")
grade_midterms_final_preperation = input("Enter grade for Midterms and Final Preperation: ")


#calculation of final grade and more variable assignments


##restriction for completed labs and quizzes over and equal to 6 and under 6

completed_labs_grade = 100 if completed_labs >=6 else (completed_labs/6) * 100
completed_quizzes_grade = 100 if completed_quizzes >=6 else (completed_quizzes/6) * 100


    



