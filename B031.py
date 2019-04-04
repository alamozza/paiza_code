# paiza B031
#
from sys import stdin
# stdin = open('t.txt')

def rev(string):
    # convert each character in string from 'b' to 'w', from 'w' to 'b'
    return ''.join(['b' if string[i] == 'w' else 'w' for i in range(len(string))])

def main():
    """
    data: read string
        [0] : not reverse
        [1] : reverse
    ind: index of the 1st different character
        [0] : index of data[0]
        [1] : index of data[1]
    """
    n = int(stdin.readline().rstrip())
    data = [''] * 2
    data[0] = stdin.readline().rstrip()
    if n != 1 and n != 2:
        ind = [ 0 ] * 2
        while True:
            if data[0].count('b') == 0 or data[0].count('w') == 0:
                break
            data[1] = data[0][::-1]
            for i in range(2):
                ind[i] = data[i].index('b') if data[i][0] == 'w' else data[i].index('w')
            if sum(ind) == n:
                break
            data[0] = data[0][:ind[0]] + rev(data[0][ind[0]:(n - ind[1])]) \
                    + data[0][n-ind[1]:]
    #
    print(data[0].count('b'), end = '\n')

if __name__ == '__main__':
    main()

