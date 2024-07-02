# Write your code using if else statements to extract the quarter
#if the date lies between 1st July, 2020 - 30th September, 2020, 
# the extracted quarter will be '2020-Q3'
date_year = '2020'
date_month = '08'

# Store the quarter value in a string variable named quarter
quarter='2020-08'
if(date_month>='01')&(date_month<='03'):
   print('quarter=',date_year+'-Q1')
elif(date_month>='04')&(date_month<='06'):
    print('quarter=',date_year+'-Q2')
elif(date_month>='07')&(date_month<='09'):
    print('quarter=',date_year+'-Q3')
else:
    print('quarter=',date_year+'Q4')