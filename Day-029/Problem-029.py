#

class Solution:
    def countStudents(self, students,sandwiches):
        index = 0
        while True:
            updated = []
            for student in students:
                if student == sandwiches[index] :
                    index += 1
                else:
                    updated.append(student)
            if len(students) == len(updated):
                break
            
            students=updated
        return len(students)

s1=[]
s2=[]

n1=int(input("Enter size-1"))
for i in range(n1):
    e=int(input())
    s1.append(e)

n2=int(input("Enter size-2"))
for j in range(n2):
    r=int(input())
    s2.append(r)

print(Solution().countStudents(s1,s2))