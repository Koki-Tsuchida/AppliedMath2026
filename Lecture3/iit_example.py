import matplotlib.pyplot as plt

systems = ["Independent sensors", "Connected sensors"]
phi_values = [0, 1]

plt.bar(systems, phi_values)
plt.ylabel("Integrated Information (phi)")
plt.title("Simple Example of IIT")

plt.show()
