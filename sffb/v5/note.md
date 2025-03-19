```text
APIRouter(*, prefix='', tags=None, dependencies=None, default_response_class=Default(JSONResponse), responses=None, callbacks=None, routes=None, redirect_slashes=True, default=None, dependency_overrides_provider=None, route_class=APIRoute, on_startup=None, on_shutdown=None, lifespan=None, deprecated=None, include_in_schema=True, generate_unique_id_function=Default(generate_unique_id))
```

```text
engine = create_engine('postgresql+psycopg2://youuser:youpassword@localhost/youdb')
Dialect+driver://username:password@host:port/database
```

```text
SQLite3

Драйверы:

    pysqlite 

    aiosqlite

База данных в памяти не хранится на диске (полезно для тестов):

DATABASE = 'sqlite:///'
DATABASE = 'sqlite:///:memory:'
DATABASE = 'sqlite+pysqlite:///:memory:'

Файловое соединение с использованием относительного пути (3 косые черты):

DATABASE = 'sqlite:///myfile.db'
DATABASE = 'sqlite+pysqlite:///myfile.db'

Подключение файлов по абсолютному пути (обратите внимание на 4 косые черты для unix, и обратная косая черта для Windows):

DATABASE = 'sqlite:////path/to/myfile.db'
DATABASE = 'sqlite:///C:\\path\\to\\myfile.db'

Современные версии SQLite поддерживают альтернативную систему подключения с использованием URI уровня драйвера, которая имеет то преимущество, что могут быть переданы дополнительные аргументы на уровне драйвера, включая такие опции, как "только для чтения". 'URI' уровня SQLite хранится как часть "базы данных" URL-адреса SQLAlchemy (то есть после косой черты):

DATABASE = 'sqlite:///file:path/to/myfile.db?uri=true&mode=ro'
DATABASE = 'sqlite:///file:path/to/myfile.db?uri=true&mode=ro&check_same_thread=true&timeout=10&nolock=1'

Aiosqlite:

DATABASE = 'sqlite+aiosqlite:///myfile.db'

Асинхронные соединения требуютcreate_async_engine

 
PostgreSQL

Драйверы:

    psycopg2 (основной драйвер)

    pg8000

    psycopg

    asyncpg

    psycopg2cffi

Драйвер по умолчанию:

DATABASE = 'postgresql://myusername:mypassword@myhost:5432/mydatabase'

Psycopg2 с использованием TCP/IP:

DATABASE = 'postgresql+psycopg2://myusername:mypassword@myhost:5432/mydatabase'
DATABASE = 'postgresql+psycopg2://myusername:mypassword@myhost:5432/mydatabase?sslmode=require'

Psycopg2 с использованием сокета Unix:

DATABASE = 'postgresql+psycopg2://myusername:mypassword@/mydatabase'  # По умолчанию сокет в /tmp
DATABASE = 'postgresql+psycopg2://myusername:mypassword@/mydatabase?host=/var/lib/postgresql' # Укажем местоположение сокета
DATABASE = 'postgresql+psycopg2://myusername:mypassword@/mydatabase?host=HostA:port1&host=HostB&host=HostC'  # Резервные хосты

Драйвер Psycopg:

DATABASE = 'postgresql+psycopg://myusername:mypassword@myhost:5432/mydatabase'

Драйвер pg8000:

DATABASE = 'postgresql+pg8000://myusername:mypassword@myhost:5432/mydatabase'

Асинхронный PostgreSQL:

DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase'
DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase?async_fallback=true'
DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase?prepared_statement_cache_size=500'
DATABASE = 'postgresql+asyncpg://myusername:mypassword@myhost:5432/mydatabase?prepared_statement_cache_size=0'

Асинхронные соединения требуютcreate_async_engine

Psycopg2cffi (реализуется с слоем cffi для портативности):

DATABASE = 'postgresql+psycopg2cffi://myusername:mypasswordword@myhost:5432/mydatabase'
```