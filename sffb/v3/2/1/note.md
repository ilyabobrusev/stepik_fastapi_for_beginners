```text
from pydantic import BaseModel


class Message(BaseModel):
    id: int
    text: str
```

```text
class Message(BaseModel):
    id: int
    description: str | None = None
    text: str = "Simple text"
```

```text
class Message(BaseModel):
    id: int
    description: str | None = Field(default=None, description="The description of the message", max_length=300)
    text: str = "Simple text"
```

```text
class Message(BaseModel):
    id: int
    description: str | None = Field(..., description="The description of the message", max_length=300)
    text: str = "Simple text"
```

```text
created: datetime = Field(default_factory=datetime.now)
```


```text
class Item(BaseModel):
    description: str | None = None
    text: str = "Simple text"


class Message(BaseModel):
    id: int
    item: Item
```

```text
В дополнение к стандартным типам данных Python, библиотека Pydantic определяет свои собственные типы:

    HttpUrl: Это поле, по сути, является строкой со встроенной проверкой для URL. Тип HttpUrl принимает как HTTP, так и HTTPS схемы. Он требует указания TLD (домена верхнего уровня) и хоста, максимальная длина 2083 символа.
    AnyUrl позволяет использовать любую схему (TLD не требуется, но хост обязателен).
    FileUrl предназначено для хранения URL-адреса файла и не требует указания хоста.
    EmailStr: Это такая же строка, но которая должна быть действительным адресом электронной почты. Для проверки правильности представления электронной почты в виде строки требует установки модуля email-validator.
    SecretStr: Этот тип данных используется в основном для хранения паролей или любой другой конфиденциальной информации, которая не должна появляться в логах или другом отслеживании. При преобразовании в JSON он будет отформатирован как '**********'.
```
