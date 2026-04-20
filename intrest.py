p=int(input("Enter the principal amoount :"));
r=int(input("Enter the rate of interest :"));
t=int(input("Enter the time period :"));
if(1<=p<=10000 and 1<=r<=20 and 1<=t<=10 ):
   SI = (p*r*t)/100;
   print(SI);
else :
   print("Enter the valid data ");
