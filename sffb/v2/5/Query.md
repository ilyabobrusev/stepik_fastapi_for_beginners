```
Query

Для работы с параметрами строки запроса фреймворк предоставляет класс Query из пакета fastapi, который используется для определения параметров запроса. Параметры запроса передаются в URL-адресе после знака вопроса (?), например:  /items?item_id=123.

Общие метаданные:
    title: Описание параметра, отображаемое в документации.
    description: Более подробное описание параметра.
    examples: Пример значения параметра.
    include_in_schema: Параметр позволяет исключить операцию пути из сгенерированной схемы OpenAPI

Специфичные правила валидации:

    min_length: Минимальная длина строки для параметра.
    max_length:  Максимальная длина строки для параметра.
    pattern: Устанавливает регулярное выражение, которому должно соответствовать значение параметра
    lt: Значение должно быть меньше указанного.
    le: Значение должно быть меньше или равно указанному.
    gt: Значение должно быть больше указанного.
    ge:Значение должно быть больше или равно указанному.
```