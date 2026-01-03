# Here we will find largest number in the list
# user input of numbers
n = int(input('Enter the lenght of the string: '))
num=[]
for i in range(0,n):
    val = input(f'enter the value for num[{i}]: ')
    num.append(val)

for i in range(0,n):
    print(f'The value for num[{i}]: ', num[i])

print('Your List is: ', end = '')
print('[', end = ' ')
for i in range(0,n):
    if i < n-1:
      print(num[i], end=', ')
    else:
     #for the last number
     print(num[i], end = '')

print(']')


largest_num = int(num[0])
trigger = 0 # Start with the first index
count = 0

while count < n:
    current_val = int(num[count])
    
    # ONLY update if the current number is bigger than our best so far
    if current_val > largest_num:
        largest_num = current_val
        trigger = count # Capture the index ONLY here
        
    count = count + 1 # Move to next item regardless of the 'if' result

print(f'The largest num is at index num[{trigger}] and it is {largest_num}')

