import os
import cv2
import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import StandardScaler, label_binarize
import pandas as pd

dataset_path = "dataset"

classes = [
    "Normal",
    "Abnormal_Heartbeat",
    "Myocardial_Infarction",
    "History_MI"
]

data = []
labels = []

for label, category in enumerate(classes):
    folder = os.path.join(dataset_path, category)
    for img in os.listdir(folder):
        img_path = os.path.join(folder, img)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (64,64))
        image = cv2.GaussianBlur(image,(3,3),0)
        image = cv2.equalizeHist(image)
        image = image.flatten()
        data.append(image)
        labels.append(label)

data = np.array(data)
labels = np.array(labels)

print("Dataset Loaded:", data.shape)

X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42, stratify=labels
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted")
recall = recall_score(y_test, y_pred, average="weighted")
f1 = f1_score(y_test, y_pred, average="weighted")

print(classification_report(y_test, y_pred, target_names=classes))

cm = confusion_matrix(y_test, y_pred)

scores = cross_val_score(knn, data, labels, cv=5)
print("Cross Validation Scores:", scores)
print("Mean CV Score:", scores.mean())

metrics_df = pd.DataFrame({
    "Metric":["Accuracy","Precision","Recall","F1 Score"],
    "Value":[accuracy,precision,recall,f1]
})



k_values = range(1,15)
errors = []

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train,y_train)
    pred = model.predict(X_test)
    errors.append(np.mean(pred != y_test))



y_test_bin = label_binarize(y_test, classes=[0,1,2,3])
y_score = knn.predict_proba(X_test)

for i in range(len(classes)):
    fpr,tpr,_ = roc_curve(y_test_bin[:,i],y_score[:,i])
    roc_auc = auc(fpr,tpr)
    plt.plot(fpr,tpr,label=classes[i]+" AUC="+str(round(roc_auc,2)))


joblib.dump(knn,"model.pkl")
