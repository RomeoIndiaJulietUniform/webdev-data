import matplotlib.pyplot as plt
from pytrends.request import TrendReq

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define the search terms
search_terms = ["Frontend Development", "FullStack Development", "Backend Development", "Node.js", "SpringBoot"]

# Build the payload
pytrends.build_payload(search_terms, timeframe='today 5-y')

# Get the interest over time
data = pytrends.interest_over_time()

# Define a custom color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Plot the data
plt.figure(figsize=(10, 6))
for i, term in enumerate(search_terms):
    plt.plot(data[term], label=term, color=colors[i])

plt.title('Realtime Automated in Development Technologies over Time')
plt.xlabel('Year')
plt.ylabel('Interest')
plt.legend()
plt.grid(True)
plt.savefig('development_tech_interest.png')
plt.show()
