# Capstone-Project-MCDANIEL
## Title: Suicide Among U.S. Veterans

#### Overview
This project is showing the number of suicides among US Veterans in past years and using that data to predict the number of suicides in the future. There are many factors that could cause someone to commit suicide however, this project will focus on numbers alone. We can see the number of veterans at risk for suicide in future years and take steps to prevent them.

#### Programs Used
Overleaf, LaTex, GitHub, Python, Excel have been used to create this project.
Link to Overleaf Project Report: https://www.overleaf.com/read/rbzmtgzqwszy#74645a

#### Data
Data was extracted from kaggle.com and from statista. 
https://www.kaggle.com/datasets/residentmario/us-veteran-suicides/data
https://www.statista.com/statistics/754401/suicide-rates-among-vha-patients/

Data has been cleaned in the following ways:
    -All of the data files were cleaned in Excel. The original data files were fairly clean to begin with. The only changes made were formatting values to two decimal places and deleting unnecessary columns in Excel. The files were all saved in the CSV format so it was easiest to open them in Excel and format them that way instead of using Pyton code.
    -All the data files that begin with c, are the cleaned data files. The original data files are still included in this project. 
    -Another folder of cleaned data was created to isolate the number of veteran suicides in each state per year. This folder is called "final cleaned data". 

#### Setting up the Virtual Environment
A virtual environment needs to be created and activated.
Open a new terminal
type: python -m venv .venv
then activate the new environment
.venv\Scripts\activate

*Note: There could be a pop-up if using vs code, wanting to confirm activating a virtual environment. If so, select yes. 

#### Install packages

Install everything in requirements.txt. 

pip install -r requirements.txt

### EDAnotebook.ipynb
This jupyter notebook is running the Exploratory Data Analysis. There is a summary statistics report and scatter plots showing correlations between the different variables. There are also two bar charts showing relationships in the data as well. Two more files are also created called averages.csv and rates.csv to be used in the model building process. So far we can see an increase in the number of veteran suicides over the time frame in the data. The following models will help to prove this to be correct or incorrect.

### LinearRegressionModel.ipynb
This notebook contains the linear regression model for this project. The goal of the model is to predict the number of veteran suicides in 2025 and beyond. The model is run  on averages.csv and rates.csv. The independent variable for both datasets is "year" and the dependent variable for averages is the average number of veteran suicides. The dependent variable for rates.csv is the average rate of veteran suicide. The train/test split is 80:20. Through scatterplots and a line graph, it's clear that the rate and average number of veteran suicides will continue to increase into the future without any intervention. This model fit well enough for such a small dataset. The RMSE was 2.31 for the first dataset and 0.45 for the second set. 

### MultipleLinearRegression.ipynb
This notebook employs a multiple linear regression model. The dataset c2005.csv was run in this model because there were more variable options. Multiple Linear regression allows for  multilple independent variables. The train/test split in this model was 70:30. The first set of independent variables were vet_pop, and vet_suicides. The dependent variable was vet_rate. Running the model with those variables resulted in a R^2 value of 0.612. The condition number was large which shows multicolinearity. This means that the independent variables were not independent of each other which skews the results. The model was run again with independent variables vet_pop, and civ_rate, and dependent variable vet_rate. The results were a little better here with an R^2 value of 0.416. The condition number was still large so there is some multicolinearity with this as well. 

### Conclusion
In conclusion, the linear regression model provided the best results. The number of veteran suicides will continue to gradually increase into the future without intervention. The hope is that intervention takes place and that this report is proven wrong. If you or anyone you know is struggling with suicidal thoughts call 988. For emergency situations call 911. 

![image](https://github.com/LuciMcD/Capstone-Project-MCDANIEL/assets/136775855/265bbe9b-d981-475c-b7eb-b4f2ed99e42c)
![image](https://github.com/LuciMcD/Capstone-Project-MCDANIEL/assets/136775855/de8a2c55-1d74-45e8-a484-a10790c82db7)
![image](https://github.com/LuciMcD/Capstone-Project-MCDANIEL/assets/136775855/f79eaa5f-d143-4f17-81e3-8cc26d0f846d)
![image](https://github.com/LuciMcD/Capstone-Project-MCDANIEL/assets/136775855/73eb1135-8085-4e43-8fb3-edae29eb505c)






