input_string=input('Enter a string:')
count=0
vowels='aeiouAEIOU'
for char in input_string:
    if char in vowels:
        count+=1
print(count)
