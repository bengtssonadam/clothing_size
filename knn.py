import math
import pandas as pd
from collections import Counter


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
    females = pd.read_csv('female_clean_tshirt.csv')
    heights = females.height.tolist()
    weights = females.weight.tolist()
    y = females['size'].tolist()

    X = [(heights[i], weights[i])for i in range(len(heights))]
    for k in (3, 5, 7, 9, 11):
        knn = KNN(k)
        knn.fit(X, y)

        result = knn.predict(160, 67)

        print('You should have', result, 'as your t-shirt size with k=', k)


if __name__ == '__main__':
    main()
