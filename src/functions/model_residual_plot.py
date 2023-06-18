import matplotlib.pyplot as plt

def model_residual_plot(test_Y,model_predicted,model_name):
    
    residuals = test_Y - model_predicted
    plt.scatter(model_predicted, residuals)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title(model_name + ' - Residual Plot')
    plt.show()