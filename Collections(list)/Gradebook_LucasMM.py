def avaragecalc(grades):
     avarage= grades[0]+grades[1]+grades[2]+grades[3]+grades[4]
     avarage = avarage/5
     return(avarage)

def gradel(avarage):
    if avarage>=90:
        letter="A"
    elif avarage>=80:
        letter="B"
    elif avarage>=70:
        letter="C"
    else:
        letter="D"
    return(letter)
name = input("What is your name:")
grades = [0,0,0,0,0]
grades[0] = int(input("What is your grade1:"))
grades[1] = int(input("What is your grade2:"))
grades[2] = int(input("What is your grade3:"))
grades[3] = int(input("What is your grade4:"))
grades[4] = int(input("What is your grade5:"))

print(name)
avarage=avaragecalc(grades)
print(avarage)
print("Letter")
print("Grade:",gradel(avarage))