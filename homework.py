import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
savings = [110, 85, 70, 90, 150]

plt.plot(days, savings)
plt.title('My Savings Progress Chart')
plt.xlabel('Days Of The Week')
plt.ylabel('Savings')
plt.grid(True)
plt.ylim(0, 200)
plt.show()

plt.bar(days, savings, color='green')
plt.title('My Savings Bar Chart')
plt.xlabel('Days')
plt.ylabel('Savings')
plt.ylim(0, 200)
plt.show()
