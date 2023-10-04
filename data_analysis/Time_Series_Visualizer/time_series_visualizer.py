import matplotlib.pyplot as plt
import pandas as pd
import sys
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

'''
 The label on the x axis should be Date and the label on the y axis should be Page Views
'''
# Clean data
cond = (df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))
df = df[cond]


def draw_line_plot():
    # Draw line plot
    
    fig, ax = plt.subplots()
    ax.plot(df.index, df['value'], c="r")
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    
    df_bar = df.groupby([(df.index.year), (df.index.month)], sort=True).sum()/df.groupby([(df.index.year), (df.index.month)], sort=True).count()
    
    fig, ax = plt.subplots(figsize=(10,10))
    df_bar = df_bar.unstack()
    df_bar.plot(ax = ax, kind='bar')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend([calendar.month_name[x[1]] for x in df_bar.columns], title="Months")
    

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2,figsize=(14, 8))
   
    sns.boxplot(ax=axes[0], data=df_box, x='year', y='value')
    sns.boxplot(ax=axes[1], data=df_box, x='month', y='value', order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[0].set_title("Year-wise Box Plot (Trend)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
