# Used to plot
import matplotlib.pyplot as plt
#matplotlib inline
import numpy as np
# Pandas is used to deal with csv file
import pandas as pd
# import statsmodels.api as sm
# from statsmodels.nonparametric.kde import KDEUnivariate
# from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame
from patsy import dmatrices,dmatrix
from sklearn import datasets, svm,cross_validation
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
# from KaggleAux import predict as ka # see github.com/agconti/kaggleaux for more details

# --------------------------------------------Loading Files----------------------------------------------
# Data loaded in a dictionary
df = pd.read_csv("train.csv") 
# Ticket and cabin are not very important so we will drop them
df = df.drop(['Ticket','Cabin'], axis=1)
# Remove NaN values
df = df.dropna()
# print df
# --------------------------------------------Visualizing the Data----------------------------------------  
# # plot a bar graph of those who Survived Vs Those who did not
# df.Survived.value_counts().plot(kind='barh', color="blue", alpha=.65)
# plt.title("Survival Breakdown (1 = Survived, 0 = Died)")
# plt.show()
# ----------------------------------------------------------------------------------------------------
# #create a plot of two subsets, male and female, of the survived variable.
# #After we do that we call value_counts() so it can be easily plotted as a bar graph. 
# #'barh' is just a horizontal bar graph
# df_male = df.Survived[df.Sex == 'male'].value_counts().sort_index()
# df_female = df.Survived[df.Sex == 'female'].value_counts().sort_index()
# df_male.plot(kind='barh',label='Male', alpha=0.65,color="blue")
# df_female.plot(kind='barh', color='#FA2379',label='Female', alpha=0.65)
# plt.title("Who Survived? with respect to Gender, (raw value counts) ");
# plt.legend(loc='best')

# plt.show()

# #adjust graph to display the proportions of survival by gender
# (df_male/float(df_male.sum())).plot(kind='barh',label='Male', alpha=0.55)  
# (df_female/float(df_female.sum())).plot(kind='barh', color='#FA2379',label='Female', alpha=0.55)
# plt.title("Who Survived proportionally? with respect to Gender"); plt.legend(loc='best')

# plt.show()
# ------------------------------------------------------------------------------------------------------

# plt.figure(figsize=(18,4))
# alpha_level = 0.65

# # building on the previous code, here we create an additional subset with in the gender subset 
# # we created for the survived variable. I know, thats a lot of subsets. After we do that we call 
# # value_counts() so it it can be easily plotted as a bar graph. this is repeated for each gender 
# # class pair.
# # ------------Female HighClass----------------
# plt.subplot(141)
# female_highclass = df.Survived[df.Sex == 'female'][df.Pclass != 3].value_counts()
# female_highclass.plot(kind='bar', label='female, highclass', color='#FA2479', alpha=0.65)
# plt.xticks([.5,1.5], ["Survived","Died"],rotation=0)
# plt.legend(loc='best')

# #------------Female LowClass------------------
# plt.subplot(142)
# female_lowclass = df.Survived[df.Sex == 'female'][df.Pclass == 3].value_counts()
# female_lowclass.plot(kind='bar', label='female, low class', color='pink', alpha=alpha_level)
# plt.xticks([.5,1.5], ["Died","Survived"],rotation=0)
# plt.legend(loc='best')

# # -------------Male HighClass-----------------
# plt.subplot(143)
# male_highclass = df.Survived[df.Sex == 'male'][df.Pclass != 3].value_counts()
# male_highclass.plot(kind='bar',label='male, highclass',color='lightblue', alpha=alpha_level)
# plt.xticks([.5,1.5], ["Died","Survived"],rotation=0)
# plt.legend(loc='best')

# # --------------Male LowClass-----------------
# plt.subplot(144)
# male_lowclass = df.Survived[df.Sex == 'male'][df.Pclass == 3].value_counts()
# male_lowclass.plot(kind='bar', label='male, low class',color='lightblue', alpha=alpha_level)
# plt.xticks([.5,1.5], ["Died","Survived"],rotation=0)
# plt.legend(loc='best')
# plt.show()
# create a regression friendly dataframe using patsy's dmatrices function
# y,x = dmatrices(formula, data=df, return_type='dataframe')
# print y
# print x
# ---------------------------------------Applying Logistic Regression---------------------------------------

# # import the machine learning library that holds the randomforest
# import sklearn.ensemble as ske
# Create an acceptable formula for our machine learning algorithms
formula_ml = 'Survived ~ C(Pclass) + C(Sex)'

# # Create the random forest model and fit the model to our training data
y, x = dmatrices(formula_ml, data=df, return_type='dataframe')
# # RandomForestClassifier expects a 1 demensional NumPy array, so we convert
y = np.asarray(y).ravel()
# #instantiate and fit our model
# results_rf = ske.RandomForestClassifier(n_estimators=100).fit(x, y)

# # Score the results
# score = results_rf.score(x, y)
# print "Mean accuracy of Random Forest Predictions on the data was: {0}".format(score)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=30)
clf.fit(x, y) 
print "Sucess"

test = pd.read_csv("test.csv") 
test = test.drop(['Ticket','Cabin'], axis=1)
# test = test.dropna()
formula_ml = 'C(Pclass) + C(Sex)'
# print test
x = dmatrix(formula_ml, data=test, return_type='dataframe')
# print x
pre=clf.predict(x)
pre = DataFrame(pre,columns=['Survived'])
pre.to_csv("output.csv")
# from sklearn.metrics import accuracy_score
# print accuracy_score(y,pre)
# print pre
# print pre[0]
# print pre
# print len(pre)
# from sklearn.metrics import accuracy_score
# print(accuracy_score(y, pre))