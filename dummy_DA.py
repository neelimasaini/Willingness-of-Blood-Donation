import warnings;
warnings.filterwarnings('ignore');
from visualize import visualizer


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import matplotlib as mpl


df=pd.read_csv("transfusion.data")



df.info()


df.describe()


df=df.rename(columns = {'Recency (months)':'Recency','Frequency (times)':'Frequency','Monetary (c.c. blood)':'CCBlood','Time (months)':'Time','whether he/she donated blood in March 2007':'Target'})




plt.figure(figsize=(10,7))
sn.heatmap(df.corr(),annot=True,cmap = 'Blues',vmin=-1,vmax=1,center=0,linewidths=2, linecolor='black')
plt.xticks(fontsize=15,rotation=90)
plt.yticks(fontsize=15,rotation=0)
plt.title('Correlation HeatMap')


#plt.show()
# Instead of plt.show(), do the following: 



viz = visualizer()
viz.jumbocard('Jumbocard Heading', plt,'My Description: This is An Important Graph')






df.groupby(['Target']).mean()



df.groupby(['Target']).median()



df.groupby(['Target']).std()



plt.figure(figsize=(10,5))
plt.title('Frequency vs Cubic Centimeters of Blood',fontsize=20)
plt.scatter(np.log(df.Frequency),np.log(df['CCBlood']),alpha=0.5,c='gold')
plt.xlabel("Log of Frequency",fontsize=15)
plt.ylabel("Log of Cubic Centimeters of Blood",fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
#fig1 = plt.gcf()
#plt.show()
#plt.draw()
#fig1.savefig('2.png', dpi=100)

viz.jumbocard('Jumbocard Heading', plt,'My Description: This is An Important Graph')



df=df.drop('CCBlood',axis=1)


d={'0':0,'1':1}
def diction(x):
    if x==0:
        d['0']+=1
    else:
        d['1']+=1
    return


df['Target'].apply(diction)



fig,ax=plt.subplots(figsize=(20,10))
plt.rcParams['font.size'] = 14.0
ax.pie(list(d.values()),labels=["Didn't Donate","Donate"],startangle=90,autopct='%1.1f%%',explode=(0,0.1),shadow=True,colors=('Lightslategray','Gold'))
plt.title('Percentage of People who Actually Donate after Pledging')


#plt.show()


viz.jumbocard('Jumbocard Heading', plt,'My Description: This is An Important Graph')



plt.figure(figsize=(15,8))
plt.title('Distribution of Recency of donation for 748 candidates',fontsize=20)
plt.hist(df['Recency'],color='Gold',edgecolor='black')
plt.xlabel('Time since Last Donation',fontsize=18)
plt.ylabel('Number of Candidates',fontsize=18)
#plt.xticks(range(min(df['Recency']), max(df['Recency'])+1))
#plt.xticks([0,4,14,21,28,35,42,49,56,63,70,77])
#plt.xticks(range(0,78,7))
fig1 = plt.gcf()
#plt.show()
#plt.draw()
#fig1.savefig('4.png', dpi=100)

viz.jumbocard('Jumbocard Heading', plt,'My Description: This is An Important Graph')




plt.figure(figsize=(12,6))
plt.title('Distribution of Frequency of donation for 748 candidates',fontsize=18)
plt.hist(df.Frequency,color='gold',edgecolor='black')
plt.xlabel('Frequency of Donations till Date',fontsize=18)
plt.ylabel('Number of Candidates',fontsize=18)
fig1 = plt.gcf()
#plt.show()
#plt.draw()
#fig1.savefig('5.png', dpi=100)

viz.jumbocard('5th Image Heading', plt,'My Description: This is An Important Graph')




plt.figure(figsize=(12,6))
plt.title('Distribution of Time since first donation  for 748 candidates',fontsize=18)
plt.hist(df.Time,color='gold',edgecolor='black')
plt.xlabel('Time since a person has been Donating (months)',fontsize=18)
plt.ylabel('Number of Candidates',fontsize=18)
fig1 = plt.gcf()
#plt.show()
#plt.draw()
#fig1.savefig('6.png', dpi=100)

viz.jumbocard('Jumbocard Heading', plt,'My Description: This is An Important Graph')


# Creating a new Column - Frequency of Donations per Annum
df['freqPerAnnum']=df['Frequency'][df['Time']>=12]/df['Time'][df['Time']>=12]
df['freqPerAnnum']



plt.figure(figsize=(12,6))
plt.title('Distribution of Frequency Donations per Annum for 748 candidates',fontsize=18)
plt.hist(df.freqPerAnnum,color='gold',edgecolor='black')
plt.xlabel('Frequency of Donations per Annum',fontsize=18)
plt.ylabel('Number of Candidates',fontsize=18)
fig1 = plt.gcf()
#plt.show()
#plt.draw()
#fig1.savefig('7.png', dpi=100)

viz.jumbocard('Jumbocard Heading', plt,'My Description: This is An Important Graph')



df.info()


plt.figure(figsize=(10,7))
sn.heatmap(df.corr(),annot=True,cmap = 'Blues',vmin=-1,vmax=1,center=0,linewidths=2, linecolor='black')
plt.xticks(fontsize=15,rotation=90)
plt.yticks(fontsize=15,rotation=0)
plt.title('Correlation HeatMap after addition of FreqPerAnnum Attribute')
fig1 = plt.gcf()
#plt.show()
#plt.draw()
#fig1.savefig('8.png', dpi=100)

viz.jumbocard('8th Image Heading', plt,'My Description: This is An Important Graph')



df2=df[df.freqPerAnnum.isnull()==True]
df2=df2.reset_index()
df2=df2.drop('index',axis=1)
df2=df2.drop('freqPerAnnum',axis=1)
df2


x_train,x_test,y_train,y_test = train_test_split(df2[['Recency','Frequency','Time']],df2['Target'],random_state=30,test_size=0.3)




classify=GridSearchCV(LogisticRegression(),{'C':[0.1]})
print(classify.get_params)
classify=classify.fit(x_train,y_train)
print('Logistic Regression Train Score: ',classify.score(x_train, y_train))
print('Logistic Regression Test Score: ',classify.score(x_test, y_test))
print(classification_report(y_test,classify.predict(x_test)))






classify3=GridSearchCV(LinearSVC(C=0.8,dual=False),{'C':[0.001]})
classify3=classify3.fit(x_train,y_train)
print('Train Score: ',classify3.score(x_train, y_train))
print('Test Score: ',classify3.score(x_test, y_test))
print(classification_report(y_test,classify3.predict(x_test)))
viz.rendertable('Table Title: GridSearchCV',classification_report(y_test,classify3.predict(x_test)))

classify4=KNeighborsClassifier(n_neighbors=3)
classify4.fit(x_train, y_train)
print('Train Score: ',classify4.score(x_train, y_train))
print('Test Score: ',classify4.score(x_test, y_test))
print(classification_report(y_test,classify4.predict(x_test)))
viz.rendertable('KNeighborsClassifier', classification_report(y_test,classify4.predict(x_test)))


classify5=RandomForestClassifier(n_estimators=300,max_depth=2.9)
print(classify5.get_params)
classify5=classify5.fit(x_train,y_train)
print('Train Score: ',classify5.score(x_train, y_train))
print('Test Score: ',classify5.score(x_test, y_test))
print(classification_report(y_test,classify5.predict(x_test)))
viz.rendertable('RandomForestClassifier',classification_report(y_test,classify5.predict(x_test)))

classify6=AdaBoostClassifier(n_estimators=300,learning_rate=0.02)
print(classify6.get_params)
classify6=classify6.fit(x_train,y_train)
print('Train Score: ',classify6.score(x_train, y_train))
print('Test Score: ',classify6.score(x_test, y_test))
print(classification_report(y_test,classify6.predict(x_test)))
viz.rendertable('AdaBoostClassifier',classification_report(y_test,classify6.predict(x_test)))



classify2=SGDClassifier(alpha=10)
print(classify2.get_params)
classify2=classify2.fit(x_train,y_train)
print('Train Score: ',classify2.score(x_train, y_train))
print('Test Score: ',classify2.score(x_test, y_test))
print(classification_report(y_test,classify2.predict(x_test)))
viz.rendertable('SGDClassifier',classification_report(y_test,classify2.predict(x_test)))
viz.card('SGD Scores: ','Train Score: '+str(classify2.score(x_train, y_train))[:3]+'  Test Score: '+str(classify2.score(x_test, y_test)),'SGD Provides Best Results')
viz.generate_output()









