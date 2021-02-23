import random
start =input('Please enter your starting  range :     ')
end = input('Please enter your ending range :        ')
start =int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True :
  count += 1
  x = input('please input your number (range between 1 to 100):    ')
  x = int(x)
  if x == r :
  	print( 'Bingo!')
  	print(' It is ', count , 'times')
  	break
  elif  x > r :
  	print ('The answer is smaller than you') 
  elif x < r :
  	print('The answer is bigger than you')
  
