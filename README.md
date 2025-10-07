# Yeast Protein Localization -- Applied Machine Learning Project

This project uses the **Yeast Protein Localization Dataset** from the UCI Machine Learning Repository.

- Source: [UCI Yeast Dataset](https://archive.ics.uci.edu/dataset/110/yeast)
- File: `yeast.data`
- Description: 1,484 samples, 8 features, 10 classes.

To use this project:
1. Download `yeast.data` from the source
2. Save it in the `data/` folder at this repository.

## Dataset Overview
- **Number of instances**: 1,484
- **Number of features**: 8 numerical
- **Number of classes**: 10 localization sites
- **Missing values**: None
- **License**: Original dataset is not included in this repository. Please download it directly from UCI.

### Data Structure

| Column Type       | Count | Description |
|-------------------|-------|-------------|
| Sequence Name     | 1     | Protein ID (SWISS-PROT accession) — not used for modeling |
| Numerical Features| 8     | mcg, gvh, alm, mit, erl, pox, vac, nuc |
| Class Label       | 1     | Protein localization site (10 classes) |

## Features Description

| Feature | Description |
|---------|-------------|
| `mcg`  | McGeoch's method for signal sequence recognition |
| `gvh`  | von Heijne's method for signal sequence recognition |
| `alm`  | ALOM membrane spanning region score |
| `mit`  | N-terminal amino acid discriminant score (mitochondrial vs non) |
| `erl`  | Presence of “HDEL” ER retention signal (binary) |
| `pox`  | Peroxisomal targeting signal in the C-terminus |
| `vac`  | Vacuolar vs extracellular discriminant score |
| `nuc`  | Nuclear localization signal discriminant score |

##Class Distribution

| Class | Description                                | Count |
|-------|---------------------------------------------|-------|
| CYT   | Cytosolic or cytoskeletal                  | 463 |
| NUC   | Nuclear                                   | 429 |
| MIT   | Mitochondrial                            | 244 |
| ME3   | Membrane (no N-terminal signal)          | 163 |
| ME2   | Membrane (uncleaved signal)              | 51 |
| ME1   | Membrane (cleaved signal)                | 44 |
| EXC   | Extracellular                           | 37 |
| VAC   | Vacuolar                               | 30 |
| POX   | Peroxisomal                           | 20 |
| ERL   | Endoplasmic reticulum lumen          | 5 |
