a = int(input("Enter the side of the cube : "));
if(1<=a<=50):
   vol = a*a*a;
   print("The volume of the cube is :" , vol);
else:
   print("Please enter a valid side ");

[24bcs034@mepcolinux itt]$cat mark.py
tam = int(input("Enter the mark :"));
eng =int(input("Enter the mark :"));
mat =int (input("Enter the mark :"));
if(0<=tam<=100 and 0<=eng<=100 and 0<=mat<=100):
   total_mark = tam+eng+mat;
   avg_mark = total_mark/3;
   print("The total mark is :" , total_mark );
   print("The average mark is :" , avg_mark );
else:
   print("Enter a valid marks ");

