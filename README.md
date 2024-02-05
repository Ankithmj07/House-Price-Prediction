# California House Price Prediction System

## Overview

This repository contains a complete end-to-end machine learning project for predicting house prices in California. The project is based on the California Housing dataset, and it involves the entire machine learning pipeline, from data exploration to model deployment.

## Dataset

The dataset used for this project is the California Housing dataset, which is commonly used for regression tasks. The dataset includes various features such as median housing price, average rooms, population, median income, and more.

Dataset source: [California Housing dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)

## Project Structure

```

.
├── datasets
│   ├── housing
|       ├──housing.csv
│   ├── housing.tgz
├── model_files
│   ├── __init__.py
│   ├── housing.pkl
│   ├── ml_model.py
├── static
│   ├── images
│   ├── script.js
│   ├── style.css
├── templates
│   ├── index.html
├── main.py
├── requirements.txt
├── README.md


```

- **Datasets :** Contains Data
- **Notebook :** Jupyter notebook for data exploration, feature engineering, and model training.
- **model_files :** Python source code for data preprocessing, feature engineering, model training, and utility functions and pre-trained machine learning model (e.g., housing.pkl).
- **main.py :** A simple web application for deploying the trained model.
- **README.md :** Documentation for the project.

 ## Getting Started

1. Clone the repository:
 ```
    git clone https://github.com/Ankithmj07/House-Price-Prediction.git
    cd House-Price-Prediction

 ```

2. Install the required packages:
```
    pip install -r requirements.txt
```

3. Explore the Jupyter notebooks in the to understand the data and the steps taken in the project.

4. Run the Python scripts in the **'model_files'** directory to preprocess the data, perform feature engineering, and train the machine learning model.

5.  Explore the web application for model deployment.

## Model Deployment

The pre-trained model is stored in the **'models_files'** directory. You can use this model for predictions without retraining.

```
import pickle
import numpy as np

# Load the pre-trained model
with open('models_files/housing.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Example prediction with dummy input
input_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]).reshape(1, -1)
prediction = model.predict(input_data)

print(f'Predicted house price: ${prediction[0]:,.2f}')

```

## Web Application

A simple web application has been created for deploying the trained model. To run the application, execute the following command:

```
python app.py
```

Visit http://localhost:8080 in your web browser to interact with the application.

## Feel free to contribute, report issues, or provide feedback. Happy coding!
