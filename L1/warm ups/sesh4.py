import matplotlib.pyplot as plt

#E1
x = [1, 3, 6, 9, 16]
y = [7, 3, 7, 1, 5]
y2 = [9, 5, 5, 2, 6]
y3 = [4, 6, 2, 6, 8]
y4 = [1, 8, 1, 3, 2]

#E2
plt.plot(x,y,color='black')
plt.plot(x,y2,color='blue')
plt.plot(x,y3,color='red')
plt.plot(x,y4,color='yellow')

#E3
plt.title('Line graph')
plt.xlabel('time')
plt.ylabel('y')
plt.show()

#E4
