#Link to the challenge:
#https://www.hackerrank.com/challenges/find-a-string/problem

#Solution begins here:
def count_substring(string, sub_string):
    return sum([1 for i in range(len(string)-len(sub_string)+1) if string[i:i+len(sub_string)] == sub_string])

#Stub code:
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)