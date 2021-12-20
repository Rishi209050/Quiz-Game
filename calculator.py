print("main menu")
print("1. calculator")
print("2. area finder")
print("3. volume finder")
print("4. exit")
i=0

ch=input("enter your choice")
if ch==('1'):
    print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    if choice=='1':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add=a+b
        print("the adition of both num is",add)
    elif choice=='2':
        c=int(input("enter first num"))
        d=int(input("enter second num"))
        sub=c-d
        print("the subtract of both num is",sub)
    elif choice=='3':
        i=int(input("enter first num"))
        f=int(input("enter second num"))
        mult=i*f
        print("the multiply of both num is",mult)
    elif choice=='4':
        g=int(input("enter first num "))
        s=int(input("enter second num "))
        div=g/s
        print("the divide of both num is",div)

        


