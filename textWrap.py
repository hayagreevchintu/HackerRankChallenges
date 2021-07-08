#Link to the challenge:
#https://www.hackerrank.com/challenges/text-wrap/problem

#Stub code:
import textwrap
#Solution begins here
def wrap(string, max_width):
    return textwrap.fill(string, max_width)
#Stub code:
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)