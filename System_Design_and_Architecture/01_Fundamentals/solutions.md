# Module 01: Fundamentals - Solutions

Detailed solutions with explanations for all exercises.

---

## Exercise 1: Design a Simple Blog API

### A) REST API Endpoints

```
Create a post:    POST   /api/posts
List all posts:   GET    /api/posts
Get single post:  GET    /api/posts/{id}
Update a post:    PUT    /api/posts/{id}
Delete a post:    DELETE /api/posts/{id}
```

**Why these URLs?**
- `/api/posts` represents the posts resource collection
- `/{id}` identifies a specific post
- HTTP methods indicate the action (POST=create, GET=read, PUT=update, DELETE=delete)

### B) Create Post Request/Response

```http
POST /api/posts
Authorization: Bearer token123
Content-Type: application/json

{
  "title": "My First Blog Post",
  "content": "This is the content of my post...",
  "tags": ["tutorial", "beginner"]
}

Response:
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/posts/1

{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of my post...",
  "author_id": 123,
  "author_name": "Alice",
  "tags": ["tutorial", "beginner"],
  "created_at": "2024-01-15T10:00:00Z",
  "updated_at": "2024-01-15T10:00:00Z",
  "views": 0,
  "likes": 0
}
```

**Key Points:**
- Use 201 Created status for successful resource creation
- Include Location header with new resource URL
- Return the complete created object with server-generated fields (id, timestamps)
- Don't require client to send author info (get from auth token)

### C) Database Schema

```
Table: posts
+------------+--------------+------+
| Column     | Type         | Note |
+------------+--------------+------+
| id         | INT          | Primary key, auto-increment
| title      | VARCHAR(200) | Required, indexed
| content    | TEXT         | Required
| author_id  | INT          | Foreign key to users table
| created_at | TIMESTAMP    | Auto-set on creation
| updated_at | TIMESTAMP    | Auto-update on modification
| views      | INT          | Default 0
| likes      | INT          | Default 0
+------------+--------------+------+

Table: post_tags
+------------+--------------+
| post_id    | INT          | Foreign key to posts
| tag        | VARCHAR(50)  |
+------------+--------------+
(Composite primary key: post_id + tag)
```

---

## Exercise 2: HTTP Status Codes

**A)** User successfully creates a new account: **201**
- 201 Created = New resource was successfully created

**B)** User tries to access a page that doesn't exist: **404**
- 404 Not Found = Requested resource doesn't exist

**C)** User successfully retrieves their profile: **200**
- 200 OK = Request succeeded

**D)** User sends invalid data (missing required field): **400**
- 400 Bad Request = Client sent malformed/invalid data

**E)** User tries to access admin page without login: **401**
- 401 Unauthorized = Authentication required

**F)** Database connection fails on the server: **500**
- 500 Internal Server Error = Server-side error

### Status Code Categories:
- **2xx** = Success (200 OK, 201 Created, 204 No Content)
- **3xx** = Redirection (301 Permanent, 302 Temporary, 304 Not Modified)
- **4xx** = Client Error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)
- **5xx** = Server Error (500 Internal Server Error, 503 Service Unavailable)

---

## Exercise 3: Design URL Structure

**A)** Get all users:
```
URL: GET /api/users
```

**B)** Get user with ID 42:
```
URL: GET /api/users/42
```

**C)** Get all posts written by user 42:
```
URL: GET /api/users/42/posts
```
Alternative: `GET /api/posts?author_id=42`

**D)** Get post 789 written by user 42:
```
URL: GET /api/users/42/posts/789
```
Alternative: `GET /api/posts/789` (simpler, preferred)

**E)** Get comments on post 789:
```
URL: GET /api/posts/789/comments
```

**RESTful URL Best Practices:**
1. Use nouns, not verbs (posts, not getPosts)
2. Use plural for collections (/users, not /user)
3. Nested resources show relationships
4. Keep it simple and predictable
5. Use query params for filtering/sorting

---

## Exercise 4: DNS Resolution

Correct order:

```
1. Browser checks its DNS cache
2. ISP DNS server is queried
3. ISP queries root DNS server
4. Root DNS server responds with .com TLD server
5. TLD server responds with authoritative name server
6. Authoritative DNS server returns IP address
7. Browser connects to the IP address
```

**Detailed Flow:**
```
www.example.com
       ↓
1. Browser cache (already know IP?) → If yes, done!
       ↓ (cache miss)
2. OS cache check
       ↓ (cache miss)
3. Router cache check
       ↓ (cache miss)
4. ISP DNS Resolver
       ↓
5. Root DNS Server: "Ask .com TLD server at IP X"
       ↓
6. TLD Server (.com): "Ask example.com's nameserver at IP Y"
       ↓
7. Authoritative Server: "example.com is at IP 93.184.216.34"
       ↓
8. Result cached at multiple levels
       ↓
9. Browser connects to 93.184.216.34
```

**Why caching matters:**
- Reduces latency (faster page loads)
- Reduces load on DNS servers
- Typical cache TTL: 5 minutes to 24 hours

---

## Exercise 5: Client-Server Interaction

1. User types URL in browser
2. Browser performs **DNS** lookup to get IP address
3. Browser sends **HTTP** request to server
4. Server processes request and queries **database**
5. Server sends **HTTP** response with HTML
6. Browser **renders/parses** the HTML and displays page

**Complete Flow Diagram:**
```
User → Browser → DNS → Server → Database
                         ↓
                    Processing
                         ↓
       ← HTML ← Response ←
       ↓
   Rendering
       ↓
   Display
```

---

## Exercise 6: Design a Weather API

### A) API Endpoints

```
Current weather:  GET /api/weather/current?city={city}&units={c|f}
7-day forecast:   GET /api/weather/forecast?city={city}&units={c|f}&days=7
```

Alternative designs:
```
GET /api/weather/{city}/current
GET /api/weather/{city}/forecast
```

### B) Current Weather Response

```json
{
  "city": "London",
  "country": "UK",
  "coordinates": {
    "latitude": 51.5074,
    "longitude": -0.1278
  },
  "current": {
    "temperature": 15,
    "feels_like": 13,
    "humidity": 72,
    "pressure": 1013,
    "wind_speed": 5.5,
    "wind_direction": "SW",
    "conditions": "Partly Cloudy",
    "icon": "partly-cloudy",
    "visibility": 10,
    "uv_index": 3
  },
  "units": {
    "temperature": "celsius",
    "wind_speed": "m/s"
  },
  "timestamp": "2024-01-15T10:00:00Z",
  "sunrise": "07:45:00",
  "sunset": "16:30:00"
}
```

### C) Temperature Unit Options

**Option 1**: Query parameter
```
/api/weather?city=London&units=celsius
/api/weather?city=London&units=fahrenheit
```
✅ Clear and explicit  
✅ Easy to change per request

**Option 2**: Header
```
GET /api/weather?city=London
Accept-Units: celsius
```
✅ RESTful approach  
❌ Less discoverable

**Option 3**: Separate endpoints
```
/api/weather/celsius?city=London
/api/weather/fahrenheit?city=London
```
❌ Not recommended (duplicates endpoints)

**Recommended**: Option 1 (query parameter)

---

## Exercise 7: Authentication Design

### A) Registration Endpoint

```http
POST /api/auth/register
Content-Type: application/json

{
  "email": "alice@example.com",
  "password": "SecurePass123!",
  "name": "Alice",
  "phone": "+1234567890" (optional)
}

Response:
HTTP/1.1 201 Created
Content-Type: application/json

{
  "user": {
    "id": 123,
    "email": "alice@example.com",
    "name": "Alice",
    "created_at": "2024-01-15T10:00:00Z"
  },
  "message": "Registration successful. Please verify your email."
}
```

**Security Notes:**
- Never return password in response
- Password should be hashed before storage (bcrypt, argon2)
- Consider email verification
- Validate email format and password strength

### B) Login Endpoint

```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "alice@example.com",
  "password": "SecurePass123!"
}

Response:
HTTP/1.1 200 OK
Content-Type: application/json

{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJleHAiOjE2MzY5ODAwMDB9.abc123",
  "token_type": "Bearer",
  "expires_in": 3600,
  "expires_at": "2024-01-15T11:00:00Z",
  "user": {
    "id": 123,
    "email": "alice@example.com",
    "name": "Alice"
  }
}
```

**Security Notes:**
- Use HTTPS only
- Implement rate limiting (prevent brute force)
- Return same error message for invalid email/password (prevent user enumeration)
- Use secure token generation (JWT, OAuth)

### C) Protected Endpoint Authentication

```http
GET /api/profile
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Implementation:**
1. Extract token from Authorization header
2. Verify token signature
3. Check token expiration
4. Extract user ID from token payload
5. Proceed with request or return 401 Unauthorized

---

## Exercise 8: Error Response Design

### A) User Not Found

```json
{
  "status": 404,
  "error": "Not Found",
  "message": "User with ID 999 does not exist",
  "timestamp": "2024-01-15T10:00:00Z",
  "path": "/api/users/999"
}
```

### B) Invalid Email Format

```json
{
  "status": 400,
  "error": "Bad Request",
  "message": "Invalid email format",
  "field": "email",
  "value": "not-an-email",
  "timestamp": "2024-01-15T10:00:00Z",
  "path": "/api/auth/register"
}
```

### C) Server Database Error

```json
{
  "status": 500,
  "error": "Internal Server Error",
  "message": "An unexpected error occurred. Please try again later.",
  "error_id": "err_abc123",
  "timestamp": "2024-01-15T10:00:00Z"
}
```

**Best Practices:**
- Consistent error format across all endpoints
- Include helpful error messages
- Don't expose internal details in production (security)
- Log detailed errors server-side
- Provide error_id for support reference
- Use appropriate status codes

---

## Exercise 9: Pagination Design

### A) URL with Pagination

```
GET /api/posts?page=1&limit=20
```

Alternative patterns:
```
GET /api/posts?offset=0&limit=20
GET /api/posts?page=1&per_page=20
```

### B) Response Structure

```json
{
  "posts": [
    {
      "id": 1,
      "title": "First Post",
      "content": "..."
    }
    // ... more posts
  ],
  "pagination": {
    "current_page": 1,
    "per_page": 20,
    "total_items": 1000,
    "total_pages": 50,
    "has_next": true,
    "has_previous": false,
    "next_page": 2,
    "previous_page": null
  },
  "links": {
    "first": "/api/posts?page=1&limit=20",
    "last": "/api/posts?page=50&limit=20",
    "next": "/api/posts?page=2&limit=20",
    "previous": null
  }
}
```

### C) Page 3 Calculation

```
URL: GET /api/posts?page=3&limit=20
Shows posts: 41 to 60

Calculation:
- Offset = (page - 1) × limit = (3 - 1) × 20 = 40
- First item: offset + 1 = 41
- Last item: offset + limit = 60
```

---

## Exercise 10: TODO List API

### A) Endpoints

```
Create task:     POST   /api/tasks
List tasks:      GET    /api/tasks?status={all|complete|incomplete}
Get single task: GET    /api/tasks/{id}
Update task:     PUT    /api/tasks/{id}
Delete task:     DELETE /api/tasks/{id}
```

### B) Database Schema

```
Table: tasks
+-------------+--------------+------+
| Column      | Type         | Note |
+-------------+--------------+------+
| id          | INT          | Primary key, auto-increment
| user_id     | INT          | Foreign key to users
| title       | VARCHAR(200) | Required
| description | TEXT         | Optional
| completed   | BOOLEAN      | Default false
| priority    | ENUM         | low, medium, high
| due_date    | DATE         | Optional
| created_at  | TIMESTAMP    | Auto-set
| updated_at  | TIMESTAMP    | Auto-update
+-------------+--------------+------+
```

### C) Create Task Request

```http
POST /api/tasks
Authorization: Bearer token123
Content-Type: application/json

{
  "title": "Learn System Design",
  "description": "Complete Module 01 exercises",
  "priority": "high",
  "due_date": "2024-01-20"
}

Response:
HTTP/1.1 201 Created

{
  "id": 1,
  "user_id": 123,
  "title": "Learn System Design",
  "description": "Complete Module 01 exercises",
  "completed": false,
  "priority": "high",
  "due_date": "2024-01-20",
  "created_at": "2024-01-15T10:00:00Z",
  "updated_at": "2024-01-15T10:00:00Z"
}
```

### D) List Tasks with Filter

```http
GET /api/tasks?status=incomplete
Authorization: Bearer token123

Response:
{
  "tasks": [
    {
      "id": 1,
      "title": "Learn System Design",
      "description": "Complete Module 01 exercises",
      "completed": false,
      "priority": "high",
      "due_date": "2024-01-20",
      "created_at": "2024-01-15T10:00:00Z"
    },
    {
      "id": 3,
      "title": "Buy groceries",
      "description": null,
      "completed": false,
      "priority": "medium",
      "due_date": "2024-01-16",
      "created_at": "2024-01-15T09:00:00Z"
    }
  ],
  "count": 2,
  "filter": "incomplete"
}
```

---

## Key Takeaways

1. **RESTful Design**: Use standard HTTP methods and resource-based URLs
2. **Consistency**: Same patterns for similar operations
3. **Security**: Always authenticate, never expose sensitive data
4. **Error Handling**: Clear, helpful error messages
5. **Pagination**: Essential for large datasets
6. **Documentation**: Clear API structure helps developers

## Next Steps

Move on to **Module 02: Scalability Basics** to learn how systems grow!
