'''You have a record of N students.
 Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
 The marks can be floating values. 
 The user enters some integer N followed by the names and marks for students. 
 You are required to save the record in a dictionary data type. 
 The user then enters a student's name. 
 Output the average percentage marks obtained by that student, correct to two decimal places.'''

n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()
query_scores = student_marks[query_name]
print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))


