# Disease Prediction from Symptoms

This project predicts possible diseases based on symptoms selected by the user. It uses a machine learning model trained on a set of disease symptoms, applying the Naive Bayes classifier to diagnose diseases based on symptom patterns.

## Table of Contents
- [Project Overview](#ProjectOverview)
- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Dataset](#Dataset)
- [GUI Interface](#GUIInterface)
- [Model](#Model)
- [Results](#Result)
- [License](#License)
## Project Overview 
This application leverages machine learning to predict diseases based on user-selected symptoms. The GUI allows users to input symptoms, and the model outputs a predicted disease based on the input data.
## Features
- Symptom-based disease prediction using a Naive Bayes model.
- User-friendly GUI for selecting symptoms and displaying predictions.
- Real-time prediction accuracy feedback.

## Installation
1. Install dependencies: Ensure you have Python installed, then   install the required libraries using the command below:

```bash 
  pip install pandas numpy scikit-learn tkinter 
```
2.Run the Application: Execute the script to start the GUI:
  ```bash
    python disease_prediction.py
  ```
## Usage
- Launch the application.
- Select up to five symptoms from the drop-down menus.
- Click on Predict Disease to see the predicted disease based on selected symptoms.
## Dataset
- Training Data: The model is trained on a dataset (Training.csv) that includes a variety of symptoms and corresponding diseases.
- Testing Data: Testing is performed on a separate dataset (Testing.csv) to evaluate the model’s accuracy.
The datasets must include symptoms as columns and a final column labeled "prognosis" representing the disease.
## GUI Interface
The application includes a graphical interface built with Tkinter:

- Symptom selection via drop-down menus.
- Predict Disease button for real-time prediction.
- Prediction display showing the name of the most likely disease based on symptoms.
## Model
  The model utilizes the Naive Bayes classifier (MultinomialNB) for prediction:

- Training: The model is trained on the symptoms provided in the training dataset.
- Testing: Accuracy is tested using a separate testing dataset.
## Results
The model's accuracy on the test data is printed upon launching, which gives insight into prediction reliability. The achieved accuracy in current testing is around 100% . 
