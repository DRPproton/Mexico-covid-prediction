# COVID-19 Prediction in Mexico

We will try to predict the probability of patient to die base in the comorbidities they have. 
This repository contains a Jupyter Notebook, `covid_prediction.ipynb`, which provides a predictive analysis of COVID-19 cases in Mexico. 
The notebook aims to help you understand and predict COVID-19 trends in Mexico using data analysis and machine learning techniques.

## Variables

1. **Sex (sexo)**: This variable represents the gender of the individual, typically categorized as male or female. It is important to consider gender as it can influence the risk and severity of COVID-19.

2. **Pneumonia (neumonia)**: This binary variable indicates whether an individual has been diagnosed with pneumonia, a common respiratory condition that can complicate COVID-19 cases.

3. **Age (edad)**: Age is a continuous variable that represents the age of the individual. Advanced age is a known risk factor for severe outcomes from COVID-19.

4. **Diabetes (diabetes)**: This binary variable denotes whether an individual has diabetes, a chronic condition that can exacerbate COVID-19 symptoms and outcomes.

5. **COPD (epoc)**: Chronic Obstructive Pulmonary Disease (COPD) is a respiratory condition, and this binary variable indicates whether an individual has it.

6. **Immunosuppression (inmusupr)**: This binary variable signifies whether the individual has a compromised immune system, which can affect their ability to fight off infections like COVID-19.

7. **Hypertension (hipertension)**: Hypertension, or high blood pressure, is a common comorbidity associated with COVID-19. This variable indicates whether the individual has this condition.

8. **Cardiovascular (cardiovascular)**: This binary variable is used to indicate whether an individual has a pre-existing cardiovascular condition, such as heart disease.

9. **Obesity (obesidad)**: Obesity is a known risk factor for severe COVID-19 outcomes. This variable represents whether the individual is obese.

10. **Chronic Kidney Disease (renal_cronica)**: This binary variable denotes whether an individual has chronic kidney disease, which can impact the body's ability to cope with infections.

11. **Outcome (decease)**: This binary variable indicates whether the individual has survived (0) or succumbed (1) to COVID-19. It is the target variable used in your prediction model.

These variables are crucial for understanding the impact of comorbidities on COVID-19 outcomes and for building predictive models to assess the risk of severe illness or mortality based on these factors.

## Introduction

The ongoing COVID-19 pandemic has had a significant impact on countries worldwide. 
This project focuses on Mexico and aims to predict the progression of COVID-19 cases in the country using data analysis and machine learning. 
The Jupyter Notebook, `covid_prediction.ipynb`, walks you through the process of loading, and analyzing COVID-19 data in Mexico. 
It also includes predictive modeling to forecast future trends.

## Data

The analysis in this notebook relies on COVID-19 data for Mexico. 
The data used is publicly available and can be obtained from a public datasets.
You can access the complete dataset in this Kaggle page https://www.kaggle.com/datasets/dashelruizperez/covid-19-mexico. 
We used only a subset of the original dataset for our modeling, becuase those the variables we were interested.

## Installation

To run the Jupyter Notebook and perform the analysis, you'll need Python and some necessary libraries. You can set up your environment by following these steps:

1. Clone this repository to your local machine:

   git clone https://github.com/DRPproton/Mexico-covid-prediction.git

   Running a Python environment using Pipenv involves creating a virtual environment, managing dependencies, and running your Python scripts within that environment. Here are the steps to set up and run a Python environment using Pipenv:

1. **Install Pipenv (if not already installed)**:
   If you don't have Pipenv installed, you can do so using `pip`, the Python package manager. Open your terminal or command prompt and run the following command:

   ```bash
   pip install pipenv
   ```

2. **Navigate to Project Directory**:
   Navigate to project directory it using the terminal.

   ```bash
   cd project_directory
   ```

3. **Initialize a New Pipenv Environment and Install Dependencies**:
   Inside your project directory, run the following command to create a new Pipenv environment and install Python packages and dependencies for your project using `pipenv install`.
   
   ```bash
   pipenv install
   ```

   This will add the package to your `Pipfile` and install it within the virtual environment.

4. **Activate the Pipenv Shell** (Optional):
   If not already activated, you can activate the Pipenv shell to work within the virtual environment:

   ```bash
   pipenv shell
   ```

   Your terminal prompt will change to indicate that you are now working within the Pipenv virtual environment.

5. **Run Python Scripts**:
   You can now run your Python scripts within the Pipenv virtual environment. For example, if you have a script named `my_script.py`, you can run it with:
    
   ```bash
   python predict.py
   ```
   
6. **Run Jupyter Notebook**:
   You can now run the Notebook within the Pipenv virtual environment. For example, you can run it with:
    
   ```bash
   jupyter lab
   ```

   Any packages installed using `pipenv install` will be available for your scripts within the virtual environment.

## Run Flask API Locally and testing

1. **Run Python Scripts**:
   You can now run your Flask scripts within the Pipenv virtual environment.
   ```bash
   python predict.py
   ```
   
2. **Test APIs**:
   Open a new shell with the enviroment activated and run the script bellow to test the api.
   The test_api.py file have a sample of a patiente, feel free to change the parameters to see how the changes affect the result. 
  ```bash
   python test_api.py
   ```

   ```
   patient = {'sexo': 1.0,
 'neumonia': 1.0,
 'edad': 75,
 'diabetes': 1.0,
 'epoc': 1.0,
 'inmusupr': 0.0,
 'hipertension': 1.0,
 'cardiovascular': 1.0,
 'obesidad': 1.0,
 'renal_cronica': 0.0}```

## Creating a Docker image using a Dockerfile involves several steps. Below are the commands and steps to build a Docker image from a Dockerfile:

1. **Navigate to the ***midterm_deployment*** folder inside the main project**:

2. **Build the Docker image**:
   Use the `docker build` command to build an image based on the Dockerfile. Replace `your-image-name` with the name you want to give to your Docker image:

   ```bash
   docker build -t your-image-name .
   ```

   The `.` at the end of the command indicates that the Dockerfile is located in the current directory.

3. **Check the list of Docker images**:
   To verify that your image was successfully created, use the `docker images` command:

   ```bash
   docker images
   ```
   You should see your newly created image in the list.

4. **Run a container from the Docker image (optional)**:
   If you want to test your image, you can run a container based on it using the `docker run` command. Replace `your-container-name` with a name for your container:

   ```bash
   docker run -d --name your-container-name your-image-name
   ```
   The `-d` flag runs the container in detached mode. You can access the running container using its name.

5. **Test your application run Python Test Scripts**:
   Open a new shell with the enviroment activated and run the script bellow.
   ```bash
   python test_api.py
   ```

## Testing the live API
1. **Open files**:
   Open a new shell with the enviroment activated and run the script bellow.
   Open the file test_api.py in your IDE
   Uncomment lines 15 and 16 and comment line 19
3. **Test your application run Python Test Scripts**:
   Save file and run it on the shell using the command bellow.
   ```bash
   python test_api.py
   ```



   
