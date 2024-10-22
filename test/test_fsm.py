import pytest
from src.utils.calculate import calculate_scores
from src.lexicons import answers as answer


@pytest.fixture
def total_questions():
    return 70


@pytest.fixture
def answers_dict():
    return answer.answers


def generate_answers(answer_type, total_questions):
    return {f'q_{i+1}': answer_type for i in range(total_questions)}


def print_scores(scores):
    print()  # Добавляем пустую строку перед выводом
    for key in ['e', 'i', 's', 'n', 't', 'f', 'j', 'p']:
        print(f"{key}: {scores[key]}")


def test_all_answers_a(total_questions, answers_dict):
    answers = generate_answers(answers_dict['a'], total_questions)
    expected_scores = {'e': 10, 'i': 0, 's': 20,
                       'n': 0, 't': 20, 'f': 0, 'j': 20, 'p': 0}
    scores = calculate_scores(answers)
    print_scores(scores)
    assert scores == expected_scores


def test_all_answers_b(total_questions, answers_dict):
    answers = generate_answers(answers_dict['b'], total_questions)
    expected_scores = {'e': 0, 'i': 10, 's': 0,
                       'n': 20, 't': 0, 'f': 20, 'j': 0, 'p': 20}
    scores = calculate_scores(answers)
    print_scores(scores)
    assert scores == expected_scores


def test_half_a_half_b(total_questions, answers_dict):
    answers = {f'q_{i+1}': answers_dict['a'] if i <
               35 else answers_dict['b'] for i in range(total_questions)}
    expected_scores = {'e': 5, 'i': 5, 's': 10,
                       'n': 10, 't': 10, 'f': 10, 'j': 10, 'p': 10}
    scores = calculate_scores(answers)
    print_scores(scores)
    assert scores == expected_scores
