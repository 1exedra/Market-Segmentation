import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    sse.append(kmeans.inertia_)


plt.plot(range(1, 11), sse, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('SSE')
plt.title('Elbow Method')
plt.show()

kmeans = KMeans(n_clusters=4, random_state=42)
customer_data['Cluster'] = kmeans.fit_predict(features_scaled)
