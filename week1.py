x='OIC Market'
y='Buea'
school_items=['books','pens','pencils','calculators','rulers','mathset']
food=['beans','corn','plantain','cabbage','potatoes']
numbers=[2,5,8,3,5,9,4,6,8,2,4,9]
items=school_items+food
print(x,y)
print('what did you buy from {}:'.format(x))
print(items)
print('add another protein to the buy as food:')
food.append('eggs')
print(food)
print('what did you buy after pencils:')
print(school_items.pop(3))
print('whats the smallest mark obtained:')
print(min(numbers))
print('whats the largest mark obtained:')
print(max(numbers))
print('how many students have 5 in the test:')
print(numbers.count(5))
print('Reverse the letters of market')
emp=''
for i in x:
    emp=i+emp
print(emp)

