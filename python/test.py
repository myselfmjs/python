
def getNumFor4(): #4个不相同的数排序方式
    x = 0
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                for z in range(1,5):
                    if (i != j) and (j != k) and (k != z) and (z != i) and (k !=i) and (z != i) and (z != j):
                        x = x+1
                        print(i,j,k,z)
    print(x)


def get99(): #九九乘法表
    for i in range(1,10):
        for j in range(1,i+1):
            print('%d*%d=%2d'% (i,j,i*j),end=" ")
        print('')

if __name__ == '__main__':

    get99()

