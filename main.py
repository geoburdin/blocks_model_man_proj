import numpy as np

A = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 3, 1, 0, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 5, 0, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 4, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4, 7, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 7, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 7, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 7, 7, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 7, 7, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 7, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 6, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ]
)

def cost_start(A, y, x):
    cost = 0.0
    for i in range(0, y+1, 1):
        for j in range(x - (y - i), x + (y - i)+1, 1):

            if i == 0:
                costs = 1
            if i == 1:
                costs = 1.5
            if i == 2:
                costs = 2
            if i == 3:
                costs = 2.5
            if i == 4:
                costs = 3
            if i < 11 and i > 4:
                costs = 3.5
            if i == 11:
                costs = 4.5
            if i == 12:
                costs = 5
            cost = cost + costs
    return cost

def value(A, y, x):
    summ = A[y, x]
    for i in range(0, y+1, 1):
        for j in range(x - (y - i), x + (y - i)+1, 1):
            if j < 29 and j > 0:
                summ = summ + A[i, j]
            elif j > 28:
                summ = summ + A[i, 28]
            elif j < 0:
                summ = summ + A[i, 1]
    return summ

def mined(A,ind):
    for i in range(0, ind[0]+1, 1):
        for j in range(ind[1]+1 - (ind[0]+1 - i), ind[1]+1 + (ind[0]+1 - i)+1, 1):
            A[i,j]=0


V = np.zeros([13, 30])

C = np.zeros([13, 30])

for y in range(13):
    for x in range(29):
        C[y, x]=cost_start(A, y, x)
        print('{:>6}'.format(C[y, x]), end=' ')
        # print(A[y, x], end=' ')
    print()
print('\n')

search = True
while search :
    for y in range(13):
        for x in range(29):
            V[y, x] = value(A, y, x)
            print('{:>6}'.format(V[y, x]), end=' ')
            # print(A[y, x], end=' ')
        print()
    print('\n')

    result = V-C
    for y in range(13):
        for x in range(29):

            print('{:>6}'.format(result[y, x]), end=' ')
            # print(A[y, x], end=' ')
        print()

    ind = np.unravel_index(np.argmax(result, axis=None), result.shape)
    print('index of max is ', ind)
    max = result[ind]

    if max <= 0:
        search=False
        break
    print('max is ', max)
    mined(A,ind)
    mined(C,ind)



