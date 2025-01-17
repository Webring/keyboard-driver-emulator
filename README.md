# Эмулятор драйвера клавиатуры

Этот проект представляет собой эмулятор драйвера для клавиатуры. Программа включает в себя текстовое поле и набор
кнопок, которые можно переназначать внутри этого текстового поля.

## Сборка проекта

Для создания исполняемого файла необходимо выполнить скрипт `build.bat`.

## Настройка темы

Вы можете добавить тему для программы. Для этого необходимо разместить файл `style.qss` в одном каталоге с исполняемым
файлом.

## Файлы конфигурации

Для корректной работы программы необходимы два файла:

1. **Файл размещения клавиш** (.kplc)
2. **Файл раскладки клавиатуры** (.klay)

При запуске программа будет искать файл `base_placement.kplc` в корневом каталоге.

## Зависимости

В проекте использовался python3.12. Все зависимости перечислены в файле `requirements.txt`. Для их установки выполните
следующую команду:

```bash
pip install -r requirements.txt
```



## Структура .kplc файла
Этот конфигурационный файл представлен в формате JSON и содержит двумерный массив, где каждая вложенная структура описывает клавишу и её размер на экране.

Каждый элемент массива представляет собой массив, содержащий два значения:

1. **Scancode клавиши**: Числовое значение, которое представляет собой уникальный идентификатор клавиши на клавиатуре. Значение `null` означает, что вместо кнопки будет размещен разделитель указанного размера.
2. **Размер клавиши на экране**: Числовое значение, которое указывает на размер клавиши. Например, `1` - это стандартный размер, `0.5` - клавиша в половину стандартного размера.

### Пример:

```json
[
  [
    [1,    1],
    [null, 0.5],
    [59,   1]
  ]
]
```

## Структура .klay файла

Этот конфигурационный файл представлен в формате JSON и содержит информацию о клавишах. Каждая клавиша описывается объектом, где ключ - это `scancode`, а значение - объект с информацией о клавише.


Каждый объект клавиши содержит следующие поля:

1. **name**: Строковое значение, представляющее имя клавиши .
2. **keycode**: Числовое значение, представляющее `keycode` клавиши.
3. **modifier**: Числовое значение, представляющее модификатор клавиши (0 - отсутствие модификаторов, модификаторы аналогичны модификаторам из Qt).
4. **text_function**: Строка, содержащая код на python, который определяет, то какой текст будет вставлен (значение храниться в переменной `value`, также есть общая для всех клавиш переменная - `extra`, по умолчанию это словарь).

### Пример

```json
{
    "16": {
        "name": "q",
        "keycode": 81,
        "modifier": 0,
        "text_function": "value='Q' if shift_pressed else 'q'"
    }
}
```

