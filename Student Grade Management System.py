print("Student Grade Management System")
total=int(input("Total number of students: "))
dict={}

for i in range(total):
    name=input("Enter Student Name: ")
    marks=int(input("Marks: "))
    dict[name]= marks
     
print("="*36)
print("\tSTUDENT REPORT")
print("="*36)
for name in dict:
    if dict[name]<=100 and dict[name]>=90:
        Grade="A"
    elif dict[name]<90 and dict[name]>=80:
        Grade="B"
    elif dict[name]<80 and dict[name]>=70:
        Grade="C"
    elif dict[name]<70 and dict[name]>=60:
        Grade ="D"
    else:
        Grade="F"
    print(f"{name} : {dict[name]} ({Grade})")

l= list(dict.values())
sum=0
for i in l:
    sum+=i
print(f"\nAverage : {round(sum/total,2)}\n")

h_name=list(dict.keys())[0]
h_marks=l[0]
l_name=list(dict.keys())[0]
l_marks=l[0]
for name in dict:
    if dict[name]>h_marks:
        h_marks= dict[name]
        h_name= name
for name in dict:        
    if dict[name]<=l_marks:
        l_marks= dict[name]
        l_name = name

print(f"Topper : {h_name}")
print(f"Lowest : {l_name}")
print("="*36)
