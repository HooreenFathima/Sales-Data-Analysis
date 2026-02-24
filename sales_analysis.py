import pandas as pd

#read and load data
try :
    df=pd.read_csv('sales_data.csv')
    print("Data loaded Successfully. ")
except FileNotFoundError:
    print(" Error : File Not Found ")
    exit()

#checking any mssing values
if df.isnull().values.any():
    print(" Found missing values , Filling with 0/default ")
    df=df.fillna(0)
else :
    print(" No Missing Values Found ")

#Calculating atlleast 3 different metrices
#Metric 1 : Total Revenue
total_revenue = df['Total_Sales'].sum()

#Metric 2 : Best selling product by quantity sold
product_sales = df.groupby('Product')['Quantity'].sum()
best_product = product_sales.idxmax()
best_product_qty = product_sales.max()

#Metric 3 : best performing region by total revenue
region_sales = df.groupby('Region')['Total_Sales'].sum()
top_region = region_sales.idxmax()
top_region_revenue = region_sales.max()

#REPORT
print("\n---------------------------------------------------------------------")
print("--------------------------SALES ANALYSIS REPORT------------------------")
print("\n---------------------------------------------------------------------")
print(f"Total Transactions Processed            : {len(df)}")
print(f"Total Revenue                           : {total_revenue}")
print(f"Best Selling Product by Quantity        : {best_product} {best_product_qty}units ")
print(f"Top Perfforming Region by Total Revenue : {top_region} (${top_region_revenue:,.2f})")
print("\n----------------------------------------------------------------------")
print(f"Key Insight : Focus Marketing on {best_product} in the {top_region} region ")
print("\n----------------------------------------------------------------------")
df.to_csv('cleaned_sales_data.csv',index=False)
print("\n Submission ready : 'cleaned_data.csv' created. ")
      
