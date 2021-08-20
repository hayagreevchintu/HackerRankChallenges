#Link to the challenge:
#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

#Solution begins here:
def split_and_join(line):
    line = line.split()
    return "-".join(line)

#Stub code:    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)