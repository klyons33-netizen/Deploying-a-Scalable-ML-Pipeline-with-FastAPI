# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This machine learning model uses demographic and employment data from the U.S. Census Bureau to predict whether an individual's income exceeds $50,000. The model used is the RandomForestClassifier model via Scikit-Learn. One-hot encoding was used to encode categorical features, and the target variable was converted to a binary label using a LabelBinarizer. The model was then trained as part of a Machine Learning DevOps pipeline, developed with Python.

## Intended Use

This model and program are purely for educational purposes, as part of a project for a Western Governors' University class, D501. Its purpose is to demonstrate my knowledge of machine learning, model training, and pipeline creation, while predicting if a person's income exceeds $50,000 a year based on demographic information. Demographic information includes age, education, marital status, hours worked per week, occupation, and more. This model is not intended for commercial or other use outside of educational purposes.

## Training Data

The data used in this model was collected from the U.S. Census Bureau and includes demographic and employment information. This model was trained using this dataset. Features include age, occupation, education, marital status, and more. The target variable for this model is salary, specifically whether an individual's income is less than or equal to $50,000 or greater than $50,000. An 80/20 train-test split was used: 80% of the records were used for training, and 20% for evaluation.

## Evaluation Data

The dataset was evaluated using a 20% holdout portion of the data gathered from the Census dataset - the portion of the data that was not used to train the model. This gives us a more accurate assessment of the model's development and prediction success. This evaluation data was preprocessed in the same manner as the trained data, with encoding and using a label binarizer.

## Metrics

This model was evaluated using precision, recall, and F1 score. The results are as follows:

- Precision: 0.7419
- Precision measures the proportion of positive predictions that were correct.

- Recall: 0.6384
- Recall measures the proportion of positive cases that were identified correctly.

- F1 Score: 0.6863
- F1 score combines precision and recall for a balanced measure.

## Ethical Considerations

The nature of the dataset we are working with, the U.S. Census Bureau data, is sensitive in nature - it contains demographic information about many people, including attributes such as race, sex, and native country. This can inadvertently introduce bias into the model if it uses this information to make predictions and assess patterns in the data, leading to variance in predictions across demographic groups. Thus, this model should be assessed carefully about population groups - using different groups for training and assessment would be the fairest.

## Caveats and Recommendations

Once again, this model was developed solely for educational purposes. Training results may vary when the model is evaluated on different data samples or with a different train-test split. Future improvements should build on previous ethical considerations to produce the fairest data results and incorporate higher-level engineering to achieve more accurate results. This model should not be used for high-stakes decision-making without further testing.