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
This notebook contains the linear regression model for this project. The goal of the model is to predict the number of veteran suicides in 2025 and beyond. The file run through this model is 

### Another model




Conclusion:.....
