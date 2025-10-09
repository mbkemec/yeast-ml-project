#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

cols = ["seq_name","mcg","gvh","alm","mit","erl","pox","vac","nuc","class"]
df = pd.read_csv("../data/yeast.data", sep="\\s+", names=cols)
numeric_cols = df.drop(columns=["seq_name","class"]).columns

plt.style.use("dark_background")
sns.set_theme(style="darkgrid")


plt.figure(figsize=(15, 10))

#Class Distribution
plt.subplot(2, 2, 1)
class_counts = df["class"].value_counts().reset_index()
class_counts.columns = ["class", "count"]
sns.barplot(data=class_counts, x="class", y="count", hue="class", palette="viridis", legend=False)
plt.title("Class Distribution")
plt.xticks(rotation=45)

# Correlation Among Classes
plt.subplot(2, 2, 2)
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap="rocket", fmt=".2f")
plt.title("Feature Correlation Matrix")

# PCA
plt.subplot(2, 1, 2)
X = df[numeric_cols]
y = df["class"]
pca = PCA(n_components=2)
pca_result = pca.fit_transform(X)
pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"])
pca_df["class"] = y

sns.scatterplot(data=pca_df, x="PC1", y="PC2", hue="class", palette="tab10", s=40, alpha=0.8)
plt.title("PCA")
plt.legend()


plt.tight_layout()
plt.savefig("../data_explore_overview.png", dpi=300, bbox_inches="tight")
plt.show()
