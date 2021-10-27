from collections import Counter


class CountVectorizer:
    def __init__(self):
        self.feature_names = set()

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)

    def fit(self, corpus):
        for one_text in corpus:
            words = one_text.lower().split()
            for word in words:
                self.feature_names.add(word)

    def transform(self, corpus):
        count_matrix = []
        for one_text in corpus:
            row = []
            counter = Counter(one_text.lower().split())
            for word in self.feature_names:
                row.append(counter.get(word, 0))
            count_matrix.append(row)
        return count_matrix

    def get_feature_names(self):
        return self.feature_names


if __name__ == '__main__':
    corpus_ = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix_ = vectorizer.fit_transform(corpus_)
    print(vectorizer.get_feature_names())
    print(count_matrix_)

