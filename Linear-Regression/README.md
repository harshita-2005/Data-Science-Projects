**Introduction:**
Housing Price Prediction using Linear Regression:
This project aims to predict housing prices based on various features such as area, number of bedrooms, bathrooms, and other amenities. It utilizes Linear Regression for modeling the relationship between the features and the target variable (price).

**Data Preprocessing:**
The prefarea column is dropped as it is not used in the prediction.
Categorical columns are encoded as follows:
Yes/No values are replaced with 1/0.
furnishingstatus is replaced with 1 for furnished, 0.5 for semi-furnished, and 0 for unfurnished.

**Model Training":**
The dataset is split into training and testing sets using train_test_split. The input features are normalized using MinMaxScaler. A Linear Regression model is then fitted to the training data.

**Conclusion:**
This project demonstrates a simple approach to predicting housing prices using Linear Regression.The model predicts housing prices based on the test data. You can visualize the predicted prices versus the actual prices using Matplotlib.
