#Link to the challenge:
#https://www.hackerrank.com/challenges/sock-merchant/problem

#Solution begins here:
def sockMerchant(n, ar):
    # Write your code here
    sockCount = {}
    count = 0
    for i in ar:
        if i in sockCount.keys():
            sockCount[i] += 1
        else:
            sockCount[i] = 1
    for i in sockCount.keys():
        count += int(sockCount[i] / 2)
    return count

#Stub code:
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = sockMerchant(n, ar)
print(result)