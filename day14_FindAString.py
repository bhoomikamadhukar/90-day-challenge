def count_substring(string, sub_string):
    return (sum([1 for i in range(0, len(string) - len(sub_string) + 1) if (string[i:(len(sub_string)+i)] == sub_string)]))

def main():
	string=input("enter string")
	sub_string=input("enter substring")
	count_substring(string,substring)
main()