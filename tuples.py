#Link to the challenge:
#https://www.hackerrank.com/challenges/python-tuples/problem

#Solution begins here:
n = int(input())
integer_list = tuple(map(int, input().split()))
print(hash(integer_list))