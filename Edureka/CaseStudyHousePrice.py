# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 22:30:01 2018

@author: Prashant Bhat
"""

"""
Import necessary librarires
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats

"""
Loading the data
"""

path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Kaggle\\HouseDataset\\"
df_train = pd.read_csv(path+"train.csv")

#Exploring the data through visualizations
"""
1.Print the columns in the loaded datasets
"""
print(list(df_train.columns))
"""
2.Print the data types of the columns
""" 
print(df_train.info())
"""
3.Sale Price is the one we need to predict
Describe the statistics of Sale Price
Explain:
    count:1460
    mean:180291
    std:79442
    min:34900
    25%:129975
    50%:163000
    75%:214000
    max:755000
"""
df_train['SalePrice'].describe()

"""
4.Plot a histogrm for Sale Price
seaborn using the distplot function
"""
sns.distplot(df_train['SalePrice'])

"""
5.Skewness and kurtosis of the SalePrice data
Skewness- Describes as a measure of a dataset's symmetry/assymetry.
A perfectly symmetrical data will have a skewness of 0

"""
print("Skewness: %f "% df_train['SalePrice'].skew())
print("Kurtosis: %f "% df_train['SalePrice'].kurt())

"""
6.Visualizing the other variables
[GrLivArea,YearBuilt,TotalBsmtSF,OverallQual]
i-> Relationship with numerical variables
ii->Relationship with categorical variables
Plot a scatterplot for the i case
"""
var='GrLivArea'
data=pd.concat([df_train['SalePrice'],df_train[var]],axis=1)
data.plot.scatter(x=var,y='SalePrice',ylim=(0,800000))

var1='YearBuilt'
data1=pd.concat([df_train['SalePrice'],df_train[var1]],axis=1)
f1,ax1=plt.subplots(figsize=(16,8))
fig1=sns.boxplot(x=var1,y='SalePrice',data=data1)
fig1.axis(ymin=0,ymax=800000)

var2='TotalBsmtSF'
data2=pd.concat([df_train['SalePrice'],df_train[var2]],axis=1)
data2.plot.scatter(x=var2,y='SalePrice',ylim=(0,800000))

var3='OverallQual'
data3=pd.concat([df_train['SalePrice'],df_train[var3]],axis=1)
#As this is a categorical variable we need to use boxplot
f,ax=plt.subplots(figsize=(8,6))
fig=sns.boxplot(x=var3,y='SalePrice',data=data3)
fig.axis(ymin=0,ymax=800000)

"""
7.We need to create a correlation plot to understand the corerelation of the variables with each other
The above four variables were just a hunch where we found out that GrLivArea with SalePrice is linearly related
i.Correlation Matrix
ii.Zoomed Correlation Matrix
iii.Scatter Plots between the most correlated variables
i.Correlation Matrix 
a.1 means positive correlation
b.-1 menas negative correlation
c.0 means no correlation
"""
#1.Correlation Matrix (heatmap style)
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True)

#2.Correlation Matrix(zoomed heatmap style)
k = 10 #number of variables for heatmap
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()

#3.ScatterPlots between Sales Price and correlated variables
sns.set()
cols=['SalePrice','OverallQual','GrLivArea','GarageCars','TotalBsmtSF','FullBath','YearBuilt']
sns.pairplot(df_train[cols],size=2.5)
plt.show()

"""
8.Dealing with the missing data
Print the null columns
"""
null_columns = dict(df_train.isnull().any()[lambda x:x])
print(null_columns)

total=df_train.isnull().sum().sort_values(ascending=False)
percent=(df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data=pd.concat([total,percent],axis=1,keys=['Total','Percent'])
missing_data.head(20)

"""
9.Drop the columns containing mising data
How do we decide which columns to drop?-more than 15 % then drop
"""

df_train=df_train.drop(missing_data[missing_data['Total']>1].index,1)
df_train=df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)
df_train.isnull().sum().max()

"""
10.Outlier Analysis
i.Univariate Analysis
ii.Bivariate Analysis
"""
#Standardizing the data
saleprice_scaled=StandardScaler().fit_transform(df_train['SalePrice'][:,np.newaxis])
low_range=saleprice_scaled[saleprice_scaled[:,0].argsort()][:10]
high_range=saleprice_scaled[saleprice_scaled[:,0].argsort()][:-10]
print("outer range (low) of the distribution:")
print(low_range)
print("\nouter range (high) of the distribution:")
print(high_range)
#Observation: 
#low range value are not to far from 0,high range values are from 0 and 7 , which are outliers

#Bivariate analysis saleprice/grlivarea 
var5='GrLivArea'
data5=pd.concat([df_train['SalePrice'],df_train[var5]],axis=1)
data5.plot.scatter(x=var,y='SalePrice',ylim=(0,800000))

"""
11.Deleting the outlier points
"""
df_train.sort_values(by='GrLivArea',ascending=False)[:2]
df_train=df_train.drop(df_train[df_train['Id']==1299].index)
df_train=df_train.drop(df_train[df_train['Id']==524].index)

#Bivariate analysis saleprice/taotalbsmtSF
var6='TotalBsmtSF'
data6=pd.concat([df_train['SalePrice'],df_train[var6]],axis=1)
data6.plot.scatter(x=var6,y='SalePrice',ylim=(0,800000))

"""
1.Normality:
    Means the data should look like a normal distribution. In this exercise we will just check for univariate normality for SalePrice.
2.Homoscedacity:
    Refers to the assumption that dependent variable(s) exhibit equal levels of variance accross the range of predictor variables
    This is necessary as we want the error term to be the same accross all values of independent variables
3.Linearity:
    Best way to examine linearity is to examine scatter plots and search for linear patterns
    If patterns are not linear, it would not be worthwhile to explre data transformations.
4.Absence of correlated errors:
    This happens whern one error is correlated to others.    
"""

#Normality- Histogram,Normal Probability plot
sns.distplot(df_train['SalePrice'],fit=norm)
fig=plt.figure()
res=stats.probplot(df_train['SalePrice'],plot=plt)

#applying log transformation
df_train['SalePrice']=np.log(df_train['SalePrice'])

#transformed histogram and normal probability plot
sns.distplot(df_train['SalePrice'],fit=norm)
fig=plt.figure()
res=stats.probplot(df_train['SalePrice'],plot=plt)

"""
We explored the data using the dataset geven and even pre processed the data , by removing the columns containg the null values
"""

"""
Regression Models
"""

"""
Import the required modules
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm,skew

"""
Loading the data
"""
path = "G:\\extra things\\Knowledge\\practice\\Edureka\\Kaggle\\HouseDataset\\"
train_data=pd.read_csv(path+"train.csv")
test_data=pd.read_csv(path+"train.csv")


"""
Exploring the data as per the above technique
"""

#1.Print the columns in the datasets
#Train Data, Test Data columns
print(list(train_data.columns))
print(list(test_data.columns))

#2.Print the data types of the columns
print(train_data.info())
print(test_data.info())

#3.Extracting the summary of the train_data,test_data
print(train_data.describe())
print(test_data.describe())

test_data.drop("SalePrice",axis=1,inplace=True)
"""
4.Plot a histogrm for Sale Price
seaborn using the distplot function
"""
sns.distplot(train_data['SalePrice'])

"""
To know the independent variables that we need to use get a good prediction
"""
#5.Create a correlation map to know th same against the SalePrice dependent variable
corrmat = train_data.corr()
f,ax=plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat,vmax=.8,square=True)


#6.Correlation Matrix(zoomed heatmap style)
k = 10 #number of variables for heatmap
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(train_data[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)
plt.show()

#7.Print the column containing the null values
null_columns = dict(train_data.isnull().any()[lambda x:x])
print(null_columns)

#8.We need to deal with the columns containg the null variables
#calculate the total values of the columns containing the null values
#calculate the percent of the null values in each columns
#Create a datafrm consiting of total and percent
total = train_data.isnull().sum().sort_values(ascending=False)
percent =((train_data.isnull().sum())/(train_data.isnull().count())*100).sort_values(ascending=False)
missing_data = pd.concat([total,percent],axis=1,keys=['Total','Percent'])
print(missing_data.head(20))


#9.Drop the columns containing mising data
#How do we decide which columns to drop?-more than 15 % then drop

#train_data=train_data.drop(missing_data[missing_data['Total']>1].index,1)
#train_data=train_data.drop(train_data.loc[train_data['Electrical'].isnull()].index)
#train_data.isnull().sum().max()

#10.Print the shape of both the train and test data
print ("The train data before dropping the Id Feature:{}".format(train_data.shape))
print ("The test data before dropping the Id feature:{}".format(test_data.shape))

train_Id= train_data['Id']
test_Id= test_data['Id']

#11.Drop the train and test data column Id

train_data.drop("Id",axis=1,inplace=True)
test_data.drop("Id",axis=1,inplace=True)

print ("The train data before dropping the Id Feature:{}".format(train_data.shape))
print ("The test data before dropping the Id feature:{}".format(test_data.shape))

#12.Plot the scatter plot for the column contained in the second scatter plot
sns.set()
cols=['SalePrice','OverallQual','GrLivArea','GarageCars','TotalBsmtSF','FullBath','YearBuilt']
sns.pairplot(train_data[cols],size=2.5)
plt.show()

#13.Plot the scatter plot fo looiking into outliers
cols=['SalePrice','OverallQual','GrLivArea','GarageCars','TotalBsmtSF','FullBath','YearBuilt']
for i in range(len(cols)):
    var=cols[i]
    data2=pd.concat([train_data['SalePrice'],train_data[var]],axis=1)
    data2.plot.scatter(x=var,y='SalePrice',ylim=(0,800000))
"""
GrLivArea - Outlier
TotalBsmtSF -Outlier
"""

#14.Deleting Outliers

train_data = train_data.drop(train_data[(train_data['GrLivArea']>4000) & (train_data['SalePrice']<300000)].index)
f,ax=plt.subplots()
ax.scatter(train_data['GrLivArea'],train_data['SalePrice'])
plt.ylabel('SalePrice',fontsize=13)
plt.xlabel('GrLivArea',fontsize=13)
plt.show()

#15.Create a distribution plot for the dependent variable 'SalePrice'
sns.distplot(train_data['SalePrice'],fit=norm)
(mu,sigma) = norm.fit(train_data['SalePrice'])
print('\n mu = {:.2f} and sigma ={:.2f}\n'.format(mu,sigma))
plt.legend(['Normal Distribution. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu,sigma)],loc='best')
plt.ylabel('Frequency')
plt.xlabel('SalePrice Distribution')

fig=plt.figure()
res=stats.probplot(train_data['SalePrice'],plot=plt)
plt.show()

#16.Log Transformation of the target variable
train_data['SalePrice'] = np.log1p(train_data['SalePrice'])
sns.distplot(train_data['SalePrice'],fit=norm)

(mu,sigma) = norm.fit(train_data['SalePrice'])
print('\n mu = {:.2f} and sigma ={:.2f}\n'.format(mu,sigma))
plt.legend(['Normal Distribution. ($\mu=$ {:.2f} and $\sigma=$ {:.2f} )'.format(mu,sigma)],loc='best')
plt.ylabel('Frequency')
plt.xlabel('SalePrice Distribution')

fig=plt.figure()
res=stats.probplot(train_data['SalePrice'],plot=plt)
plt.show()

#16.Feature Engineering
ntrain = train_data.shape[0]
ntest = test_data.shape[0]
y_train = train_data.SalePrice.values
all_data=pd.concat((train_data,test_data)).reset_index(drop=True)
all_data.drop(['SalePrice'],axis=1,inplace=True)
print("all data size is:{}".format(all_data.shape))


#19.Print the column containing the null values
null_columns = dict(all_data.isnull().any()[lambda x:x])
print(null_columns)


#20.We need to deal with the columns containg the null variables
#calculate the total values of the columns containing the null values
#calculate the percent of the null values in each columns
#Create a datafrm consiting of total and percent
total = all_data.isnull().sum().sort_values(ascending=False)
percent =((all_data.isnull().sum())/(all_data.isnull().count())*100).sort_values(ascending=False)
missing_data = pd.concat([total,percent],axis=1,keys=['Total','Percent'])
print(missing_data.head(20))

all_data_na = (all_data.isnull().sum()/len(all_data))*100
all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)[:30]
missing_data = pd.DataFrame({'Missing Ratio' :all_data_na})
missing_data.head(20)

f, ax = plt.subplots(figsize=(15, 12))
plt.xticks(rotation='90')
sns.barplot(x=all_data_na.index, y=all_data_na)
plt.xlabel('Features', fontsize=15)
plt.ylabel('Percent of missing values', fontsize=15)
plt.title('Percent missing data by feature', fontsize=15)

"""
Imputing Missing Value
"""

cols1=['PoolQC','MiscFeature','Alley','Fence','FireplaceQu']
for i in range(len(cols1)):
    all_data[cols1[i]]=all_data[cols1[i]].fillna("None")

all_data["LotFrontage"] = all_data.groupby("Neighborhood")["LotFrontage"].transform(
    lambda x: x.fillna(x.median()))

for col in ('GarageType', 'GarageFinish', 'GarageQual', 'GarageCond'):
    all_data[col] = all_data[col].fillna('None')

for col in ('GarageYrBlt', 'GarageArea', 'GarageCars'):
    all_data[col] = all_data[col].fillna(0)

for col in ('BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF','TotalBsmtSF', 'BsmtFullBath', 'BsmtHalfBath'):
    all_data[col] = all_data[col].fillna(0)

for col in ('BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2'):
    all_data[col] = all_data[col].fillna('None')

all_data["MasVnrType"] = all_data["MasVnrType"].fillna("None")
all_data["MasVnrArea"] = all_data["MasVnrArea"].fillna(0)

all_data['MSZoning'] = all_data['MSZoning'].fillna(all_data['MSZoning'].mode()[0])

all_data = all_data.drop(['Utilities'], axis=1)

all_data["Functional"] = all_data["Functional"].fillna("Typ")

all_data['Electrical'] = all_data['Electrical'].fillna(all_data['Electrical'].mode()[0])

all_data['KitchenQual'] = all_data['KitchenQual'].fillna(all_data['KitchenQual'].mode()[0])

all_data['Exterior1st'] = all_data['Exterior1st'].fillna(all_data['Exterior1st'].mode()[0])
all_data['Exterior2nd'] = all_data['Exterior2nd'].fillna(all_data['Exterior2nd'].mode()[0])

all_data['SaleType'] = all_data['SaleType'].fillna(all_data['SaleType'].mode()[0])
all_data['MSSubClass'] = all_data['MSSubClass'].fillna("None")


#Check remaining missing values if any 
all_data_na = (all_data.isnull().sum() / len(all_data)) * 100
all_data_na = all_data_na.drop(all_data_na[all_data_na == 0].index).sort_values(ascending=False)
missing_data = pd.DataFrame({'Missing Ratio' :all_data_na})
missing_data.head()
            

#20.Transforming some numerical variables that are categorical
#MSSubClass=The building class
all_data['MSSubClass'] = all_data['MSSubClass'].apply(str)


#Changing OverallCond into a categorical variable
all_data['OverallCond'] = all_data['OverallCond'].astype(str)


#Year and month sold are transformed into categorical features.
all_data['YrSold'] = all_data['YrSold'].astype(str)
all_data['MoSold'] = all_data['MoSold'].astype(str)


print(all_data.info())

from sklearn.preprocessing import LabelEncoder
cols = ('FireplaceQu', 'BsmtQual', 'BsmtCond', 'GarageQual', 'GarageCond', 
        'ExterQual', 'ExterCond','HeatingQC', 'PoolQC', 'KitchenQual', 'BsmtFinType1', 
        'BsmtFinType2', 'Functional', 'Fence', 'BsmtExposure', 'GarageFinish', 'LandSlope',
        'LotShape', 'PavedDrive', 'Street', 'Alley', 'CentralAir', 'MSSubClass', 'OverallCond', 
        'YrSold', 'MoSold')

# process columns, apply LabelEncoder to categorical features
for c in cols:
    lbl = LabelEncoder() 
    lbl.fit(list(all_data[c].values)) 
    all_data[c] = lbl.transform(list(all_data[c].values))
print('Shape all_data: {}'.format(all_data.shape))


# Adding total sqfootage feature 
all_data['TotalSF'] = all_data['TotalBsmtSF'] + all_data['1stFlrSF'] + all_data['2ndFlrSF']

#Skewed Features

numeric_feats = all_data.dtypes[all_data.dtypes != "object"].index

# Check the skew of all numerical features
skewed_feats = all_data[numeric_feats].apply(lambda x: skew(x.dropna())).sort_values(ascending=False)
print("\nSkew in numerical features: \n")
skewness = pd.DataFrame({'Skew' :skewed_feats})
skewness.head(10)


skewness = skewness[abs(skewness) > 0.75]
print("There are {} skewed numerical features to Box Cox transform".format(skewness.shape[0]))

from scipy.special import boxcox1p
skewed_features = skewness.index
lam = 0.15
for feat in skewed_features:
    #all_data[feat] += 1
    all_data[feat] = boxcox1p(all_data[feat], lam)

#Getting dummy categorical variables
all_data = pd.get_dummies(all_data)
print(all_data.shape)

train = all_data[:ntrain]
test = all_data[ntrain:]

#Modelling 