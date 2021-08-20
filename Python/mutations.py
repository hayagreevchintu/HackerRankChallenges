#Link to the challenge:
#https://www.hackerrank.com/challenges/python-mutations/problem

#Solution begins here:
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

#Stub code:
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)