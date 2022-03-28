def areaofsquare():
    side=int (input("enter the size of square:"))
    print("area of square is",side ,"unit is",side**2,"square units.")


def perimeterofrectangle():
    length = int(input("enter the length  of rectangle:"))
    breadth = int(input("enter the breadth  of rectangle:"))
    print("perimeter of rectangle  is", length, "", breadth, "", "unit is", 2*(length + breadth), "square units.")


def areaofrectangle():
    length = int(input("enter the length  of rectangle:"))
    breadth=int(input("enter the breadth  of rectangle:"))
    print("area of rectangle  is", length,"", breadth,"", "unit is",length*breadth, "square units.")

if __name__=="__main__":
    print("menu \n"
      "1.area of square\n"
      "2.perimeter of rectangle\n"
      "3.area of rectangle\n"
      "4.exit\n")

x=int(input("enter choice to get the result "))
if x==1:
    areaofsquare()
elif x==2:
    perimeterofrectangle()
elif x==3:
    areaofrectangle()
elif x==4:
    exit()
else:
    print("please enter correct choice")


