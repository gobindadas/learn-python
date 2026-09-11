# Module 01: Fundamentals - Real-World Examples

Learn from real systems and practical implementations!

---

## Example 1: Simple URL Shortener (Like bit.ly)

### Problem
Design a basic URL shortening service that converts long URLs to short ones.

### System Architecture

```
┌─────────┐      ┌────────────┐      ┌──────────┐
│ Browser │─────▶│ Web Server │─────▶│ Database │
└─────────┘      └────────────┘      └──────────┘
    │                   │
    │  1. POST long URL │
    │──────────────────▶│
    │                   │
    │  2. Generate short│
    │     code (abc123) │
    │                   │
    │  3. Return short  │
    │     URL           │
    │◀──────────────────│
    │                   │
    │  4. GET /abc123   │
    │──────────────────▶│
    │                   │
    │  5. Redirect to   │
    │     original URL  │
    │◀──────────────────│
```

### API Design

**Create Short URL:**
```http
POST /api/shorten
Content-Type: application/json

{
  "url": "https://www.example.com/very/long/url/that/needs/shortening"
}

Response:
{
  "short_code": "abc123",
  "short_url": "https://short.ly/abc123",
  "original_url": "https://www.example.com/very/long/url/that/needs/shortening"
}
```

**Use Short URL:**
```http
GET /abc123

Response:
HTTP/1.1 301 Moved Permanently
Location: https://www.example.com/very/long/url/that/needs/shortening
```

### Database Schema

```
Table: urls
+------------+---------------+
| short_code | original_url  |
+------------+---------------+
| abc123     | https://...   |
| xyz789     | https://...   |
+------------+---------------+
```

### How It Works

1. **User submits long URL** via POST request
2. **Server generates unique code** (abc123)
3. **Store mapping** in database: abc123 → long URL
4. **Return short URL** to user
5. **When someone visits** short URL, look up code in database
6. **Redirect** to original URL

---

## Example 2: Social Media Post Feed (Like Twitter)

### Problem
Display a user's feed showing posts from people they follow.

### System Architecture

```
┌─────────┐     ┌─────────────┐     ┌──────────┐
│ Mobile  │────▶│ API Gateway │────▶│   Auth   │
│   App   │     └─────────────┘     │ Service  │
└─────────┘            │             └──────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Feed Service   │
              └─────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
    ┌────────┐   ┌─────────┐   ┌────────┐
    │ User   │   │  Post   │   │ Cache  │
    │   DB   │   │   DB    │   │ Redis  │
    └────────┘   └─────────┘   └────────┘
```

### API Design

**Get User Feed:**
```http
GET /api/feed?user_id=123&limit=20&offset=0
Authorization: Bearer token123

Response:
{
  "posts": [
    {
      "id": 1001,
      "author": {
        "id": 456,
        "username": "alice",
        "avatar": "https://..."
      },
      "content": "Just learned system design!",
      "created_at": "2024-01-15T10:30:00Z",
      "likes": 42,
      "comments": 5
    },
    {
      "id": 1002,
      "author": {
        "id": 789,
        "username": "bob",
        "avatar": "https://..."
      },
      "content": "Building my first API",
      "created_at": "2024-01-15T09:15:00Z",
      "likes": 15,
      "comments": 2
    }
  ],
  "next_offset": 20
}
```

**Create Post:**
```http
POST /api/posts
Authorization: Bearer token123
Content-Type: application/json

{
  "content": "Hello, World!",
  "media_urls": ["https://..."]
}

Response:
{
  "id": 1003,
  "author_id": 123,
  "content": "Hello, World!",
  "created_at": "2024-01-15T11:00:00Z",
  "status": "published"
}
```

### Database Schema

```
Table: users
+----+----------+
| id | username |
+----+----------+
| 1  | alice    |
| 2  | bob      |
+----+----------+

Table: posts
+----+-----------+-----------+------------+
| id | author_id | content   | created_at |
+----+-----------+-----------+------------+
| 1  | 1         | Hello...  | 2024-...   |
| 2  | 2         | World...  | 2024-...   |
+----+-----------+-----------+------------+

Table: follows
+-------------+-------------+
| follower_id | followee_id |
+-------------+-------------+
| 1           | 2           |
| 1           | 3           |
+-------------+-------------+
```

### Feed Generation Logic

```sql
-- Get posts from users that user 123 follows
SELECT posts.*
FROM posts
JOIN follows ON posts.author_id = follows.followee_id
WHERE follows.follower_id = 123
ORDER BY posts.created_at DESC
LIMIT 20;
```

---

## Example 3: E-Commerce Product API

### Problem
Design an API for browsing and purchasing products.

### API Endpoints

**Browse Products:**
```http
GET /api/products?category=electronics&sort=price&order=asc&page=1&limit=20

Response:
{
  "products": [
    {
      "id": 101,
      "name": "Wireless Headphones",
      "description": "High-quality audio...",
      "price": 99.99,
      "currency": "USD",
      "stock": 150,
      "category": "electronics",
      "images": [
        "https://cdn.example.com/headphones-1.jpg",
        "https://cdn.example.com/headphones-2.jpg"
      ],
      "rating": 4.5,
      "reviews_count": 234
    }
  ],
  "total": 500,
  "page": 1,
  "total_pages": 25
}
```

**Add to Cart:**
```http
POST /api/cart/items
Authorization: Bearer token123

{
  "product_id": 101,
  "quantity": 2
}

Response:
{
  "cart_id": "cart_abc123",
  "items": [
    {
      "product_id": 101,
      "name": "Wireless Headphones",
      "quantity": 2,
      "unit_price": 99.99,
      "subtotal": 199.98
    }
  ],
  "total": 199.98
}
```

**Checkout:**
```http
POST /api/orders
Authorization: Bearer token123

{
  "cart_id": "cart_abc123",
  "shipping_address": {
    "street": "123 Main St",
    "city": "New York",
    "zip": "10001"
  },
  "payment_method": {
    "type": "credit_card",
    "token": "card_token_xyz"
  }
}

Response:
{
  "order_id": "order_789",
  "status": "confirmed",
  "total": 199.98,
  "estimated_delivery": "2024-01-20"
}
```

---

## Example 4: User Authentication Flow

### Problem
Implement secure user login and authorization.

### Authentication Flow

```
┌──────────┐                              ┌──────────┐
│  Client  │                              │  Server  │
└──────────┘                              └──────────┘
     │                                          │
     │  1. POST /api/auth/login                │
     │     { email, password }                 │
     │─────────────────────────────────────────▶│
     │                                          │
     │                                     2. Verify
     │                                     credentials
     │                                          │
     │  3. Return JWT token                    │
     │◀─────────────────────────────────────────│
     │     { token: "eyJ..." }                 │
     │                                          │
     │  4. Store token locally                 │
     │                                          │
     │  5. GET /api/profile                    │
     │     Authorization: Bearer eyJ...        │
     │─────────────────────────────────────────▶│
     │                                          │
     │                                     6. Verify
     │                                     token
     │                                          │
     │  7. Return user data                    │
     │◀─────────────────────────────────────────│
```

### API Design

**Register:**
```http
POST /api/auth/register

{
  "email": "alice@example.com",
  "password": "SecurePass123!",
  "name": "Alice"
}

Response:
{
  "user_id": 123,
  "email": "alice@example.com",
  "name": "Alice"
}
```

**Login:**
```http
POST /api/auth/login

{
  "email": "alice@example.com",
  "password": "SecurePass123!"
}

Response:
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_at": "2024-01-16T10:00:00Z",
  "user": {
    "id": 123,
    "email": "alice@example.com",
    "name": "Alice"
  }
}
```

**Access Protected Resource:**
```http
GET /api/profile
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

Response:
{
  "id": 123,
  "email": "alice@example.com",
  "name": "Alice",
  "created_at": "2024-01-01T00:00:00Z"
}
```

---

## Example 5: File Upload Service

### Problem
Allow users to upload and retrieve files (images, documents).

### Upload Flow

```
┌──────────┐              ┌──────────┐              ┌──────────┐
│  Client  │              │  Server  │              │ Storage  │
└──────────┘              └──────────┘              └──────────┘
     │                          │                          │
     │  1. POST /upload         │                          │
     │     (file data)          │                          │
     │─────────────────────────▶│                          │
     │                          │                          │
     │                          │  2. Save to storage      │
     │                          │─────────────────────────▶│
     │                          │                          │
     │                          │  3. Return file path     │
     │                          │◀─────────────────────────│
     │                          │                          │
     │  4. Return file URL      │                          │
     │◀─────────────────────────│                          │
     │                          │                          │
     │  5. GET /files/abc123    │                          │
     │─────────────────────────▶│                          │
     │                          │                          │
     │                          │  6. Fetch file           │
     │                          │─────────────────────────▶│
     │                          │                          │
     │  7. Return file data     │                          │
     │◀─────────────────────────│                          │
```

### API Design

**Upload File:**
```http
POST /api/files/upload
Authorization: Bearer token123
Content-Type: multipart/form-data

file: [binary data]
metadata: {
  "filename": "document.pdf",
  "description": "Important document"
}

Response:
{
  "file_id": "abc123",
  "url": "https://storage.example.com/files/abc123",
  "filename": "document.pdf",
  "size": 1048576,
  "uploaded_at": "2024-01-15T10:00:00Z"
}
```

**Download File:**
```http
GET /api/files/abc123

Response:
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Disposition: attachment; filename="document.pdf"
Content-Length: 1048576

[binary file data]
```

---

## Key Patterns Demonstrated

1. **REST Principles**: Resource-based URLs, appropriate HTTP methods
2. **Authentication**: Token-based auth with JWT
3. **Pagination**: Using limit/offset for large datasets
4. **Status Codes**: Proper use of 200, 201, 401, 404, etc.
5. **Data Format**: Consistent JSON structure
6. **Error Handling**: Clear error messages

## Practice Exercise

Try designing APIs for these scenarios:
1. Weather API (get current weather for a city)
2. Task Management (create, list, update, delete tasks)
3. Messaging API (send and receive messages)

Next, check out **exercises.md** for hands-on practice!
