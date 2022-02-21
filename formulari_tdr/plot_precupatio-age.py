from cProfile import label
import data
import matplotlib.pyplot as plt

respostes = data.get()

def average_precupation(age:int):
    temp = []
    for resposta in respostes:
        if resposta["age_int"] == age:
            temp.append(resposta["Precupacio"])
            
    return sum(temp) / len(temp) * 10

def num_responses(age:int):
    i = 0
    for resposta in respostes:
        if resposta["age_int"] == age:
            i += 1
            
    return i

def num_knows(age:int):
    i = 0
    n = 0
    for resposta in respostes:
        if resposta["age_int"] == age:
            i += resposta["knows"]
            n += 1
             
    return i/n*100

precupations = []
n = []
knows =  []
ages = [12, 16, 19, 26, 36, 46, 56, 65]

for age in ages:
    precupations.append(average_precupation(age))
    n.append(num_responses(age))
    knows.append(num_knows(age))

plt.plot(ages, precupations, label="Precupation")
plt.plot(ages, n, label="Responses")
plt.plot(ages, knows, label="Knows")
 
# naming the x axis
plt.ylabel('perecupartion')
# naming the y axis
plt.xlabel('age')
 
# giving a title to my graph
plt.title('Precupation - Age')
 
# function to show the plot
plt.show()