# Projects - Interview Answers

## Level: Normal (1-5)

### Answer 1: Project Structure
```
myproject/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils.py
├── docs/
│   └── README.md
├── .gitignore
├── .env.example
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

### Answer 2: Virtual Environments
```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Deactivate
deactivate
```

### Answer 3: Requirements Management
```python
# requirements.txt - production dependencies
requests==2.28.0
flask==2.3.0

# requirements-dev.txt - development dependencies
-r requirements.txt
pytest==7.4.0
black==23.3.0
mypy==1.4.0

# setup.py or pyproject.toml - package dependencies
install_requires = [
    'requests>=2.28.0',
    'flask>=2.3.0',
]
```

### Answer 4: Configuration Management
```python
import os
from dataclasses import dataclass

@dataclass
class Config:
    ENV: str = os.getenv('ENVIRONMENT', 'development')
    DEBUG: bool = os.getenv('DEBUG', 'True') == 'True'
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    
    @classmethod
    def load(cls):
        if cls.ENV == 'production':
            return ProductionConfig()
        return DevelopmentConfig()

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
```

### Answer 5: Logging Setup
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger('myapp')
    logger.setLevel(logging.DEBUG)
    
    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        'app.log',
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console)
    logger.addHandler(file_handler)
    
    return logger
```

## Level: Medium (6-10)

### Answer 6: CLI Application
```python
import click

@click.group()
def cli():
    """My CLI application"""
    pass

@cli.command()
@click.option('--name', default='World', help='Name to greet')
@click.option('--count', default=1, help='Number of greetings')
def greet(name, count):
    """Greet someone"""
    for _ in range(count):
        click.echo(f'Hello, {name}!')

@cli.command()
@click.argument('filename')
def process(filename):
    """Process a file"""
    with open(filename) as f:
        click.echo(f.read())

if __name__ == '__main__':
    cli()
```

### Answer 7: REST API
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = {}

@app.post("/items/")
async def create_item(item: Item):
    items[item.name] = item
    return item

@app.get("/items/{name}")
async def get_item(name: str):
    if name not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[name]

@app.get("/items/")
async def list_items():
    return list(items.values())
```

### Answer 9: Testing Strategy
```python
import pytest
from unittest.mock import Mock, patch

# Unit test
def test_add():
    assert add(2, 3) == 5

# Integration test
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_endpoint(client):
    response = client.get('/api/items')
    assert response.status_code == 200

# Mocking
@patch('requests.get')
def test_api_call(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'data': 'test'}
    result = fetch_data()
    assert result == {'data': 'test'}
```

## Level: Hard (11-15)

### Answer 13: Security Best Practices
```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import secrets

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# SQL injection prevention (use parameterized queries)
def safe_query(user_id: int):
    # GOOD - parameterized
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    
    # BAD - SQL injection vulnerable
    # cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# Input validation
from pydantic import BaseModel, validator

class User(BaseModel):
    username: str
    email: str
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
```

### Answer 15: Production Deployment
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 3s
      retries: 3
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```
