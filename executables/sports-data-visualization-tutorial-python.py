# Import necessary libraries
import plotly.express as px
from bokeh.plotting import figure, save
from bokeh.io import output_file
import pandas as pd

# Load the College Basketball dataset
basketball_data = pd.read_csv('cbb25.csv')


# Preview the dataset
print(basketball_data.head())

# Example 1: Bar Plot - Number of Games Played by Conference
fig_bar = px.bar(basketball_data, x='CONF', y='G', 
                 title='Number of Games Played by Conference', 
                 color='CONF', barmode='group')
fig_bar.write_image("games_by_conference.png")  # Save the plot as a PNG file

# Example 2: Scatter Plot - Adjusted Offensive Efficiency vs Defensive Efficiency
fig_scatter = px.scatter(basketball_data, x='ADJOE', y='ADJDE', 
                         title='Adjusted Offensive vs Defensive Efficiency', 
                         color='Team', hover_data=['RK', 'CONF'])
fig_scatter.write_image("offense_vs_defense.png")  # Save the plot as a PNG file

# Example 3: Bokeh Plot - Adjusted Offensive Efficiency by Team
# Define the output file for the Bokeh plot
output_file("adjusted_offensive_efficiency.html")
# Create the Bokeh figure
p_line = figure(title="Adjusted Offensive Efficiency by Team", 
                x_range=basketball_data['Team'], 
                x_axis_label='Team', 
                y_axis_label='Adjusted Offensive Efficiency (ADJOE)', 
                tools="pan,wheel_zoom,box_zoom,reset", 
                width=1000, height=600)
# Add a line plot
p_line.line(basketball_data['Team'], basketball_data['ADJOE'], 
            legend_label="ADJOE", line_width=2, line_color="blue")
# Add hover tool for interactivity
from bokeh.models import HoverTool
hover = HoverTool()
hover.tooltips = [("Team", "@x"), ("Adjusted Offensive Efficiency", "@y")]
p_line.add_tools(hover)
# Rotate the x-axis labels for better readability
p_line.xaxis.major_label_orientation = 1.2
# Save Bokeh plot as an HTML file
save(p_line)
print("All plots saved successfully!")
