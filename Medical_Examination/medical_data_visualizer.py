import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import sys

# Import data
df = pd.read_csv('medical_examination.csv')
# Add 'overweight' column
df['overweight'] = np.where(df['weight'] > ((df['height']/100)**2 * 25), 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = df['gluc'].map(lambda x: 1 if x > 1 else 0)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='value')

    
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(by="cardio").value_counts()).reset_index()
    
    df_cat.columns.values[-1] = "total"
    
    
    # Draw the catplot with 'sns.catplot()'
   
    # Get the figure for the output
    cat_plot =  sns.catplot(
    data=df_cat, x="variable", y="total", col="cardio", hue='value', kind="bar", height=4, aspect=.6, order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    fig = cat_plot.fig
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    press = (df['ap_lo'] <= df['ap_hi'])
    height_cond = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    weight_cond = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    
    df_heat = df[press & height_cond & weight_cond]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    
    
    fig, ax = plt.subplots(figsize=(10,10))         # Sample figsize in inches
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt=".1f")    
    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
