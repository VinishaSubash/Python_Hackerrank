p=int(input("ENTER THE SALARY:"))
if (p>5000 and p<50000 ):
   hdr=0.2*p
   da=0.1*p
   si=p+hdr+da
   print("THE gross salary:",si)
else:
      print("invalid input")
