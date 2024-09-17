"fields must be private"
class KNN:
    def __init__(self, k=1):
        self.k = k
        self.observations = None #not necessary but can be you used to save observations
        self.ground_truth = None
        self._parameters = {}

    def another(a, b):
            return KNN()

    def fit(self): #to use knn.fit() you need self
            self.observations = observations
            self.ground_truth = ground_truth
            self._parameters = {
                "observations": observations,
                "ground_truth": ground_truth}

    def predict(self, observations):
        predictions = [self._predict_single(x) for x in observations]
        return predictions

    def _predict_single(self, observations): #user gives 1 point and you have to predict where the point is
        # TODO: predict a single point
        # step1 : calc distance between observation and ever other point
        distances = np.linalg.norm(self._parameters["observations"] - observation, axis=1)
        # step2 : sort the array of the distances and take first k
        k_indices = np.argsort(distances)[:self.k]
        # step3 : check the label aka ground truth of those points. now we have k = 3, 3 labels inside an array
        k_nearest_labels = [self._parameters["ground_truth"] [i] for i in k_indices]
        # step4 : take most common label and return it to the caller
        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]

class FruitClassifier(KNN):
    def __init__(self, k=3):
        super().__init__(k)
