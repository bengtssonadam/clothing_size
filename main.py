import math
from collections import Counter
from sklearn.neighbors import KNeighborsClassifier

import pandas as pd
from sklearn.svm import SVC


class KNN:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, height, weight):
        dists = []
        for i, d in enumerate(self.X_train):
            h, w = d
            delta_x = height - h
            delta_y = weight - w
            dist = math.sqrt(delta_x**2 + delta_y**2)
            dists.append((dist, self.y_train[i]))
        dists.sort(key=lambda data: data[0])
        sizes = [d[1] for d in dists[:self.k]]
        return Counter(sizes).most_common(1)[0][0]


def main():
    garment = input('Are you looking for pants or a tshirt?')
    gender = input('Chooses your gender: (male/female) ')

    df = pd.read_csv(gender + garment + '.csv')

    heights = df.height.tolist()
    weights = df.weight.tolist()
    y = df['size'].tolist()

    X = [(heights[i], weights[i]) for i in range(len(heights))]

    user_height = int(input('Enter your height in cm: '))
    user_weight = int(input('Enter your weight in kg: '))

    user_data = (user_height, user_weight)
    svc_X = list(zip(heights, weights))

    for k in (3, 5, 7, 9, 11, 99):
        knn = KNN(k)
        knn.fit(X, y)
        print('k =', k)

        result = knn.predict(user_height, user_weight)

        print(f'You should have {result} as your size in {gender} {garment}')

        clf_knn = KNeighborsClassifier(n_neighbors=k)

        clf_knn.fit(X, y)

        predicted = clf_knn.predict([user_data])
        print("sklearn's knn prediction is: ", predicted[0])

        svc = SVC(kernel='linear')
        svc.fit(svc_X, y)
        print(f'SVM prediction is: {svc.predict([[user_height, user_weight]])}')

        print('*'*40)


if __name__ == '__main__':
    main()
