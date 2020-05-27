# Sensitivity Analysis for Neural Networks
## Description
This Python code performs sensitivity analysis for neural networks in order to analyse how the value of target variable varies when the value of only one input feature is varied at a time, keeping all other input features constant. This is also known as parametric analysis. For this, a synthetic dataset of user-specified length (number of observations) is generated for each input feature Fi, in which the value of Fi is incrementally increased from its minimum value (in the original dataset) to the corresponding maximum value. All the other input features are kept fixed at their constant value. This new dataset is provided to the trained model (preferably model should first be checkpointed) to obtain the sensitivity analysis results. 

## How to use the function?

All you have to do is to call the sensitivity() function in your Python code with the following arguments:

  Results = sensitivity(dataset=dataset,features=features,cols=columns,points=100,model=model,target="Phase Angle")

Each of the function arguments is described below:

- dataset: a Pandas dataframe

     This is the original dataset used for your neural network model. 

- features: a Python list 

     This contains the of names of input features as mentioned in the dataset columns for which sensitivity analysis of the target variable is to be performed.

- points: an integer

     This argument specifies the number of obervations to be generated in the synthetic dataset.

- cols: a Python list

     This contains the names of all the input features for the developed neural network model. 

- model: a Keras object

     This is the object for the developed Keras model. 

- target: a Python string

     This specifies the name of target variable as a string  

## What would the function return?

The functions returns a list of n dataframes, where n is the number of input features for which sensitivity analysis is carried out. Each dataframe has two columns: column1 has the values of input feature Fi whereas column 2 has the corresponding value of target variable. 

## Plotting function 

plot_curves(features,target,Results)

- Results: list of n dataframes 

     n is the number of input features for which sensitivity analysis is carried out. Each dataframe has two columns: column1 has the values of input feature Fi whereas column 2 has the corresponding value of target variable. 


  

 
