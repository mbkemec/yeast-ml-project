#!/usr/bin/env python3
"""
# In this script, i split the data into %75 training set and %25 test (benchmark) set!
# After splitting 75-25, i also split the train set into 3 sub-fold for cross validation.
# I split 3 folds because the data is not big and the class distributions are not balanced.
# That's why i dont want to miss the small class in the both training and benchmark dataset.
# So, i split the data with certain rules in all folds and protect the class distribution ratio.
"""

import pandas as pd

cols = ["seq_name","mcg","gvh","alm","mit","erl","pox","vac","nuc","class"]
df = pd.read_csv("../data/yeast.data", sep=r"\s+", names=cols)

# Shuffle
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Adding fold column
df["fold"] = None

# Define the order (benchmark is -1 & 3 folds for training and cross-validation)
fold_order = [-1, 0, 1, 2]

for cls in df["class"].unique():
	# Start a loop for every class, so class distribution made by separately!!

    class_indices = df.index[df["class"] == cls].tolist()
    # Take index numbers

    # assign folds in repeating pattern -1,0,1,2
    for i, idx in enumerate(class_indices):
		# Take order and index at the same time!
        df.at[idx, "fold"] = fold_order[i % len(fold_order)]
        # Distribute every sample in every class one by one into the folds!
        # So we can sure every fold contains every class!!


df.to_csv("../data/yeast_folds.tsv", sep="\t", index=False)
df[["seq_name","fold"]].to_csv("../data/fold_index.tsv", sep="\t", index=False)

print("Splitting completed and files saved!(the final file is: yeast_folds.tsv)(the sharable version is: fold_index.tsv)")
print("You can see the sample size for each fold:")
print(df["fold"].value_counts().sort_index())
print()
print("Class distribution by fold:")
print(df.groupby(["fold","class"]).size().unstack())
