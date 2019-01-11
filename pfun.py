import numpy
A = numpy.array([[3, 4, 5], [5,6,7], [8,9,10]])
B = numpy.array([1,9,0])
#print(numpy.row_stack((A, B)))
#print(numpy.column_stack((A, B)))
#print(numpy.shape(A))
#print(A)


C = numpy.array([
    [
        [1, 2, 3], [4,5,6]
    ],
    [
        [11,22,33], [44,55,66]
    ]
])
print(numpy.shape(C))
print(C)

#A = numpy.array([[3, 4, 5],
              [1, 9, 0],
              [4, 6, 8]])
#numpy.column_stack((A, A, A))
#print(numpy.shape(A))

x = numpy.array([2,5,18,14,4])
y = x[:, numpy.newaxis, numpy.newaxis]
print(y)
A = pd.read_csv("/home/bid/Desktop/noquote.csv", sep=",", header=None)
print(data2)



















