# a="20"
# b=10
# c=40
# d=15
# e="34"
# f="28"
# print(int(a)+int(e)+int(f))
# print(b-c+d)
# print(int(a)+int(b)+int(f))
# g=79
# print("my marks in maths is",g) 



# a=10
# b=8.6
# c="my is faiz"
# d=True
# print(type(a),a)
# print(type(b),b)
# print(type(c),c)
# print(type(d),d)

# age=23
# print(type(age),age)

# name="faiz"
# print(name)
# print(len(name))



# / division 





# a=17
# b=5
# c=a+b
# d=a-b
# e=a*b
# f=a/b # division 
# g=a//b # floor division, integer division 
# h=a%b # modulo division 
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h) 


# x=10
# y=20
# x,y=y,x
# print(x,y)



# age=20
# c=age+5
# print(c)


# price=99.99
# gst=99.99%18
# print(gst)

# price = 99.99
# gst = price * 18 / 100
# final_price = price + gst

# print(final_price)


# name=input("my name is:")
# phonenumber=input("my phn is:")
# college=input("college name:")
# print(name)
# print(phonenumber)
# print(college)

# name=str(input("what is your name:"))
# age=int(input("what is your age:"))
# birth=2026-age
# print("hello", name, "we both are of same birth year that is" , birth)

# name=str(input("what is your name:"))
# age=int(input("what is your age:"))
# maths_marks=float(input("what is your marks:"))
# print(f"Name: {name} , Age:{age}")
# print(f"Marks: {maths_marks:.1f}%") 

# total = int(input("Enter seconds: "))
# hours = total // 3600
# minutes = (total % 3600) // 60
# seconds = total % 60
# print(f"Hours: {hours} , minutes:{minutes} , seconds: {seconds}")


# width=float(input("width:"))
# height=float(input("height:"))
# area=width*height
# perimeter=2*(width+height)
# print(f"Area: {area}, Perimeter: {perimeter}")

# item1=float(input("your first item is:"))
# item2=float(input("your second item is:"))
# item3=float(input("your third item is:"))
# total=item1+item2+item3
# gst = total * 18 /100
# print("the total bill including gst is:" ,total+gst) 


# food_items=["shawarma","coke", "icecream", "biryani"]
# prices=[100,30,50,200]
# a=input("enter the first item:")
# b=input("enter the second item:")
# item1=food_items.index(a)
# item2=food_items.index(b)
# price1 = prices[food_items.index(item1)]
# price2 = prices[food_items.index(item2)]
# total=price1+price2 
# gst = total * 18 /100
# print("the total bill including gst is:" ,total+gst)


categories=["silver", "gold", "platimun"]
prices=[200,300,400]
cat1=input("enter the no of first category:")
cat2=input("enter the no of second category:")
ticket1=int(input("enter the first of ticket:"))
ticket2=int(input("enter the second of ticket:"))
price1=prices[categories.index(cat1)]
price2=prices[categories.index(cat2)]
total= (price1*cat1)+(price2*cat2)
sum = total+0.12
print("the final bill is:", total)


# g=[11,33,44,22,55]
# g.remove(22)
# # print(g)
# g.pop()
# print(g)
