# Market-Segmentation

In this elbow method the x-axis represents the number of clusters and the y-axis represents the sum of squared errors which measures the variance within each cluster


![image](https://github.com/1exedra/Market-Segmentation/assets/171572078/7a1623ec-cffd-4320-86bd-d9988e0be237)

Before the elbow (1 to 3 clusters): The SSE decreases significantly indicating that adding more clusters greatly reduces the variance within cluster

After the elbow (5 or more clusters): The SSE decreases more gradually so adding more clusters does not significantly improve the clustering results

The elbow is at 4 clusters which indicates that using 4 clusters will balance the trade-off between variance within clusters and the number of clusters

![image](https://github.com/1exedra/Market-Segmentation/assets/171572078/3183bcff-a3d5-4503-8529-5a862eae53fc)


The 3D scatter plot represents the customer segments identified by the K-Means clustering algorithm. The clusters are visualized based on three dimensions:

Purchase Frequency (x-axis), Total Spend (y-axis), and Average Purchase Value (z-axis). Each color represents a different cluster.

1. Cluster 0 (Purple):

Characteristics:


Low purchase frequency

Low total spend

Low average purchase value

Insight: This cluster likely represents customers who are infrequent buyers and have low spending habits. They might not be very engaged or high-value customers.

2. Cluster 1 (Blue):

Characteristics:


Moderate purchase frequency

Moderate total spend

Moderate average purchase value

Insight: These customers have a higher engagement level compared to Cluster 0. They make purchases more regularly and spend a moderate amount. They are a more valuable segment than Cluster 0 but not the highest spenders.

3. Cluster 2 (Green):

Characteristics:


High purchase frequency

High total spend

High average purchase value

Insight: This cluster represents high-value customers who purchase frequently and spend a lot. They are the most engaged and valuable segment and should be targeted with premium offers and personalized services.

Cluster 3 (Yellow):

Characteristics:

High total spend


High average purchase value


Low to moderate purchase frequency


Insight: These customers spend a lot on fewer purchases. They might be buying high-value items infrequently. They are an important segment for high-ticket items and might respond well to exclusive offers and high-end products.
