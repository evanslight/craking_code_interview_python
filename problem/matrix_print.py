# given a matrix with integers. please print it in the spiral order way
# the space complexity should be O(1)
import numpy as np
class matrix():
    def spiralOrderPrint(self, matrixdata):

        sR = 0
        sC = 0
        eR = matrixdata.shape[0] - 1
        eC = matrixdata.shape[1] - 1
        while (sR <= eR and eR <= eC):
            self.printEdge(matrixdata, sR, sC, eR, eC)
            sR += 1
            sC += 1
            eR -= 1
            eC -= 1

    def printEdge(self, matrix, sR, sC, eR, eC):
        if (sR == eR):
            for i in range(sC, eC+1):
                print(matrix[sR][i]," ")
        elif (sC == eC):
            for i in range(sR, eR+1):
                print(matrix[i][sC]," ")
        else:
            cursC = sC
            cursR = sR
            while (cursC < eC):
                print(matrix[sR][cursC]," ")
                cursC += 1
            while (cursR < eR):
                print(matrix[cursR][eC])
                cursR += 1
            while (cursC > sC):
                print(matrix[eR][cursC])
                cursC -= 1
            while (cursR > sR):
                print(matrix[cursR][sC])
                cursR -= 1



if __name__ == "__main__":
    matrixNum = np.random.randint(100, size=(5, 5))
    print(matrixNum)
    matrixPrint = matrix()
    matrixPrint.spiralOrderPrint(matrixNum)

