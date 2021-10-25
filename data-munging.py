import pandas as pd
#import glob
#import os
from datetime import datetime, timedelta

now = datetime(2012, 11, 22, 0, 0, 0)
last = datetime(2012, 11, 22, 23, 59, 59)
delta = timedelta(seconds=1)
times = []
while now <= last:
    times.append(now.strftime("%H:%M:%S"))
    now += delta

#path = r"eco\04_plugs_csv\01"
#all_files = glob.glob(path + "/*.csv")
#li = []
#for filename in all_files:
    #df = pd.read_csv(filename, index_col=None, header=None)
    #df["time"] = os.path.basename(filename)
    #li.append(df)

df1 = pd.read_csv("eco/04_plugs_csv/01/2012-11-22.csv", index_col=None, header=None)
df2 = pd.read_csv("eco/04_plugs_csv/02/2012-11-22.csv", index_col=None, header=None)
#df3 = pd.read_csv("eco/04_plugs_csv/03/2012-11-22.csv", index_col=None, header=None)
#df4 = pd.read_csv("eco/04_plugs_csv/04/2012-11-22.csv", index_col=None, header=None)
df5 = pd.read_csv("eco/04_plugs_csv/05/2012-11-22.csv", index_col=None, header=None)
df6 = pd.read_csv("eco/04_plugs_csv/06/2012-11-22.csv", index_col=None, header=None)
df7 = pd.read_csv("eco/04_plugs_csv/07/2012-11-22.csv", index_col=None, header=None)
df8 = pd.read_csv("eco/04_plugs_csv/08/2012-11-22.csv", index_col=None, header=None)

df = [df1, df2, df5, df6, df7, df8]

for i in df:
    i.columns = ["consumption"]
    i["time"] = times
    i["householdID"] = "04"
    
df1 = df1[-df1.consumption.isin([-1])]
df2 = df2[-df2.consumption.isin([-1])]
#df3 = df3[-df3.consumption.isin([-1])]
#df4 = df4[-df4.consumption.isin([-1])]
df5 = df5[-df5.consumption.isin([-1])]
df6 = df6[-df6.consumption.isin([-1])]
df7 = df7[-df7.consumption.isin([-1])]
df8 = df8[-df8.consumption.isin([-1])]

df1["appliance"] = "Fridge"
df2["appliance"] = "Kitchen appliances"
#df3["appliance"] = "Lamp"
#df4["appliance"] = "Stereo and laptop"
df5["appliance"] = "Freezer"
df6["appliance"] = "Tablet"
df7["appliance"] = "Entertainment"
df8["appliance"] = "Microwave"

df = [df1, df2, df5, df6, df7, df8]
df_04 = pd.concat(df, axis=0, ignore_index=True)
#df_04.to_csv("household04.csv")


df1 = pd.read_csv("eco/05_plugs_csv/01/2012-11-22.csv", index_col=None, header=None)
df2 = pd.read_csv("eco/05_plugs_csv/02/2012-11-22.csv", index_col=None, header=None)
#df3 = pd.read_csv("eco/05_plugs_csv/03/2012-11-22.csv", index_col=None, header=None)
df4 = pd.read_csv("eco/05_plugs_csv/04/2012-11-22.csv", index_col=None, header=None)
df5 = pd.read_csv("eco/05_plugs_csv/05/2012-11-22.csv", index_col=None, header=None)
df6 = pd.read_csv("eco/05_plugs_csv/06/2012-11-22.csv", index_col=None, header=None)
df7 = pd.read_csv("eco/05_plugs_csv/07/2012-11-22.csv", index_col=None, header=None)
#df8 = pd.read_csv("eco/05_plugs_csv/08/2012-11-22.csv", index_col=None, header=None)

df = [df1, df2, df4, df5, df6, df7]

for i in df:
    i.columns = ["consumption"]
    i["time"] = times
    i["householdID"] = "05"
    
df1 = df1[-df1.consumption.isin([-1])]
df2 = df2[-df2.consumption.isin([-1])]
#df3 = df3[-df3.consumption.isin([-1])]
df4 = df4[-df4.consumption.isin([-1])]
df5 = df5[-df5.consumption.isin([-1])]
df6 = df6[-df6.consumption.isin([-1])]
df7 = df7[-df7.consumption.isin([-1])]
#df8 = df8[-df8.consumption.isin([-1])]

df1["appliance"] = "Tablet"
df2["appliance"] = "Coffee machine"
#df3["appliance"] = "Fountain"
df4["appliance"] = "Microwave"
df5["appliance"] = "Fridge"
df6["appliance"] = "Entertainment"
df7["appliance"] = "PC"
#df8["appliance"] = "Kettle"

df = [df1, df2, df4, df5, df6, df7]
df_05 = pd.concat(df, axis=0, ignore_index=True)
#df_05.to_csv("household05.csv")


df1 = pd.read_csv("eco/06_plugs_csv/01/2012-11-22.csv", index_col=None, header=None)
df2 = pd.read_csv("eco/06_plugs_csv/02/2012-11-22.csv", index_col=None, header=None)
#df3 = pd.read_csv("eco/06_plugs_csv/03/2012-11-22.csv", index_col=None, header=None)
df4 = pd.read_csv("eco/06_plugs_csv/04/2012-11-22.csv", index_col=None, header=None)
df5 = pd.read_csv("eco/06_plugs_csv/05/2012-11-22.csv", index_col=None, header=None)
df6 = pd.read_csv("eco/06_plugs_csv/06/2012-11-22.csv", index_col=None, header=None)
df7 = pd.read_csv("eco/06_plugs_csv/07/2012-11-22.csv", index_col=None, header=None)

df = [df1, df2, df4, df5, df6, df7]

for i in df:
    i.columns = ["consumption"]
    i["time"] = times
    i["householdID"] = "06"
    
df1 = df1[-df1.consumption.isin([-1])]
df2 = df2[-df2.consumption.isin([-1])]
#df3 = df3[-df3.consumption.isin([-1])]
df4 = df4[-df4.consumption.isin([-1])]
df5 = df5[-df5.consumption.isin([-1])]
df6 = df6[-df6.consumption.isin([-1])]
df7 = df7[-df7.consumption.isin([-1])]

df1["appliance"] = "Lamp"
df2["appliance"] = "Laptop"
#df3["appliance"] = "Router"
df4["appliance"] = "Coffee machine"
df5["appliance"] = "Entertainment"
df6["appliance"] = "Fridge"
df7["appliance"] = "Kettle"

df = [df1, df2, df4, df5, df6, df7]
df_06 = pd.concat(df, axis=0, ignore_index=True)
#df_06.to_csv("household06.csv")


df = [df_04, df_05, df_06]
df_final = pd.concat(df, axis=0, ignore_index=True)
df_final.to_csv("household.csv", index=False)
