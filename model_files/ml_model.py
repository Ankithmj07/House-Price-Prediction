import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import pickle
from flask import json,jsonify

from pathlib import Path
import pandas as pd
import tarfile
import urllib.request


from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,FunctionTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector,make_column_transformer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import rbf_kernel


data=pd.read_csv("datasets\housing\housing.csv")
#print(housing)

housing=data.drop("median_house_value",axis=1)

housing_train=housing[:-15]
housing_test=housing[-15:]
#print(housing_test)

some_data=housing_test[:3]

class ClusterSimilarity(BaseEstimator,TransformerMixin):
  def __init__(self,n_clusters=10,gamma=0.1,random_state=None):
    self.n_clusters=n_clusters
    self.gamma=gamma
    self.random_state=random_state

  def fit(self,X,y=None,sample_weight=None):
    self.kmeans_=KMeans(self.n_clusters,random_state=self.random_state)
    self.kmeans_.fit(X,sample_weight=sample_weight)
    return self

  def transform(self,X):
    return rbf_kernel(X,self.kmeans_.cluster_centers_,gamma=self.gamma)

  def get_feature_names_out(self,names=None):
    return [f"Cluster {i} similarity" for i in range(self.n_clusters)]




num_attribs=["longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income"]

cat_attribs=["ocean_proximity"]

num_pipeline=make_pipeline(SimpleImputer(strategy="median"),StandardScaler())

cat_pipeline=make_pipeline(SimpleImputer(strategy="most_frequent")
                          ,OneHotEncoder(handle_unknown="ignore"))

preprocessing=ColumnTransformer([("num",num_pipeline,num_attribs),
                                 ("cat",cat_pipeline,cat_attribs),])


def column_ratio(X):
    return X[:, [0]] / X[:, [1]]

def ratio_name(function_transformer, feature_names_in):
    return ["ratio"]  # feature names out

def ratio_pipeline():
    return make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(column_ratio, feature_names_out=ratio_name),
        StandardScaler())

def pipeline_transformer():

    log_pipeline = make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(np.log, feature_names_out="one-to-one"),
        StandardScaler())
    cluster_simil = ClusterSimilarity(n_clusters=10, gamma=1., random_state=42)
    default_num_pipeline = make_pipeline(SimpleImputer(strategy="median"),
                                         StandardScaler())
    preprocessing_pipeline = ColumnTransformer([
            ("bedrooms", ratio_pipeline(), ["total_bedrooms", "total_rooms"]),
            ("rooms_per_house", ratio_pipeline(), ["total_rooms", "households"]),
            ("people_per_house", ratio_pipeline(), ["population", "households"]),
            ("log", log_pipeline, ["total_bedrooms", "total_rooms", "population",
                                   "households", "median_income"]),
            ("geo", cluster_simil, ["latitude", "longitude"]),
            ("cat", cat_pipeline, make_column_selector(dtype_include=object)),
        ],
        remainder=default_num_pipeline) 
    preprocessing_pipeline.fit_transform(housing_train)

def predict_data(data):
  with open("model_files\housing.pkl", "rb") as file:
   loaded_model = pickle.load(file)
  data_df=pd.DataFrame(data,index=[0])
  y_pred=loaded_model.predict(data_df)
  pred_dict={"y_pred":int(y_pred)}
  return jsonify(pred_dict)

mj={
  "longitude":-117.52,
  "latitude":36.9,
  "housing_median_age":48,
  "total_rooms":3120,
  "total_bedrooms":420,
  "population":1100,
  "households":432,
  "median_income":8.337,
  "ocean_proximity":"NEAR OCEAN"
}


#print(predict_data(mj))
    
    
class Predict:
   
   def makeDict(self,longitude,latitude,medianAge,totalRooms,totalBedrooms,population,households,income,oceanProximity):
      oceanStr=str(oceanProximity)
      dictData={
        "longitude":longitude,
        "latitude":latitude,
        "housing_median_age":medianAge,
        "total_rooms":totalRooms,
        "total_bedrooms":totalBedrooms,
        "population":population,
        "households":households,
        "median_income":income,
        "ocean_proximity":oceanStr
      }
      jsonData=json.dumps(dictData, sort_keys=False)
      return dictData
   

objPredict = Predict()


   






