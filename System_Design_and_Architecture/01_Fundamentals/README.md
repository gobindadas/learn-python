# Module 01: Fundamentals of System Design

Welcome to system design! Let's start with the building blocks that power every modern application.

## What is System Design?

System design is like being an architect for software. Just as a building architect decides where to place rooms, doors, and utilities, a system designer decides how different parts of a software system work together.

### Real-World Analogy
Think of a restaurant:
- **Kitchen** = Server/Backend (where processing happens)
- **Waiters** = APIs (communicate between kitchen and customers)
- **Menu** = Interface (what customers see)
- **Storage** = Database (where recipes/data are stored)
- **Manager** = Load Balancer (distributes work among waiters)

## Topic 1: Client-Server Architecture

The foundation of almost all web applications!

### What is it?

```
┌──────────┐         Request          ┌──────────┐
│          │ ───────────────────────▶ │          │
│  Client  │                          │  Server  │
│ (Browser)│ ◀─────────────────────── │          │
└──────────┘        Response          └──────────┘
```

- **Client**: The device/application making requests (your web browser, mobile app)
- **Server**: The computer that processes requests and sends responses

### How It Works

1. **Client makes a request**: "Show me cat videos"
2. **Request travels over network**: Through internet cables/WiFi
3. **Server processes request**: Finds cat videos in database
4. **Server sends response**: Returns video data
5. **Client displays result**: You watch cat videos!

### Example: Loading a Webpage

```
You type: www.example.com
   ↓
Browser (Client) sends: "GET /home.html"
   ↓
Web Server receives request
   ↓
Server fetches home.html from storage
   ↓
Server sends back: HTML, CSS, JavaScript
   ↓
Browser displays the webpage
```

## Topic 2: Understanding HTTP

HTTP (HyperText Transfer Protocol) is how clients and servers communicate.

### HTTP Methods

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve data | Get user profile |
| POST | Create new data | Submit a form, create account |
| PUT | Update existing data | Update user settings |
| DELETE | Remove data | Delete a post |
| PATCH | Partial update | Update just the email |

### HTTP Request Structure

```
GET /api/users/123 HTTP/1.1
Host: api.example.com
Authorization: Bearer token123
Content-Type: application/json

{
  "include": "profile,posts"
}
```

Components:
- **Method**: GET
- **Path**: /api/users/123
- **Headers**: Metadata about the request
- **Body**: Data sent with request (for POST/PUT)

### HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=3600

{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com"
}
```

Components:
- **Status Code**: 200 (success), 404 (not found), 500 (server error)
- **Headers**: Metadata about the response
- **Body**: The actual data

### Common HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | OK | Request successful |
| 201 | Created | New resource created |
| 400 | Bad Request | Invalid data sent |
| 401 | Unauthorized | Need to login |
| 403 | Forbidden | Don't have permission |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Something broke on server |
| 503 | Service Unavailable | Server is down |

## Topic 3: DNS (Domain Name System)

DNS is like the internet's phonebook - it converts human-readable names to computer addresses.

### How DNS Works

```
1. You type: www.example.com
           ↓
2. Computer asks: "What's the IP address of www.example.com?"
           ↓
3. DNS Server responds: "It's 93.184.216.34"
           ↓
4. Your computer connects to: 93.184.216.34
```

### DNS Hierarchy

```
.                           (Root)
├── .com                    (Top-Level Domain)
│   ├── example.com         (Second-Level Domain)
│   │   ├── www.example.com (Subdomain)
│   │   └── api.example.com (Subdomain)
│   └── google.com
└── .org
    └── wikipedia.org
```

### DNS Resolution Steps (Detailed)

1. **Browser Cache**: Check if IP is cached locally
2. **OS Cache**: Check operating system's DNS cache
3. **Router Cache**: Check home router's cache
4. **ISP DNS Server**: Ask your internet provider
5. **Root Server**: "Ask the .com server"
6. **TLD Server**: "Ask example.com's server"
7. **Authoritative Server**: "Here's the IP: 93.184.216.34"

## Topic 4: API Design Basics

API (Application Programming Interface) is how different software components talk to each other.

### REST API Principles

REST (Representational State Transfer) is the most common API style.

**Key Principles:**
1. **Stateless**: Each request is independent
2. **Resource-based**: URLs represent resources
3. **HTTP methods**: Use GET, POST, PUT, DELETE properly
4. **JSON format**: Common data format

### Good REST API Design

```
# Users Resource
GET    /api/users           # List all users
GET    /api/users/123       # Get specific user
POST   /api/users           # Create new user
PUT    /api/users/123       # Update user
DELETE /api/users/123       # Delete user

# Nested Resources
GET    /api/users/123/posts      # Get user's posts
POST   /api/users/123/posts      # Create post for user
DELETE /api/users/123/posts/456  # Delete specific post
```

### Request/Response Example

**Request:**
```http
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json

{
  "name": "Alice",
  "email": "alice@example.com",
  "age": 25
}
```

**Response:**
```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: /api/users/123

{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com",
  "age": 25,
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Topic 5: Network Basics

### TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Reliability | Guaranteed delivery | Best effort |
| Order | Packets arrive in order | May arrive out of order |
| Speed | Slower (more overhead) | Faster (less overhead) |
| Use Cases | Web, email, file transfer | Video streaming, gaming, DNS |

### TCP Three-Way Handshake

```
Client                          Server
  │                               │
  │──── SYN (Let's connect) ─────▶│
  │                               │
  │◀─── SYN-ACK (OK, ready) ──────│
  │                               │
  │──── ACK (Great, let's go) ───▶│
  │                               │
  │    Connection Established     │
```

### Latency vs Throughput

- **Latency**: How long it takes for one request (milliseconds)
  - Example: Ping time to server
  
- **Throughput**: How much data can be transferred (MB/second)
  - Example: Download speed

**Analogy**: 
- Latency = How long it takes a bus to reach destination
- Throughput = How many passengers the bus can carry

## Topic 6: Data Formats

### JSON (JavaScript Object Notation)

Most common format for APIs.

```json
{
  "user": {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
    "active": true,
    "roles": ["user", "admin"],
    "metadata": {
      "created_at": "2024-01-15",
      "login_count": 42
    }
  }
}
```

**Advantages:**
- Human-readable
- Language-independent
- Lightweight

### XML (eXtensible Markup Language)

Older but still used.

```xml
<?xml version="1.0"?>
<user>
  <id>123</id>
  <name>Alice</name>
  <email>alice@example.com</email>
  <active>true</active>
</user>
```

### Protocol Buffers (Protobuf)

Binary format, very efficient.

```protobuf
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
  bool active = 4;
}
```

**Advantages:**
- Much smaller than JSON
- Faster to parse
- Strongly typed

## Key Takeaways

1. **Client-Server**: The basic pattern - clients request, servers respond
2. **HTTP**: The protocol that powers the web
3. **DNS**: Converts domain names to IP addresses
4. **REST APIs**: Standard way to design web APIs
5. **TCP/UDP**: Different protocols for different needs
6. **Data Formats**: JSON is most common, but alternatives exist

## Real-World Application

When you visit a website:
1. **DNS** converts domain to IP
2. **TCP** establishes connection
3. **HTTP** sends request
4. **Server** processes and responds
5. **Browser** renders the page

## Next Steps

Now that you understand the fundamentals, check out:
- **examples.md**: See real-world implementations
- **exercises.md**: Practice problems
- **solutions.md**: Detailed solutions with explanations

## Further Reading

- [HTTP Protocol RFC](https://tools.ietf.org/html/rfc2616)
- [RESTful API Design Best Practices](https://restfulapi.net/)
- [How DNS Works](https://howdns.works/)

Continue to [Module 02: Scalability Basics](../02_Scalability_Basics/) to learn how systems grow!
