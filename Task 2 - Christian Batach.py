number_list = []
odd_list = []

for i in range(1,31):
  number_list.append(i)

print("The list from 1-30:",'\n',number_list,'\n')

sum_list = sum(number_list)

for i in range(len(number_list)):
 if number_list[i]%2 == 1:
   odd_list.append(number_list[i])

odd_sum = sum(odd_list)

for i in range (10, 21):
  number_list.remove(i)
  

print("The sum of all numbers in the list:",sum_list,'\n')

print("The sum of all odd numbers in the list:",odd_sum,'\n')

print("The list with numbers 10-20 removed:",'\n',number_list)