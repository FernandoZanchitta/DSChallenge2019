import numpy as np
from sklearn import metrics
# function to calculate Root mean square error (RMSE)
def rmse(y_pred, y_test): 
    
    rmse_ = np.sqrt(metrics.mean_squared_error(y_pred,y_test))
    print("rmse: ", rmse_)