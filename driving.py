country = input('請問是哪國人:')
age = input('請問今年幾歲:')
age=int(age)
if country == '台灣':
	if age >18:
		print('如果你年紀', age, '你可以考駕照')
	else:
		print('你還不能考駕照')
		
