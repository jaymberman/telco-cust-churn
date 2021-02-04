import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score
from joblib import dump

PATH_TO_DATA = "../dataset/processed_data"


def load_and_process_data(path):
    X_train = np.load(path + '/X_train.npy')
    X_test = np.load(path + '/X_test.npy')
    y_train = pd.read_csv(path + '/y_train', header=None)
    y_test = pd.read_csv(path + '/y_test', header=None)
    return X_train, X_test, y_train, y_test


def build_model():
    model = RandomForestClassifier(min_samples_leaf=2,
                                   min_samples_split=4,
                                   n_estimators=200,
                                   max_features=0.3,
                                   n_jobs=-1,
                                   random_state=42)
    return model


def train_model():
    model = build_model()
    X_train, X_test, y_train, y_test = load_and_process_data(PATH_TO_DATA)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    model.fit(X_train, y_train.ravel())
    y_pred = model.predict(X_test)

    print(f"test accuracy: {accuracy_score(y_test, y_pred)}")
    print(f"precision accuracy: {precision_score(y_test, y_pred)}")
    print(f"recall accuracy: {recall_score(y_test, y_pred)}")

    return model

def main():
    model = train_model()
    dump(model, 'model.joblib')

if __name__ == "__main__":
    main()