import pandas as pd
import sklearn
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

filepath="C:/Users/user/OneDrive/Desktop/Data Science Syllabus and notes/Dataset/diabetes_prediction_dataset (1).csv"
diabetes=pd.read_csv(filepath)
#Pre-processing
diabetes.drop_duplicates(inplace=True)
encoded=OrdinalEncoder()
diabetes['gender']=encoded.fit_transform(diabetes[['gender']])
diabetes['smoking_history']=encoded.fit_transform(diabetes[['smoking_history']])
#choosing independant and dependant
x=diabetes.drop('diabetes',axis=1)
y=diabetes.iloc[:,-1]
#spliting for train and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
#model selection
#dependant is category hence choosing classifier alogrithm
model=DecisionTreeClassifier().fit(x_train,y_train)
#evaluation
y_predict=model.predict(x_test)
pickle.dump(model,open('diabetes_result','wb'))
