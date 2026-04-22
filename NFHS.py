import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.outliers_influence import variance_inflation_factor

sns.set(style="whitegrid")

df = pd.read_excel("C:/Users/srikar mourya/Downloads/Int375project/NFHS_5_Factsheets_Data.xls")

print("Shape:", df.shape)
print(df.head())
print(df.info())

df.fillna(0, inplace=True)

numeric_df = df.select_dtypes(include=np.number)

if numeric_df.shape[1] < 5:
    numeric_df = df.iloc[:, 1:6].apply(pd.to_numeric, errors='coerce').fillna(0)

cols = numeric_df.columns[:5]

plt.figure(figsize=(10,5))
plt.plot(numeric_df[cols[0]])
plt.title(f"{cols[0]} Trend")
plt.xlabel("Index")
plt.ylabel(cols[0])
plt.show()

plt.figure(figsize=(10,5))
numeric_df[cols].sum().plot(kind='bar')
plt.title("Sum of Selected Indicators")
plt.show()

plt.figure(figsize=(8,5))
plt.hist(numeric_df[cols[0]], bins=30)
plt.title(f"Distribution of {cols[0]}")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df[cols].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(data=numeric_df[cols])
plt.title("Boxplot for Outliers")
plt.show()

sns.pairplot(numeric_df[cols])
plt.show()

plt.figure(figsize=(10,5))
sns.violinplot(data=numeric_df[cols])
plt.title("Violin Plot")
plt.show()

plt.figure(figsize=(8,5))
sns.regplot(x=numeric_df[cols[0]], y=numeric_df[cols[1]])
plt.title("Regression Plot")
plt.show()

print("\nSummary Statistics:\n", numeric_df.describe())
print("\nCorrelation Matrix:\n", numeric_df.corr())

sample = numeric_df[cols[0]].sample(min(100, len(numeric_df)))

z_score = (sample.mean() - numeric_df[cols[0]].mean()) / (sample.std()/np.sqrt(len(sample)))
print("\nZ-score:", z_score)

t_stat, p_val = stats.ttest_1samp(sample, numeric_df[cols[0]].mean())
print("T-test:", t_stat, p_val)

observed = np.array([10, 20, 30])
expected = np.array([15, 15, 30])
chi, p = stats.chisquare(observed, expected)
print("Chi-square:", chi, p)

if len(sample) >= 3:
    shapiro_test = stats.shapiro(sample)
    print("Shapiro Test:", shapiro_test)

vif_data = numeric_df[cols].fillna(0)

vif = pd.DataFrame()
vif["Feature"] = vif_data.columns
vif["VIF"] = [variance_inflation_factor(vif_data.values, i) for i in range(len(vif_data.columns))]
print("\nVIF:\n", vif)

print("\nNormal Dist Mean:", np.mean(sample))

binomial = np.random.binomial(n=10, p=0.5, size=1000)
poisson = np.random.poisson(lam=5, size=1000)
uniform = np.random.uniform(0,1,1000)

group_A = numeric_df[cols[0]].sample(min(50, len(numeric_df)))
group_B = numeric_df[cols[1]].sample(min(50, len(numeric_df)))

t_stat_ab, p_val_ab = stats.ttest_ind(group_A, group_B)
print("\nA/B Test:", t_stat_ab, p_val_ab)
