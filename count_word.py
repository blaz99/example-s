#two ways to count

'''

string= "i am just testing this one"
print(f"This is original: {string}")
result= len(string.split())
print(f"The number of words is: {result}")

'''
#\w letters ..... \w+ words
import re
string= "i am just testing this one"
print(f"This is original: {string}")
result= len(re.findall(r'\w', string))
print(f"The number of words is: {result}")

