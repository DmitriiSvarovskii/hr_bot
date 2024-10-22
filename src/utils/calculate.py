from src.lexicons import answers as answer
from itertools import product


def calculate_scores(answers):
    scores = {'e': 0, 'i': 0, 's': 0, 'n': 0, 't': 0, 'f': 0, 'j': 0, 'p': 0}

    questions_map = {
        'e': [1, 8, 15, 22, 29, 36, 43, 50, 57, 64],
        'i': [1, 8, 15, 22, 29, 36, 43, 50, 57, 64],
        's': [2, 3, 9, 10, 16, 17, 23, 24, 30, 31, 37, 38, 44, 45, 51, 52, 58, 59, 65, 66],
        'n': [2, 3, 9, 10, 16, 17, 23, 24, 30, 31, 37, 38, 44, 45, 51, 52, 58, 59, 65, 66],
        't': [4, 5, 11, 12, 18, 19, 25, 26, 32, 33, 39, 40, 46, 47, 53, 54, 60, 61, 67, 68],
        'f': [4, 5, 11, 12, 18, 19, 25, 26, 32, 33, 39, 40, 46, 47, 53, 54, 60, 61, 67, 68],
        'j': [6, 7, 13, 14, 20, 21, 27, 28, 34, 35, 41, 42, 48, 49, 55, 56, 62, 63, 69, 70],
        'p': [6, 7, 13, 14, 20, 21, 27, 28, 34, 35, 41, 42, 48, 49, 55, 56, 62, 63, 69, 70]
    }

    for key, value in answers.items():
        question_num = int(key.split('_')[1])
        if value == answer.answers['a']:
            for k, v in questions_map.items():
                if k in ['e', 's', 't', 'j'] and question_num in v:
                    scores[k] += 1
                    break
        elif value == answer.answers['b']:
            for k, v in questions_map.items():
                if k in ['i', 'n', 'f', 'p'] and question_num in v:
                    scores[k] += 1
                    break

    # Определяем возможные типы личности
    pairs = [('e', 'i'), ('s', 'n'), ('t', 'f'), ('j', 'p')]

    def get_letter(a, b):
        if scores[a] > scores[b]:
            return [a.upper()]
        elif scores[a] < scores[b]:
            return [b.upper()]
        else:
            return [a.upper(), b.upper()]

    letters_list = [get_letter(a, b) for a, b in pairs]
    types = [''.join(combination).lower()
             for combination in product(*letters_list)]

    return scores, types
