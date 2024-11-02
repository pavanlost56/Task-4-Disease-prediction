from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the training and testing data
train_file = "D:\CodeAlpha Internship\CodeAlpha Internship\ML INTERSHIP\Diseaseprediction\Diseaseprediction\Training.csv"
test_file = "D:\CodeAlpha Internship\CodeAlpha Internship\ML INTERSHIP\Diseaseprediction\Diseaseprediction\Testing.csv"

# Read CSV files
try:
    df_train = pd.read_csv(train_file)
    df_test = pd.read_csv(test_file)
except Exception as e:
    print("Error loading data:", e)
    exit()

# Define symptoms and map diseases to numerical labels
symptoms = df_train.columns[:-1].tolist()  # All columns except 'prognosis'
disease_mapping = {disease: idx for idx, disease in enumerate(df_train['prognosis'].unique())}

# Replace disease names with numeric values in training and testing sets
df_train.replace({'prognosis': disease_mapping}, inplace=True)
df_test.replace({'prognosis': disease_mapping}, inplace=True)

# Training and testing data
X_train = df_train[symptoms]
y_train = df_train['prognosis']
X_test = df_test[symptoms]
y_test = df_test['prognosis']

# Create the model and train it
model = MultinomialNB()
model.fit(X_train, y_train)

# Check accuracy on the testing data
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f"Model accuracy on test data: {accuracy * 100:.2f}%")

# GUI setup
root = Tk()
root.title("Disease Prediction From Symptoms")
root.configure(bg="lightblue")

# Variables to hold user-selected symptoms
Symptom1, Symptom2, Symptom3, Symptom4, Symptom5 = [StringVar() for _ in range(5)]
for var in (Symptom1, Symptom2, Symptom3, Symptom4, Symptom5):
    var.set("None")

# Function to predict the disease based on selected symptoms
def predict_disease():
    selected_symptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    if all(symptom == "None" for symptom in selected_symptoms):
        messagebox.showinfo("Input Error", "Please select at least one symptom.")
        return

    symptom_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
    prediction = model.predict([symptom_vector])[0]
    disease_name = next(disease for disease, idx in disease_mapping.items() if idx == prediction)
    t3.delete("1.0", END)
    t3.insert(END, disease_name)

# GUI layout
Label(root, text="Disease Prediction From Symptoms", font=("Elephant", 20), bg="lightblue").grid(row=0, column=0, columnspan=2)

# Labels for each symptom
for i, text in enumerate(["Symptom 1", "Symptom 2", "Symptom 3", "Symptom 4", "Symptom 5"], start=1):
    Label(root, text=text, font=("Elephant", 15), bg="lightblue").grid(row=i+1, column=0, pady=10, sticky=W)

# OptionMenus for symptom selection
OPTIONS = sorted(symptoms)
OptionMenu(root, Symptom1, *OPTIONS).grid(row=2, column=1)
OptionMenu(root, Symptom2, *OPTIONS).grid(row=3, column=1)
OptionMenu(root, Symptom3, *OPTIONS).grid(row=4, column=1)
OptionMenu(root, Symptom4, *OPTIONS).grid(row=5, column=1)
OptionMenu(root, Symptom5, *OPTIONS).grid(row=6, column=1)

# Button to predict disease
Button(root, text="Predict Disease", command=predict_disease, font=("Elephant", 15), bg="blue", fg="white").grid(row=7, column=1, pady=20)

# Text box to display the result
t3 = Text(root, height=2, width=30, font=("Elephant", 15))
t3.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
