import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
scores = [75, 80, 60, 90, 70]

plt.plot(days, scores, color="red", linestyle="dotted")
plt.title("My quiz score tracker")
plt.ylabel("Score")
plt.xlabel("Days of the week")
plt.grid(True)
plt.show()

plt.bar(days, scores, color = "orange")
plt.title("My quiz score bar chart")
plt.ylabel("Score")
plt.xlabel("Days of the week")
plt.ylim(0, 100)
plt.show()