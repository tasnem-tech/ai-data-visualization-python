import pandas as pd
import matplotlib.pyplot as plt

# full path of dataset
data = pd.read_csv(r"C:\Users\User\Downloads\ai_company_adoption.csv")

# create scatter plot
plt.scatter(data["ai_maturity_score"], data["productivity_change_percent"])

# labels
plt.xlabel("AI Maturity Score")
plt.ylabel("Productivity Change (%)")
plt.title("AI Maturity vs Productivity Change")

# show graph
plt.show()