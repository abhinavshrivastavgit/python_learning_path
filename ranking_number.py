index = int(input('Enter the lenght of the list: '))
print('Enter the your respected list: ',end ='')
num =[]
# taking input from the user for following list
for i in range(0,index):
    value = int(input(f'value for num[{i}] is: '))
    num.append(value)

# now printing the list
print('Registered list is: [', end= '')
for i in range(0,index):
    if i < index-1:
       print(num[i],end=', ')
    else:
        print(num[i], end= '')
print(']')

# removing Duplicates using set()
unique_nums= list(set(num))

# sorting number
unique_nums.sort( )

print(f'Winner: {unique_nums[-1]}')
# precaution
# for runner-up checking case if not all numbers are same or not
if len(unique_nums) < 2:
    print("No Runner-Up: All values are identical.")
else:
    print(f'Second Runner-Up: {unique_nums[-2]}')

