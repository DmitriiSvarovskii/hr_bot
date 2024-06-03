from src.schemas import test_schemas


common_text = {
    'start_text': "Вы сейчас пройдёте тестирование по Типологии Майерс – "
    "Бриггс. Вам нужно будет ответить на 70 вопросов. Тест займёт +/- 15-20 "
    "минут. Для ответа на вопросы используйте кнопки 'а' и 'б', для того,"
    " чтобы прервать тестирование, нажмите на кнопку "
    '"Прервать прохождение".',
    'cancel_text': "Вы прервали прохождение теста.",
    'select_item': "Выберите интересующий Вас пункт меню.",
    'you_dont_have_test': 'У Вас пока нет пройденных тестов',
    'empl_dont_have_test': 'У сотрудника нет пройденных тестов',
    'select_result_empl_test': 'Выберите сотрудника, результат которого '
                               'Вас интересует',
    'select_result_test': 'Выберите тест, по которому Вас интересует '
                          'результат.',
}


async def generate_result_text(data: test_schemas.ResultTestRead) -> str:
    message = (
        f"Результат теста от {data.created_at.strftime('%d.%m.%Y')}\n"
        f"e = {data.e}"
        f"\ni = {data.i}"
        f"\ns = {data.s}"
        f"\nn = {data.n}"
        f"\nt = {data.t}"
        f"\nf = {data.f}"
        f"\nj = {data.j}"
        f"\np = {data.p}"
    )
    return message


async def generate_result_finish_test(
    data: test_schemas.ResultTestBase
) -> str:
    message = (
        "Вы завершили выполнение теста. Ваш результат\n"
        f"e = {data.e}"
        f"\ni = {data.i}"
        f"\ns = {data.s}"
        f"\nn = {data.n}"
        f"\nt = {data.t}"
        f"\nf = {data.f}"
        f"\nj = {data.j}"
        f"\np = {data.p}"
        "\nДля расшифровки результата обратитесь к @alena_bigdig_ital"
    )
    return message
