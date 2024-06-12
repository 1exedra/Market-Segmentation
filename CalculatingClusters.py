import pandas as pd

file_path = '/mnt/data/Retail_1.csv'
data = pd.read_csv(file_path)

data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], format='%d-%m-%Y %H:%M')
data = data.dropna(subset=['CustomerID'])

customer_data = data.groupby('CustomerID').agg({
    'InvoiceNo': 'nunique',  
    'Quantity': 'sum',       
    'UnitPrice': 'mean'    
}).reset_index()

customer_data['TotalSpend'] = customer_data['Quantity'] * customer_data['UnitPrice']
customer_data['AveragePurchaseValue'] = customer_data['TotalSpend'] / customer_data['InvoiceNo']
features = customer_data[['InvoiceNo', 'TotalSpend', 'AveragePurchaseValue']]
