---
layout: post
title: "Interactive Sports Data Visualization with Python"
date: 2025-02-18
description: "Enhancing sports analytics with interactive visualizations using Plotly and Bokeh."
categories: [data-science, sports-analytics]
image: "/assets/img/sports_visualization_banner.jpg"
display_image: true
permalink: /sports_data_visualization/2025/04/07/sports-data-visualization.html
---

# Interactive Sports Data Visualization with Python

## Introduction
Sports analytics enables teams, athletes, and fans to understand performance and make data-driven decisions. Interactive data visualization adds an exciting dimension by allowing dynamic exploration of sports datasets. This tutorial introduces interactive visualizations using Plotly and Bokeh, helping you uncover insights hidden within the data.

---

## Prerequisites
- Basic understanding of Python programming
- Installation of required libraries (`Plotly`, `Bokeh`)

---

## Step-by-Step Guide to Interactive Sports Visualizations

### Step 1: Install Required Libraries
Run the following commands to install the required Python libraries:
```bash
pip install plotly bokeh
```
### Step 2: Import Libraries and Load Data
Import the necessary libraries and load your sports dataset. For this example, we’ll use a college basketball 2025 dataset:
```python
import plotly.express as px
from bokeh.plotting import figure, show
from bokeh.io import output_file
import pandas as pd

# Load the College Basketball dataset
# Replace 'path_to_dataset.csv' with the actual path to your downloaded dataset
#basketball_data = pd.read_csv('path_to_dataset.csv')
basketball_data = pd.read_csv('Documents/BYU/STAT-386/Blog-2/executables/cbb25.csv')

# Preview the dataset
print(basketball_data.head())
```
### Step 3: Create Interactive Plots with Plotly
Plotly makes it simple to create dynamic and interactive charts.

Bar Plot Example
```python
# Example: Bar Plot - Number of Games Played by Conference
fig = px.bar(basketball_data, x='CONF', y='G', title='Number of Games Played by Conference', color='CONF', barmode='group')
fig.show()
```
It should look like this:
![Bar Plot]({{site.url}}{{site.baseurl}}/assets/img/games_by_conference.png)

Scatter Plot Example
```python
# Example: Scatter Plot - Adjusted Offensive Efficiency vs Defensive Efficiency
fig = px.scatter(basketball_data, x='ADJOE', y='ADJDE', title='Adjusted Offensive vs Defensive Efficiency', color='TEAM', hover_data=['RK', 'CONF'])
fig.show()
```
It should look like this:
![Scatter Plot]({{site.url}}{{site.baseurl}}/assets/img/offensive_vs_defensive.png)


### Step 4: Create Interactive Plots with Bokeh
Bokeh enables embedding detailed interactive charts into web applications.

Line Plot Example
Tracking player performance over matches:
```python
# Add hover tool for interactivity
from bokeh.models import HoverTool
hover = HoverTool()
hover.tooltips = [("Year", "@x"), ("Wins Above Bubble", "@y")]
p.add_tools(hover)

show(p)
```
It should look like this:
![Bokeh Plot]({{site.url}}{{site.baseurl}}/assets/img/adjusted_offensive_efficiency.html)

### Step 5: Explore Advanced Customization Options
Enhance interactivity further with dropdown filters, animations, or by combining features of both libraries.

## Conclusion
Interactive data visualization transforms sports analytics by enabling deeper exploration and understanding. Libraries like Plotly and Bokeh empower users to go beyond static graphs, creating dynamic and insightful visual stories. Experiment with these tools and let your data tell compelling sports stories!

## Resources
- **GitHub Repository**: 

