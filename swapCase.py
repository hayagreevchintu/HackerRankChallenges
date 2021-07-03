#Link to the challenge:
#https://www.hackerrank.com/challenges/swap-case/problem

#Solution begins here:
def swap_case(s):
    return "".join([i.lower() if i.isupper() else i.upper() for i in s])

#Stub code:
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)