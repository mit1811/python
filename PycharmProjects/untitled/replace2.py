n=int(raw_input())
students=[]
for i in range(n):
    name = raw_input()
    marks = float(input())
    students.append([name,marks])
second_largest=sorted(list(set([s for n, s in students])))[1]
students=[n for n,s in students if second_largest==s]
for s in sorted(students):
    print s



