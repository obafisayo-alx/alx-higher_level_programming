#!/usr/bin/python3


def no_c(my_string):
	result = ""
	for i in my_string:
		if i.lower() != "c":
			result += i
	return result

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
