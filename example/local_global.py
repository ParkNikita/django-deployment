def function_outer():
	x = 2
	print("x равен", x)
	def function_inner():
		x = 5 
	function_inner()
	print("теперь x равен ", x)
function_outer()		