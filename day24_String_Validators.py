'''In the first line, print True if s has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if s has any alphabetical characters. Otherwise, print False. 
In the third line, print True if s has any digits. Otherwise, print False. 
In the fourth line, print True if s has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True'''


s = input()
print (any([c.isalnum() for c in s]))
print (any([c.isalpha() for c in s]))
print (any([c.isdigit() for c in s]))
print (any([c.islower() for c in s]))
print (any([c.isupper() for c in s]))