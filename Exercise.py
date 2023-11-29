import matplotlib.pyplot as plt

age = [ 20,25,30,35,40,45,50,55]
edeucation = [16,18,22,24,26,28,30,32]

plt.plot(age, edeucation)

plt.xlabel('Age')
plt.ylabel('Years of Education')
plt.title('Relationship between Age and Education')

plt.grid(True)


plt.show()