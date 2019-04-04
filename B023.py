from sys import stdin

def get_line():
    return stdin.readline().rstrip()

data = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1010010',
    '8': '1111111',
    '9': '1111011'
}

def ext(string_, i, txt):
    tmp = list(string_)
    tmp[i] = txt
    return ''.join(tmp)

def plus_(a):
    ans = []
    for j in data.keys():
        if j == a:
            continue
        for k in range(7):
            if data[a][k] == '0' and ext(data[a], k, '1') == data[j]:
                ans += [ j ]
    return ans

def minus_(a):
    ans = []
    for j in data.keys():
        if j == a:
            continue
        for k in range(7):
            if data[a][k] == '1' and ext(data[a], k, '0') == data[j]:
                ans += [ j ]
    return ans

def check(a, b):
    ans = []
    for j in range(7):
        if a[j] == '1' and b[j] == '0':
            ans += ['m']
        elif a[j] == '0' and b[j] == '1':
            ans += ['n']
        else:
            ans += ['0']
    return ''.join(ans)

def zero_(a):
    ans = []
    for j in data.keys():
        if j == a:
            continue
        tmp = check(data[a], data[j])
        if tmp.count('m') == 1 and tmp.count('n') == 1:
            ans += [ j ]
    return ans

n = get_line()
ans = []
for k in range(len(n)):
    pat1 = zero_( n[k] )
    if pat1 == []:
        continue
    for i in range(len(pat1)):
        ans += [ ext(n, k, pat1[i]) ]

for k in range(len(n)):
    pat1 = plus_( n[k] )
    if pat1 == []:
        continue
    for i in range(len(n)):
        if i == k:
            continue
        pat2 = minus_( n[i] )
        if pat2 == []:
            continue
        for a in range(len(pat1)):
            for b in range(len(pat2)):
                ans += [ ext( ext(n, k, pat1[a]), i, pat2[b]) ]

if ans == []:
    print('none')
else:
    ans.sort()
    print(*ans, sep = '\n')
