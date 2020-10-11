
import numpy as np
import pandas as pd
import nltk
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score
from sklearn.metrics import confusion_matrix
from sklearn.grid_search import GridSearchCV
dominant_wrist_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_train\\dominant_wrist_train.csv')
train_data_wrist = dominant_wrist_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_wrist = dominant_wrist_file[['Activity']].values.ravel()
print "Training data dimensions for sensor at dominant_wrist position"
print train_data_wrist.shape
print target_label_wrist.shape

print "----------------------------------------------------------------------------"
print "\n"
dominant_wrist_file_test = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_test\\dominant_wrist_test.csv')
test_data_wrist = dominant_wrist_file_test[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_wrist_test = dominant_wrist_file_test[['Activity']].values.ravel()
print "Testing data dimensions for sensor at dominant_wrist position"
print test_data_wrist.shape
print target_label_wrist_test.shape

print "----------------------------------------------------------------------------"
print "\n"
rfc_wrist = RandomForestClassifier(n_estimators=100, criterion='entropy',n_jobs=-1)
param_grid = {
    'n_estimators': [50, 100, 200],
    'criterion': ['entropy', 'gini']
}
rfc_wrist_gs = GridSearchCV(rfc_wrist, param_grid=param_grid)
rfc_wrist_gs.fit(train_data_wrist, target_label_wrist)
predicted = rfc_wrist_gs.predict(test_data_wrist)
print "Classification report for sensor at Wrist position"
print metrics.classification_report(target_label_wrist_test, predicted)
print metrics.confusion_matrix(target_label_wrist_test, predicted)
print "F-Score: ",metrics.f1_score(target_label_wrist_test, predicted)
activities = ['sitting:-legs-straight','cycling:-70-rpm_-50-watts_-.7-kg','walking:-natural','lying:-on-back']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(activities))
    plt.xticks(tick_marks, activities, rotation=45)
    plt.yticks(tick_marks, activities)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
cm = confusion_matrix(target_label_wrist_test, predicted, labels=activities)
np.set_printoptions(precision=2)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print('Normalized confusion matrix for Sensor located at Dominant Wrist position')
print(cm_normalized)
plt.figure(figsize=(10,10))
plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix for Sensor located at Dominant Wrist position')
plt.savefig('confusion_matrix.png')
plt.show()

print "--------------------------------------------------------------------------------------"
print "\n"
dominant_wrist_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_33\\dominant_wrist_train.csv')
train_data_wrist = dominant_wrist_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_wrist = dominant_wrist_file[['Activity']].values.ravel()

print "Beginning 10-Fold cross validation on all the 33 subjects for sensor at wrist position..."
clf_cross_val = RandomForestClassifier(n_estimators=50, criterion='gini')
scores = cross_val_score(clf_cross_val, train_data_wrist,target_label_wrist,cv=10)
print "Scores for each fold:"
print scores
print "\n"
print "---------------------------------------------------------------------------------"
print ("Accuracy for 10-Fold cross validation using Random Forest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
dominant_upperarm_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_train\\dominant_Upper_Arm_train.csv')
train_data_upperarm = dominant_upperarm_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_upperarm = dominant_upperarm_file[['Activity']].values.ravel()
print "Training data dimensions for sensor at dominant_upper_arm position"
print train_data_upperarm.shape
print target_label_upperarm.shape
print "----------------------------------------------------------------------------"
print "\n"
dominant_upperarm_file_test = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_test\\dominant_Upper_Arm_test.csv')
test_data_upperarm = dominant_upperarm_file_test[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_upperarm_test = dominant_upperarm_file_test[['Activity']].values.ravel()
print "Testing data dimensions for sensor at dominant_upper_arm position"
print test_data_upperarm.shape
print target_label_upperarm_test.shape
print "----------------------------------------------------------------------------"
print "\n"
rfc_upperarm = RandomForestClassifier(n_estimators=100, criterion='entropy',n_jobs=-1)
param_grid = {
    'n_estimators': [50, 100, 200],
    'criterion': ['entropy', 'gini']
}
rfc_arm_gs = GridSearchCV(rfc_upperarm, param_grid=param_grid)
rfc_arm_gs.fit(train_data_upperarm, target_label_upperarm)
predicted = rfc_arm_gs.predict(test_data_upperarm)
print "Classification report for sensor at Upper_Arm position"
print metrics.classification_report(target_label_upperarm_test, predicted)
print metrics.confusion_matrix(target_label_upperarm_test, predicted)
print "F-Score: ",metrics.f1_score(target_label_upperarm_test, predicted)
activities = ['sitting:-legs-straight','cycling:-70-rpm_-50-watts_-.7-kg','walking:-natural','lying:-on-back']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(activities))
    plt.xticks(tick_marks, activities, rotation=45)
    plt.yticks(tick_marks, activities)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print('Normalized confusion matrix for Sensor located at Upper Arm position')
print(cm_normalized)
plt.figure(figsize=(10,10))
plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix for Sensor located at Upper Arm position')
plt.savefig('confusion_matrix.png')
plt.show()

print "--------------------------------------------------------------------------------------"
print "\n"
dominant_upperarm_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_33\\dominant_Upper_Arm_train.csv')
train_data_upperarm = dominant_upperarm_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_upperarm = dominant_upperarm_file[['Activity']].values.ravel()
print "Beginning 10-Fold cross validation on all the 33 subjects for sensor at upper arm position..."
clf_upperarm_cross_val = RandomForestClassifier(n_estimators=100, criterion='gini')
scores = cross_val_score(clf_upperarm_cross_val, train_data_upperarm,target_label_upperarm,cv=10)
print "Scores for each fold:"
print scores
print "\n"
print "---------------------------------------------------------------------------------"
print ("Accuracy for 10Fold cross validation using Random Forest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
dominant_thigh_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_train\\dominant_Thigh_train.csv')
train_data_thigh = dominant_thigh_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_thigh = dominant_thigh_file[['Activity']].values.ravel()
print "Training data dimensions for sensor at dominant_thigh position"
print train_data_thigh.shape
print target_label_thigh.shape
print "----------------------------------------------------------------------------"
print "\n"
dominant_thigh_file_test = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_test\\dominant_Thigh_test.csv')
test_data_thigh = dominant_thigh_file_test[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_thigh_test = dominant_thigh_file_test[['Activity']].values.ravel()
print "Testing data dimensions for sensor at dominant_thigh position"
print test_data_thigh.shape
print target_label_thigh_test.shape
print "----------------------------------------------------------------------------"
rfc_thigh = RandomForestClassifier(n_estimators=100, criterion='entropy',n_jobs=-1)
param_grid = {
    'n_estimators': [50, 100, 200],
    'criterion': ['entropy', 'gini']
}
rfc_thigh_gs = GridSearchCV(rfc_thigh, param_grid=param_grid)
rfc_thigh_gs.fit(train_data_thigh, target_label_thigh)
predicted = rfc_thigh_gs.predict(test_data_thigh)
print "Classification report for sensor at Thigh position"
print metrics.classification_report(target_label_thigh_test, predicted)
print metrics.confusion_matrix(target_label_thigh_test, predicted)
print "F-Score: ",metrics.f1_score(target_label_thigh_test, predicted)
activities = ['sitting:-legs-straight','cycling:-70-rpm_-50-watts_-.7-kg','walking:-natural','lying:-on-back']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(activities))
    plt.xticks(tick_marks, activities, rotation=45)
    plt.yticks(tick_marks, activities)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
cm = confusion_matrix(target_label_thigh_test, predicted, labels=activities)
np.set_printoptions(precision=2)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print('Normalized confusion matrix for Sensor located at Dominant Thigh position')
print(cm_normalized)
plt.figure(figsize=(10,10))
plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix for Sensor located at Dominant Thigh position')
plt.savefig('confusion_matrix.png')
plt.show()
print "--------------------------------------------------------------------------------------"
print "\n"
dominant_thigh_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_33\\dominant_Thigh_train.csv')
train_data_thigh = dominant_thigh_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_thigh = dominant_thigh_file[['Activity']].values.ravel()
print "Beginning 10-Fold cross validation on all the 33 subjects for sensor at Thigh position..."
clf_thigh_cross_val = RandomForestClassifier(n_estimators=200, criterion='gini')
scores = cross_val_score(clf_thigh_cross_val, train_data_thigh,target_label_thigh,cv=10)
print "Scores for each fold:"
print scores
print "---------------------------------------------------------------------------------"
print "\n"
print ("Accuracy for 10Fold cross validation using Random Forest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
dominant_hip_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_train\\dominant_Hip_train.csv')
train_data_hip = dominant_hip_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_hip = dominant_hip_file[['Activity']].values.ravel()
print "Training data dimensions for sensor at dominant_hip position"
print train_data_hip.shape
print target_label_hip.shape
print "----------------------------------------------------------------------------"
print "\n"
dominant_hip_file_test = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_test\\dominant_Hip_test.csv')
test_data_hip = dominant_hip_file_test[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_hip_test = dominant_hip_file_test[['Activity']].values.ravel()
print "Testing data dimensions for sensor at dominant_hip position"
print test_data_hip.shape
print target_label_hip_test.shape
print "----------------------------------------------------------------------------"
print "\n"
rfc_hip = RandomForestClassifier(n_estimators=100, criterion='entropy',n_jobs=-1)
param_grid = {
    'n_estimators': [50, 100, 200],
    'criterion': ['entropy', 'gini']
}
rfc_hip_gs = GridSearchCV(rfc_hip, param_grid=param_grid)
rfc_hip_gs.fit(train_data_hip, target_label_hip)
predicted = rfc_hip_gs.predict(test_data_hip)
print "Classification report for sensor at Hip position"
print metrics.classification_report(target_label_hip_test, predicted)
print metrics.confusion_matrix(target_label_hip_test, predicted)
print "F-Score",metrics.f1_score(target_label_hip_test, predicted)
activities = ['sitting:-legs-straight','cycling:-70-rpm_-50-watts_-.7-kg','walking:-natural','lying:-on-back']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(activities))
    plt.xticks(tick_marks, activities, rotation=45)
    plt.yticks(tick_marks, activities)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
cm = confusion_matrix(target_label_hip_test, predicted, labels=activities)
np.set_printoptions(precision=2)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print('Normalized confusion matrix for Sensor located at Dominant Hip position')
print(cm_normalized)
plt.figure(figsize=(10,10))
plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix for Sensor located at Dominant Hip position')
plt.savefig('confusion_matrix.png')
plt.show()
print "--------------------------------------------------------------------------------------"
print "\n"
dominant_hip_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_33\\dominant_Hip_train.csv')
train_data_hip = dominant_hip_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_hip = dominant_hip_file[['Activity']].values.ravel()
print "Beginning 10-Fold cross validation on all the 33 subjects for sensor at Hip position..."
clf_hip_cross_val = RandomForestClassifier(n_estimators=200, criterion='gini')
scores = cross_val_score(clf_hip_cross_val, train_data_hip,target_label_hip,cv=10)
print "Scores for each fold:"
print scores
print "---------------------------------------------------------------------------------"
print "\n"
print ("Accuracy for 10Fold cross validation using Random Forest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
dominant_ankle_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_train\\dominant_Ankle_train.csv')
train_data_ankle = dominant_ankle_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_ankle = dominant_ankle_file[['Activity']].values.ravel()
print "Training data dimensions for sensor at dominant_ankle position"
print train_data_ankle.shape
print target_label_ankle.shape
print "----------------------------------------------------------------------------"
print "\n"
dominant_ankle_file_test = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_test\\dominant_Ankle_test.csv')
test_data_ankle = dominant_ankle_file_test[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_ankle_test = dominant_ankle_file_test[['Activity']].values.ravel()
print "Testing data dimensions for sensor at dominant_ankle position"
print test_data_ankle.shape
print target_label_ankle_test.shape
print "----------------------------------------------------------------------------"
print "\n"
rfc_ankle = RandomForestClassifier(n_estimators=100, criterion='entropy',n_jobs=-1)
param_grid = {
    'n_estimators': [50, 100, 200],
    'criterion': ['entropy', 'gini']
}
rfc_ankle_gs = GridSearchCV(rfc_ankle, param_grid=param_grid)
rfc_ankle_gs.fit(train_data_ankle, target_label_ankle)
predicted = rfc_ankle_gs.predict(test_data_ankle)
print "Classification report for sensor at Ankle position"
print metrics.classification_report(target_label_ankle_test, predicted)
print metrics.confusion_matrix(target_label_ankle_test, predicted)
print "F-Score",metrics.f1_score(target_label_ankle_test, predicted)
activities = ['sitting:-legs-straight','cycling:-70-rpm_-50-watts_-.7-kg','walking:-natural','lying:-on-back']
def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(activities))
    plt.xticks(tick_marks, activities, rotation=45)
    plt.yticks(tick_marks, activities)
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
cm = confusion_matrix(target_label_ankle_test, predicted, labels=activities)
np.set_printoptions(precision=2)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print('Normalized confusion matrix for Sensor located at Dominant Ankle position')
print(cm_normalized)
plt.figure(figsize=(10,10))
plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix for Sensor located at Dominant Ankle position')
plt.savefig('confusion_matrix.png')
plt.show()
print "--------------------------------------------------------------------------------------"
print "\n"
dominant_ankle_file = pd.read_csv('C:\\Users\\shiva\\Desktop\\MLDM PROJECT\\DATA\\sensor_based_files_33\\dominant_Ankle_train.csv')
train_data_ankle = dominant_ankle_file[['MeanSM','StDevSM','MdnSM','belowPer25SM','belowPer75SM','TotPower_0.3_15','FirsDomFre_0.3_15','PowFirsDomFre_0.3_15','SecDomFre_0.3_15','PowSecDomFre_0.3_15','FirsDomFre_0.6_2.5','PowFirsDomFre_0.6_2.5','FirsDomFre_per_TotPower_0.3_15']].values
target_label_ankle = dominant_ankle_file[['Activity']].values.ravel()
print "Beginning 10-Fold cross validation on all the 33 subjects for sensor at Ankle position..."
clf_ankle_cross_val = RandomForestClassifier(n_estimators=100, criterion='entropy')
scores = cross_val_score(clf_ankle_cross_val, train_data_ankle,target_label_ankle,cv=10)
print "Scores for each fold:"
print scores
print "---------------------------------------------------------------------------------"
print "\n"
print ("Accuracy for 10Fold cross validation using Random Forest: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
