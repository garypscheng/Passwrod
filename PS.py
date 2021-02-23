password = 'a123456'
x = 3
while x > 0:
	x= x-1
	psw = input('Please enter your password :     ')
	if psw == password :
		print('Login sucessful')
	else:
		print ("Password is incorrect")
		if x > 0:
			print('You still have', x, 'times to enter your password')
		else: 
			print('Your account have blocked')
