# Diabetes Prediction App

This project is a **Diabetes Prediction Web Application** built using a Machine Learning model trained on a healthcare dataset. Users can input key health parameters (e.g. Glucose, BMI, Age, Pregnancies), and the app predicts their likelihood of having diabetes.

The solution consists of:
- A **Jupyter Notebook** for data exploration, model training & evaluation.
- [You can see ml_Diabetes_jupyter_notebook]
- (https://github.com/GiftAkintotu/Diabetes-Project/blob/main/diabetes.data.ipynb)
- ![Data exploration visualization Screenshot]
  (https://github.com/GiftAkintotu/Diabetes-Project/blob/main/Data%20exploration_visualization.png)

- A **Streamlit** app for a user-friendly interface to make predictions.
- ![App Screenshot](https://github.com/GiftAkintotu/Diabetes-Project/blob/main/Screenshot%20of%20diabetes%20app.png)


  ## Key Features
- Loads a pre-trained Diabetes model and scaler.
- Scales user inputs and provides real-time diabetes risk predictions.
- Displays the predicted outcome with confidence level.
- Interactive interface powered by Streamlit.

## Dataset
This project is trained on the **Pima Indians Diabetes Dataset** containing features such as:
- Glucose
- BMI
- Age
- Pregnancies
- Insulin
- SkinThickness
- DiabetesPedigreeFunction
- BloodPressure

You can obtain the dataset from [UCI Machine Learning Repository](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database?select=diabetes.csv).

## Feature Selection Technique
- We can use correlation matrix to pick the most important feature
- Correlation Matrix measure the linear relationship between the target and the feature
- Helps visualize which features are strongly correlated with outcome
  (https://github.com/GiftAkintotu/Diabetes-Project/blob/main/correlation%20matrix.png)

## Model Development
1. Preprocessing: Features were scaled using StandardScaler.
2. Model Training: A LogisticRegression model was trained and saved with joblib.
3. Evaluation:
   - Accuracy: ~80%
   - Confusion Matrix and metrics were calculated.

## Streamlit Application
Run the `Diabetes_ui.py` file to launch a local web app:
```bash
streamlit run Diabetes_ui.py
You will see:
Input fields for Glucose, BMI, Age, Pregnancies.
A "Prediction" button that returns:
Diabetic or Not Diabetic
Prediction confidence (probability score)

## Installation & Usage
- git clone https://github.com/GiftAkintotu/Diabetes-Project.git
- cd diabetes-prediction-app
- pip install -r requirements.txt
- streamlit run Diabetes_ui.py

## **Project Structure**
- ├── diabetes.data.ipynb         # Notebook for EDA, Model Training & Evaluation
- ├── Diabetes_ui.py        # Streamlit UI for making predictions
- ├── new_diabetes_model.pkl    # Saved trained model
- ├── new_scaler.pkl            # Saved scaler for preprocessing
- ├── requirements.txt          # Dependencies
- └── README.md

## Contact
Feel free to reach out:
- GitHub: [https://github.com/Owaboye](https://github.com/Owaboye/diabetes_detection_ml_appp/tree/main)
- LinkedIn: [Gift Akintotu](https://www.linkedin.com/in/gift-akintotu-38b38b220/)
