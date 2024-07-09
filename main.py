import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from KNN import KNN

cmap = ListedColormap(['#FF0000','#00FF00','#0000FF'])

iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
# plt.figure()
# plt.scatter(X[:,2],X[:,3], c=y, cmap=cmap, edgecolor='k', s=20)
# plt.show()



X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y_train = np.array([0, 1, 0, 1, 0])
X_test = np.array([[1.5, 2.5], [3.5, 4.5]])

clf = KNN(k=5)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
predictions = [int(pred) for pred in predictions]

print(f"X_train: {X_train}")
print(f"y_train: {y_train}")

print(f"X_test: {X_test}")
print(f"y_test: {y_test}")

# accuracy = np.sum(predictions == y_test) / len(y_test)
# print(f"accuracy: {accuracy}")

print("Predictions:", predictions)

# Plotting
plt.figure(figsize=(10, 6))

# Plot training data
for i, point in enumerate(X_train):
    if y_train[i] == 0:
        plt.scatter(point[0], point[1], color='blue', label='Class 0' if i == 0 else "")
    else:
        plt.scatter(point[0], point[1], color='red', label='Class 1' if i == 1 else "")

# Plot test data
for i, point in enumerate(X_test):
    if predictions[i] == 0:
        plt.scatter(point[0], point[1], color='cyan', edgecolors='k', marker='x', s=100, label='Test Prediction Class 0' if i == 0 else "")
    else:
        plt.scatter(point[0], point[1], color='magenta', edgecolors='k', marker='x', s=100, label='Test Prediction Class 1' if i == 1 else "")

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('k-NN Classification')
plt.legend()
plt.show()