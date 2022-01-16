#True and False are reserve words needed for the 
#boolean data type
is_cc_valid = False
i_pwd_okay = True
x = 1

if is_cc_valid and is_pwd_okay:
	print('This Customer is in good standing')
	print('second message to go with true')
else:
	print('This Customer is NOT in good standing')
	print('second message to go with else')

if (not is_cc_valid) or is_pwd_okay:
	print('message')
if x == 1:
	print('x is 1')
else:
	print('x is not 1')

