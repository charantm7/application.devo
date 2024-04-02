eligibility_criteria=int(input("Enter your current age:"))

if (eligibility_criteria>=21 and eligibility_criteria<30):
    print("you are having a eligibile for marragie")
    height=int(input(f"Enter your height in cm between your eligibility criteria:"))
    if (eligibility_criteria>=21 and eligibility_criteria<=25 and height>=160 and height<170):
         print("and you get young and energitic girl to marry")
    elif (eligibility_criteria>=26 and eligibility_criteria<=30 and height>=160 and height<=170):
         print(" and you will get a normal young girl to marry")
    elif (eligibility_criteria>=21 and eligibility_criteria<=25 and height>170):
         print("you will get a young girl but she is more than your height") 
    elif (eligibility_criteria>=26 and eligibility_criteria<=30 and height>170):
         print(" and you will get a normal young girl to marry but she is more heighter than you")   
    else :
         print("you will marry but you will not get a young girl to marry")
elif (eligibility_criteria>=60):
      print("you can not marry in this age")
elif (eligibility_criteria>=30 and eligibility_criteria<60):
       print("yep You will marry a girl little bit of older age but she also younger than you.")
else :
    print("you are not eligible for marraige")