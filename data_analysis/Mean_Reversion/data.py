import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#function for MA calculation based on passed period
def calculate_MA(period, ma, spread):
    k = 0

    while k < len(spread) - period + 1:
        ma.append(round(sum(spread[k:k+period])/period, 2))
        k = k+1

#function for calculation of mean reversion probability
def spread_frequency(spread, ma, period):
    
    k=0
    j=period-1
    TickMove = []
    
    while(j<len(spread)):
        if (abs(spread[j]-ma[k]) > 0.10):
            TickMove.append(j)
        k=k+1
        j=j+1

    return TickMove

#function to determine how trade played out after 20+ tick move and with max 3 hour time window
def check_mean_reversion_play(spread, ma, freq, maxTime, period):

    prob = {}
    flag=False

    for i in freq: #Check all entrie, every spot where spread made 20-tick move away from mean
        for j in range(1,maxTime+1): #Check next 9 20-min periods, 3 hours
            
            if(spread[i+j] <= ma[i-(period-1)+j] and spread[i] > ma[i-(period-1)]): #
                if(ma[i-(period-1)+j] < spread[i]):
                    flag=True
                    break
            elif(spread[i+j] >= ma[i-(period-1)+j] and spread[i] < ma[i-(period-1)]):
                if(ma[i-(period-1)+j] > spread[i]):
                    flag=True
                    break
        if(flag):
            prob[i] = True
        else:
            prob[i] = False
        flag=False

    return prob

def plot_results(prob, ma, period, spread):

    plt.plot(range(0, len(ma)), spread[period-1:])
    plt.plot(range(0, len(ma)), ma)

    short_true = [i for i,j in prob.items() if j == True]
    short_false = [i for i,j in prob.items() if j == False]

    print(f"Percentage of successful reversions({period}-MA): {round(len(short_true)/len(prob) * 100,2)}%")
    print(f"Percentage of unsuccessful reversions({period}-MA): {round(len(short_false)/len(prob) * 100, 2)}%")

    plotY1= [spread[i] for i in short_true]
    plotY2 = [spread[i] for i in short_false]
    plt.scatter([i-(period-1) for i in short_true], plotY1, c="g")
    plt.scatter([i-(period-1) for i in short_false], plotY2, c="r")
    plt.legend(["Spread", f"{period}-MA", "Successful Reversion", "Unsuccessful Reversion"], loc ="best")
    plt.show()


#Read Excel file that contains data for FGBL & FBTP
df = pd.read_excel('data.xlsx')

#Take closing prices of FGBL & FBTP
fgbl = df["Close"]
fbtp = df["Close.1"]

#Calculate spread between FBTP & FGBL = FBTP - FGBL
spread = [btp - gbl for (btp, gbl) in zip(fbtp, fgbl)]

#Calculate moving average

max_time = 3*3 #3 hours is max time for mean reversion, in 1 hour there are 3 20 min periods, in 3 hours 9 periods

short_period = 10 #10 period MA
long_period = 20 #20 period MA

ma10 = []
ma20 = []

#Calculate moving averages, 10 and 20 period
calculate_MA(short_period, ma10, spread)
calculate_MA(long_period, ma20, spread)

#Check if price reverts to the mean, max time for that is 3 hours

freq1 = spread_frequency(spread, ma10, short_period) #Frequency of 20-tick moves for 10MA, function return indices when 20+ tick moves happened
freq2 = spread_frequency(spread, ma20, long_period)  #Frequency of 20-tick moves for 20MA, function return indices when 20+ tick moves happened


prob1 = check_mean_reversion_play(spread, ma10, freq1, max_time, short_period) #Returns dictionary that for every move has True/False value which is set based on what happened after that in 3 hour time window, 10MA
prob2 = check_mean_reversion_play(spread, ma20, freq2, max_time, long_period) #Returns dictionary that for every move has True/False value which is set based on what happened after that in 3 hour time window, 20MA

prob= [prob1, prob2]
ma = [ma10, ma20]
period = [10, 20]

for i in range(0,2):
    plot_results(prob[i], ma[i], period[i], spread)
