with open('day6.txt','r') as file:
    line = file.readline().strip('\n')

def setize(string,index,n):
    lst = [string[index-i] for i in range(n)]
    return set(lst)


n = 14

for i in range(n-1,len(line)+1):
    if len(setize(line,i,n)) < n:
        continue
    else:
        print(i+1)
        break
