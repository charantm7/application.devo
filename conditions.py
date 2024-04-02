eligibility_criteria=int(input("Enter your current age:"))

if (eligibility_criteria>=21 and eligibility_criteria<30):
    print("you are having a eligibile for marragie")
    if (eligibility_criteria>=21 and eligibility_criteria<=24):
         print("and you get young and energitic girl to marry")
    else :
         print(" and you will not get young girl to marry")     
elif (eligibility_criteria>=60 and eligibility_criteria<=100):
      print("you can not marry in this age")
elif (eligibility_criteria>=30 and eligibility_criteria<40):
       print(input("what type of age criteria is required:"))
else :
    print("you are not eligible for marraige")