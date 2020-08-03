import matplotlib.pyplot as plt
plt.plot(gdp_cap,life_exp)

# Display the plot
plt.show()

plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()