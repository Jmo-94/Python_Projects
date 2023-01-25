Menu = ["Chicken sandwich", "Mac n cheese", "Chicken wings", "Waffle fries","Chicken tenders","Drinks"]
Price = [13,13,10,8,12,5]

print ("Welcome to the Chick inn")
print ("Table for two?")
print ("Heres the Menu for today")
print (Menu)
print (Price)

myorderFood=[]
myorderprice=[]
counter=0
Total=0

for i in Menu:
    print(i), 
    
order = input("Can I take your order? Yes/No ")
if order == "No":
    print("Ok I'll come back to you")
    exit()
else:
    print("Ok")    

nextorder = True

while nextorder == True:
    foodorder = input("What would you like?\n")
    if foodorder == "Chicken sandwich":
        myorderFood.append(Menu[0])
        myorderprice.append(Price[0]) 
        counter=counter+1
        Total=Total+(Price[0])
    elif foodorder == "Mac n cheese":
        myorderFood.append(Menu[1])
        myorderprice.append(Price[1])
        counter=counter+1
        Total=Total+(Price[1])
    elif foodorder == "Chicken wings":
        myorderFood.append(Menu[2])
        myorderprice.append(Price[2])
        counter=counter+1
        Total=Total+(Price[2])
    elif foodorder == "Waffle fries":
        myorderFood.append(Menu[3])
        myorderprice.append(Price[3])    
        counter=counter+1
        Total=Total+(Price[3])
    elif foodorder == "Chicken tenders":
        myorderFood.append(Menu[4])
        myorderprice.append(Price[4])
        counter=counter+1
        Total=Total+(Price[4])
    elif foodorder == "Drinks":
        myorderFood.append(Menu[5])
        myorderprice.append(Price[5])
        counter=counter+1
        Total=Total+(Price[5])
    finished = input("Will that be all? Y/N ")
    if finished == "N":
        nextorder=True
    else:
        nextorder=False     
        print(myorderFood)
        print(myorderprice)

#order2 = input("Can I take your order miss? Yes/No")


y=0

print ("Heres your receipt\n")
#print ("     ")
print ("********")
while y<counter:

    print ("Item:" + (myorderFood[y]))
    print ("Cost:" + str(myorderprice[y]))
    y=y+1

print ("The final cost will be $"+ str(Total))    