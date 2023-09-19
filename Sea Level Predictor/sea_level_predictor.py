import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
   
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c="red")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    print(df['Year'])
    plt.plot(range(1880, 2051, 1), range(1880,2051,1)*regression.slope + regression.intercept, c="black")
    plt.scatter(2051, regression.slope*2051 + regression.intercept, c="lime", s=100)
    print(df.loc[df['Year']>=2000, 'Year'])
    regression = linregress(df.loc[df['Year']>=2000, 'Year'], df.loc[df['Year']>=2000, 'CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), range(2000,2051,1)*regression.slope + regression.intercept, c="blue")
    plt.scatter(2050, regression.slope*2050 + regression.intercept, c="gold", s=100)
    plt.legend(["CSIRO Adjusted Sea Level", "Linear regression(1880-2050)", "Year: 2050", "Linear regression(Years:2000-2050)", "Year: 2050 (Data used: 2000-2050)"], loc="best")
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()