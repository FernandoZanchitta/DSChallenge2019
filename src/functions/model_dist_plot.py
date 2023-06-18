import seaborn as sns
import matplotlib.pyplot as plt
def model_dist_plot(y_test,y_pred,model_name):
    plt.figure(figsize=(10,5))
    sns.histplot(y_test, kde=False)
    sns.histplot(y_pred, kde=False)
    plt.title(model_name + ' - Distribution Plot')
    plt.legend(labels=['Actual Values of Price', 'Predicted Values of Price'])
    plt.xlim(0,)
