class Evaluator:
    @staticmethod
    def zip_evaluate(coefs: list, words: list) -> float:
        if len(coefs) != len(words):
            return -1
        result = 0
        for c, w in zip(coefs, words):
            result += c * len(w)
        return result

    @staticmethod
    def enumerate_evaluate(coefs: list, words: list) -> float:
        if len(coefs) != len(words):
            return -1
        result = 0
        for i, w in enumerate(words):
            result += coefs[i] * len(w)
        return result


if __name__ == '__main__':
    test_words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    test_coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(test_coefs, test_words))
    print(Evaluator.enumerate_evaluate(test_coefs, test_words))
    # 32.0
    test_words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    test_coefs = [0.02, -1.0, 1.0, -12.0, 0.1, 42.42, 1.9]
    print(Evaluator.zip_evaluate(test_coefs, test_words))
    print(Evaluator.enumerate_evaluate(test_coefs, test_words))
    # 115.0
    test_words = ["Lists", "do", "not", "have", "same", "length"]
    test_coefs = [1.0, 2.0, 1.0, 4.0]
    print(Evaluator.zip_evaluate(test_coefs, test_words))
    print(Evaluator.enumerate_evaluate(test_coefs, test_words))
    # -1
