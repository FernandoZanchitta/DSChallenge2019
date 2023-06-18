"""
função do arquivo src/functions/actual_vs_pred_plot.py
"""
import matplotlib.pyplot as plt
def actual_vs_pred_plot(y_train,y_pred,model_name):
    """
    
    """
    fig = plt.figure(figsize=(12,12))
    fig, ax = plt.subplots()
    
    ax.scatter(y_train, y_pred,color = "teal",edgecolor = 'lightblue')
    ax.plot([y_train.min(),y_train.max()], [y_train.min(), y_train.max()], 'k--',lw=0.2)
    ax.set_xlabel('Atual')
    ax.set_ylabel('Predito')
    plt.suptitle(model_name + ' - Actual vs Predicted Values',size=14)
    plt.show()