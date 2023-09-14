import pandas as pd
import openpyxl
from finvizfinance.group.performance import Performance
from finvizfinance.screener.performance import Performance as PerformanceStocks

def write_to_excel(df, Sheet):
    
    existing_data = pd.read_excel('Market_Breadth.xlsx', engine='openpyxl')

    # Write the new data to the existing file without overwriting its previous data
    with pd.ExcelWriter('Market_Breadth.xlsx', engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:
        df.to_excel(writer, sheet_name=f'{Sheet}', index=False)

    print(f"{Sheet}: DONE!")

def update_data(df, flag):

    if(flag == 'Stocks'):
        del df["Price"]
        del df["Volatility W"]
        del df["Volatility M"]

    elif(flag == 'Industries' or flag == 'Sectors'):
        del df["Change"]
   
    del df["Perf Year"]
    del df["Recom"]
    del df["Avg Volume"]
    del df["Rel Volume"]
    del df["Volume"]
    

def week_transform(df, col):
     for i in range(0, len(df)):
        df[col][i] = float(df[col][i].replace("%",""))/100.

def get_stocks():
    
    foverview = PerformanceStocks()
    filters_dict = {"Price": "Over $1"}
    foverview.set_filter(filters_dict=filters_dict)
    df = foverview.screener_view()
    
    update_data(df, 'Stocks')
    write_to_excel(df, 'Stocks')

def get_sectors():
    
    foverview = Performance()
    df = foverview.screener_view()

    update_data(df, 'Sectors')
    week_transform(df, "Perf Week")
    write_to_excel(df, 'Sectors')


def get_industries():
    
    foverview = Performance()
    df = foverview.screener_view("Industry", "Performance (Week)")

    update_data(df, 'Industries')
    week_transform(df, "\n\nPerf Week")
    write_to_excel(df, 'Industries')

get_stocks()
get_sectors()
get_industries()

print("FINISHED!")