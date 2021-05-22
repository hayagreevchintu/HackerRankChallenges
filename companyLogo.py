#Challenge link:
#https://www.hackerrank.com/challenges/most-commons/problem

def fun(string):
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    print(all_freq)
    all_freq_list=sorted(all_freq,key=all_freq.get,reverse=True)
    print(all_freq_list)
    for i in range(3):
        print(all_freq_list[i] + ' '+str(all_freq[all_freq_list[i]]))

string = sorted(list(input()))
fun(string)
