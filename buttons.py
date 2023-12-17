from pyrogram.types import InlineKeyboardButton

#Начальные кнопки
start_buttons = [
    [
        InlineKeyboardButton("Выбрать предмет", callback_data="Choose subject")
    ],
    [
        InlineKeyboardButton("Посмотреть рейтинг", callback_data="Get rating")
    ]
]

#Кнопки выбора предмета
choose_sub = [
    [
        InlineKeyboardButton("Информатика", callback_data="Inf")
    ],
    [
        InlineKeyboardButton("Математика", callback_data="Math")
    ],
    [
        InlineKeyboardButton("Русский язык", callback_data="Rus")
    ],
    [
        InlineKeyboardButton("Химия", callback_data="Chem")
    ],
    [
        InlineKeyboardButton("Физика", callback_data="Phys")
    ],
    [
        InlineKeyboardButton("Английский язык", callback_data="Eng")
    ]
]

#Кнопки после выбора предмета
buttons_aft_choose_s = [
    [
        InlineKeyboardButton("Выбрать тему", callback_data="Choose theme")
    ],
    [
        InlineKeyboardButton("Сгенерировать тест по всем темам", callback_data="Generate test all themes")
    ]
]


#Информатика_темы
inf_themes = [
    [
        InlineKeyboardButton("1. Анализ информационных моделей", callback_data="theme_inf_1")
    ],
    [
        InlineKeyboardButton("2. Построение таблиц истинности логических выражений", callback_data="theme_inf_2")
    ],
    [
        InlineKeyboardButton("3. Поиск информации в реляционных базах данных", callback_data="theme_inf_3")
    ],
    [
        InlineKeyboardButton("4. Кодирование и декодирование информации", callback_data="theme_inf_4")
    ],
    [
        InlineKeyboardButton("5. Анализ и построение алгоритмов для исполнителей", callback_data="theme_inf_5")
    ],
    [
        InlineKeyboardButton("6. Определение результатов работы простейших алгоритмов", callback_data="theme_inf_6")
    ],
    [
        InlineKeyboardButton("7. Кодирование и декодирование информации. Передача информации", callback_data="theme_inf_7")
    ],
    [
        InlineKeyboardButton("8. Перебор слов и системы счисления", callback_data="theme_inf_8")
    ],
    [
        InlineKeyboardButton("9. Работа с таблицами", callback_data="theme_inf_9")
    ],
    [
        InlineKeyboardButton("10. Поиск символов в текстовом редакторе", callback_data="theme_inf_10")
    ],
    [
        InlineKeyboardButton("11. Вычисление количества информации", callback_data="theme_inf_11")
    ],
    [
        InlineKeyboardButton("12. Выполнение алгоритмов для исполнителей", callback_data="theme_inf_12")
    ],
    [
        InlineKeyboardButton("13. Организация компьютерных сетей. Адресация", callback_data="theme_inf_13")
    ],
    [
        InlineKeyboardButton("14. Кодирование чисел. Системы счисления", callback_data="theme_inf_14")
    ],
    [
        InlineKeyboardButton("15. Преобразование логических выражений", callback_data="theme_inf_15")
    ],
    [
        InlineKeyboardButton("16. Рекурсивные алгоритмы", callback_data="theme_inf_16")
    ],
    [
        InlineKeyboardButton("17. Обработки числовой последовательности", callback_data="theme_inf_17")
    ],
    [
        InlineKeyboardButton("18. Робот-сборщик монет", callback_data="theme_inf_18")
    ],
    [
        InlineKeyboardButton("19. Выигрышная стратегия. Задание 1", callback_data="theme_inf_19")
    ],
    [
        InlineKeyboardButton("20. Выигрышная стратегия. Задание 2", callback_data="theme_inf_20")
    ],
    [
        InlineKeyboardButton("21. Выигрышная стратегия. Задание 3", callback_data="theme_inf_21")
    ],
    [
        InlineKeyboardButton("22. Многопроцессорные системы", callback_data="theme_inf_22")
    ],
    [
        InlineKeyboardButton("23. Оператор присваивания и ветвления. Перебор вариантов, построение дерева", callback_data="theme_inf_23")
    ],
    [
        InlineKeyboardButton("24. Обработка символьных строк", callback_data="theme_inf_24")
    ],
    [
        InlineKeyboardButton("25. Обработка целочисленной информации", callback_data="theme_inf_25")
    ],
        [
        InlineKeyboardButton("26. Обработка целочисленной информации", callback_data="theme_inf_26")
    ],
    [
        InlineKeyboardButton("27. Программирование", callback_data="theme_inf_27")
    ],
]


quantity_choose_t = [
    [
        InlineKeyboardButton("5", callback_data="5")
    ],
    [
        InlineKeyboardButton("10", callback_data="10")
    ],
    [
        InlineKeyboardButton("15", callback_data="15")
    ],
    [
        InlineKeyboardButton("Ввести свое количество", callback_data="own quantity")
    ]
]


buttons_aft_choose_t = [
    [
        InlineKeyboardButton("Сгенерировать тест по теме")
    ]
]