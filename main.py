# Project: Bank recovery analysis by regression

# Importing libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Read in dataset
df = pd.read_csv("datasets/bank_data.csv")
df.head()

# Plotting the relationship between age and recovery amount
plt.scatter(x=df['expected_recovery_amount'], y=df['age'], c="g", s=2)
plt.xlim(0, 2000)
plt.ylim(15, 60)
plt.xlabel("Expected Recovery Amount")
plt.ylabel("Age")
plt.legend(loc=2)
plt.show()
