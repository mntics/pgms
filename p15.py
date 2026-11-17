# Dimension Reductions
# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns

# Load the Dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
print(df.head())

# Standardize the features
scalar = StandardScaler()
scaled_data = pd.DataFrame(scalar.fit_transform(df))
print(scaled_data)

# Apply PCA
pca = PCA(n_components=3)
pca.fit(scaled_data)
data_pca = pca.transform(scaled_data)
data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2', 'PC3'])

# Before PCA
plt.figure(figsize=(7, 5))
sns.heatmap(scaled_data.corr())
plt.title("Before PCA")
plt.show()

# After PCA
plt.figure(figsize=(7, 5))
sns.heatmap(data_pca.corr())
plt.title("After PCA")
plt.show()
