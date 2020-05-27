from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def sensitivity(dataset,features,points,cols,model,target):
    print(dataset.columns)
    print(features)
    sc=StandardScaler()
    X=dataset[cols]
    X=sc.fit_transform(X)
    norm_dataset=pd.DataFrame(X,columns=cols)

    plot_values=list()
    list1=list()
    list2=list()
    sensitivity=list()
    S=list()
    Z=list()
    
    for i in range(len(features)):
        max_value=dataset[features[i]].max()
        min_value=dataset[features[i]].min()
        a=np.linspace(min_value,max_value,points)
        plot_values.append(a)
    
    plot_values=np.array(plot_values)
    plot_values=np.transpose(plot_values)
    
    for i in range(len(cols)):
        max_value=norm_dataset[cols[i]].max()
        min_value=norm_dataset[cols[i]].min()
        a=np.linspace(min_value,max_value,points)
        list1.append(a)

    list1=np.array(list1)
    Range=np.transpose(list1)

    for j in range(len(cols)):
         mean_value=norm_dataset[cols[j]].mean()
         b=np.linspace(mean_value,mean_value,points)
         list2.append(b)

    list2=np.array(list2)
    Mean=np.transpose(list2) 
    
    for i in range(len(features)):
        Array=Mean.copy()
        Array[:,i]=Range[:,i]
        y_pred=model.predict(Array)
        S.append(y_pred[:,0])
    
    for i in range(len(features)):
            Y=S[:][i]
            X=plot_values[:,i]
            Z=pd.DataFrame(list(zip(X, Y)),columns=[features[i],target])
            sensitivity.append(Z)
    return sensitivity

def plot_curves(features,target,sensitivity):
    fig, axs = plt.subplots(len(sensitivity),figsize=(15,15))
    for i in range(len(sensitivity)):
        fig.suptitle('Sensitivity Analysis')
        axs[i].plot(sensitivity[i][features[i]],sensitivity[i][target])
        axs[i].set_xlabel(features[i])
        axs[i].set_ylabel(target)
        #plt.ylabel(target)