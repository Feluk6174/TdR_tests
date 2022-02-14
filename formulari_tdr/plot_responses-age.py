import data
import matplotlib.pyplot as plt

respostes = data.get()

def num_responses(age:int):
    i = 0
    for resposta in respostes:
        if resposta["age_int"] == age:
            i += 1
            
    return i

n = []
ages = [12, 16, 19, 26, 36, 46, 56, 65]

for age in ages:
    n.append(num_responses(age))

plt.plot(ages, n)
 
# naming the x axis
plt.ylabel('perecupartion')
# naming the y axis
plt.xlabel('age')
 
# giving a title to my graph
plt.title('Precupation - Age')
 
# function to show the plot
plt.show()