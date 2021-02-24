'''
Which of the following code snippets will NOT reverse the string 'hello' 
and return 'olleh'?
'''

input_str = "hello"

#print(input_str[::-1])
print(reversed(input_str))

reversed_input = reversed(input_str)

print(''.join(reversed_input))

l = [1,2,3]