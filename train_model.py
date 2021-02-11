

import pandas
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor
from joblib import dump
import json
from sklearn.preprocessing import StandardScaler




def normalize(in_df, feature_cols, target_col):
    X = in_df.loc[ :, feature_cols].values
    Y = in_df.loc[:, target_col].values
    scaler = StandardScaler()
    scaler.fit(X)
    X_norm= scaler.transform(X)
    out_df = pandas.DataFrame(X_norm,index = in_df.index, columns=features)
    out_df[target_col]= Y
    return out_df, scaler






with open("conf.json") as conffile:
    allconf = json.load(conffile)

### for resolution: SGDRegressor_epsilon_insensitive_elasticnet_0.001_0.7_highdim_smote1

var = "resolution"
model = SGDRegressor(loss="epsilon_insensitive",penalty="elasticnet",alpha=0.001,l1_ratio=0.7)
conf = allconf[var]
training_set_path = conf ["data_file"]
features = conf["features"]
target_col = conf["target_var_col"]
### read the right dataset
train_df = pandas.read_csv(training_set_path)
#create the scaler and scale the features
norm_train_df,scaler = normalize(train_df,features,target_col)
#save the scaler
dump(scaler, var+".scaler")
#train the right model on the scaled dataset
train_X = norm_train_df.loc[:, features].values
train_Y = norm_train_df.loc[:, target_col].values
model.fit(train_X, train_Y)
dump(model, var+".model")
#save the model


###for rfree ElasticNet_0.001_0.05_lowdim_smote2


var = "rfree"
model = (alpha=0.001,l1_ratio=0.05)
conf = allconf[var]
training_set_path = conf["data_file"]
features = conf["features"]
target_col = conf["target_var_col"]
### read the right dataset
train_df = pandas.read_csv(training_set_path)
#create the scaler and scale the features
norm_train_df,scaler = normalize(train_df,features,target_col)
#save the scaler
dump(scaler, var+"_new.scaler")
#train the right model on the scaled dataset
train_X = norm_train_df.loc[:, features].values
train_Y = norm_train_df.loc[:, target_col].values
model.fit(train_X, train_Y)
dump(model, var+"_new.model")
#save the model
