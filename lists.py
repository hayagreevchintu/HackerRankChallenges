#Link to the challenge:
#https://www.hackerrank.com/challenges/python-lists/problem

#Solution begins here:
if __name__ == '__main__':
    outputList = []
    N = int(input())
    for i in range(N):
        j = input().split()
        if j[0] == 'insert':
            outputList.insert(int(j[1]), int(j[2]))
        elif j[0] == 'print':
            print(outputList)
        elif j[0] == 'remove':
            outputList.remove(int(j[1]))
        elif j[0] == 'append':
            outputList.append(int(j[1]))
        elif j[0] == 'sort':
            outputList = sorted(outputList)
        elif j[0] == 'pop':
            outputList.pop()
        elif j[0] == 'reverse':
            outputList = outputList[::-1]