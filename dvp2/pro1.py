import pandas as pd
import plotly.express as px

# Load the data
churn_data = pd.read_csv(r"C:\Users\Charan TM\OneDrive\CoreTech\dvp lab\customer_churn.csv")

# Example: Assuming columns 'Segment' and 'Churn' exist
fig = px.treemap(
    churn_data,
    path=['Location','Company'],
    values='Churn',
    title="Customer Churn by Segment"
)
fig.show()
