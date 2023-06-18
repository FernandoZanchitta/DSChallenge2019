import numpy as np
from sklearn import metrics
# function to calculate Root mean square error (RMSE)
def regression_metrics(y_pred, y_test,model_name): 
    
    rmse_ = np.sqrt(metrics.mean_squared_error(y_pred,y_test))
    r2 = metrics.r2_score(y_test, y_pred)
    print(model_name," RMSE: ", rmse_)
    print(model_name,"R2: " + str(r2))
    return rmse_,r2