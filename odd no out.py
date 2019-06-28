# odd-no-out
i=int(input())

for j in repr(i):
    if j.isdigit():
        if (int(j)%2!=0):
            print(j,end=' ')
