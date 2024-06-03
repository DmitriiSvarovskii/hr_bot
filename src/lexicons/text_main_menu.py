main_btn: dict[str, dict[str, str]] = {
    'start_test': {
        'text': 'Пройти тест',
        'callback_data': 'press_start_test'
    },
    'my_result': {
        'text': 'Мои результаты',
        'callback_data': 'press_my_result'
    },
    'result_employees': {
        'text': 'Результаты сотрудников',
        'callback_data': 'press_result_employees'
    },
}


main_menu_dict: dict[str, str] = {
    'start':
        "Вы находитесь в главном меню, выберите интересующий Вас пункт меню."
        " Вы можете посмотреть результаты своих тестов в разделе "
        '"Мои результаты"',
    'start_admin':
        "Вы находитесь в главном меню, выберите интересующий Вас пункт меню."
        " Вы можете посмотреть результаты своих тестов в разделе "
        '"Мои результаты", а также можете посмотреть результаты сотурдников '
        " в соответствуеющем разделе",
    'error_private_chat': 'Извините, этот бот предназначен '
                          'для использования только в '
                          'личных чатах. Если вы хотите воспользоваться ботом,'
                          ' пожалуйста, перейдите в сам бот',
}


back_button_dict: dict[str, dict[str, str]] = {
    'back': {
        'text': '<<< Назад',
        'callback_data': 'press_menu'
    },
}

back_button_admin_dict: dict[str, dict[str, str]] = {
    'back': {
        'text': '<<< Назад',
        'callback_data': 'press_result_employees'
    },
}
