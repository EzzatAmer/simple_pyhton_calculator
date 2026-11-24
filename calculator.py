# i wont builld a Calculator
print("hallo to my sumbol app")
nm1=float(input("intr_namdr_one :"))

add=(input("Add symbol-,+,*,/,% : " ))

nm2=float(input("intr_namdr_two :"))

print("|---------------------------|")
if add=="+":
    print( nm1 + nm2 )

elif add=='-' :
    print(nm1-nm2)
    
elif add=='*' :
    print(nm1*nm2)

elif add=='/' :
    print(nm1/nm2)

elif add=='%' :
    print(nm1%nm2)

else:
     print ("sorry tray agane")