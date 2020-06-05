mathsmark = float(input("Mark here: "))
chemsmark = float(input("Mark here: "))
physmark = float(input("Mark here: "))

sum = mathsmark + chemsmark + physmark
print(sum)
percentage = int(sum)/3

print("overall percentage: "+str(percentage)+'%')

def perc(): 
    if percentage >= 70:
        print("A")
    elif percentage >= 60:
        print("B")
    elif percentage >= 50:
        print("C")
    elif percentage >= 40:
        print("D")
    else:
     percentage < 40
     print("You Failed")

