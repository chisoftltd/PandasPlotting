# Pandas - Plotting
# Plotting
import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('data.csv')
df.plot()
plt.show()

df = pd.read_csv('data1.csv')
df.plot()
plt.show()

# Scatter Plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

# Histogram
df["Duration"].plot(kind = 'hist')
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()