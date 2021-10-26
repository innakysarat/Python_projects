from collections import Counter

class CountVectorizer():
    def __init__(self):
        self.count_matrix = list()
        self.feature_names = []

    def fit_transform(self, corpus):
        CountVectorizer.split(self, corpus)
        feature_position = {feature: position for position, feature in enumerate(self.feature_names)}
        for one_text in corpus:
            one_matrix = [0] * len(self.feature_names)
            counter = Counter(CountVectorizer.split_one_text(one_text))
            for word, count in counter.items():
                one_matrix[feature_position[word]] = count
            self.count_matrix.append(one_matrix)
        return self.count_matrix

    def fit_transform_another_version(self, corpus):
        CountVectorizer.split(self, corpus)
        for one_text in corpus:
            count_matrix = {feature: 0 for position, feature in enumerate(self.feature_names)}
            words_in_one_text = CountVectorizer.split_one_text(one_text)
            for word in words_in_one_text:
                count_matrix[word] = count_matrix.get(word, 0) + 1
            self.count_matrix.append(count_matrix)
        return self.count_matrix

    @staticmethod
    def split_one_text(text: str) -> [str]:
        return text.lower().split()

    def split(self, corp: []):
        for one_text in corp:
            words = one_text.split()
            for word in words:
                if word.lower() not in self.feature_names:
                    self.feature_names.append(word.lower())

    def get_feature_names(self):
        return self.feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform_another_version(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
