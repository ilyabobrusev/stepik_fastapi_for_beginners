```text
Класс HTTPException принимает три аргумента:

    status_code: Код состояния, который будет возвращен для этого сбоя
    detail: Сопроводительное сообщение для отправки клиенту
    headers: Необязательный параметр для ответов, требующих заголовков
```

```test
Вы также можете использовать библиотеку from starlette import status.
В этом случае код 404 ошибки будет выглядеть следующим образом:
status_code=status.HTTP_404_NOT_FOUND

FastAPI предоставляет тот же starlette.status под псевдонимом fastapi.status для удобства разработчика.
Но его источник - это непосредственно Starlette.
```