# Module 01: Fundamentals - Practice Exercises

Apply what you've learned with these hands-on exercises!

---

## Exercise 1: Design a Simple Blog API

**Scenario**: You're building a basic blogging platform.

### Requirements:
- Users can create, read, update, and delete blog posts
- Each post has: title, content, author, created date
- Users can list all posts
- Users can view a single post by ID

### Your Tasks:

**A) Design the REST API endpoints**
```
Create a post:    POST   /api/____________________
List all posts:   GET    /api/____________________
Get single post:  GET    /api/____________________
Update a post:    PUT    /api/____________________
Delete a post:    DELETE /api/____________________
```

**B) Design the request/response for creating a post**
```http
POST /api/________
Content-Type: application/json

{
  // What fields should go here?
}

Response:
{
  // What should the response contain?
}
```

**C) Design a simple database schema**
```
Table: posts
+----+-------+
| ?? | ??    |
+----+-------+
```

---

## Exercise 2: HTTP Status Codes

**Scenario**: Match the correct HTTP status code to each situation.

Status Codes: 200, 201, 400, 401, 404, 500

**A)** User successfully creates a new account: ______

**B)** User tries to access a page that doesn't exist: ______

**C)** User successfully retrieves their profile: ______

**D)** User sends invalid data (missing required field): ______

**E)** User tries to access admin page without login: ______

**F)** Database connection fails on the server: ______

---

## Exercise 3: Design URL Structure

**Scenario**: Design clean, RESTful URLs for these operations:

**A)** Get all users:
```
URL: ________________________________
```

**B)** Get user with ID 42:
```
URL: ________________________________
```

**C)** Get all posts written by user 42:
```
URL: ________________________________
```

**D)** Get post 789 written by user 42:
```
URL: ________________________________
```

**E)** Get comments on post 789:
```
URL: ________________________________
```

---

## Exercise 4: DNS Resolution

**Scenario**: Trace the DNS resolution process.

When you type `www.example.com` in your browser, number the steps in the correct order:

```
___ Browser checks its DNS cache
___ Root DNS server responds with .com TLD server
___ ISP DNS server is queried
___ Authoritative DNS server returns IP address
___ Browser connects to the IP address
___ TLD server responds with authoritative name server
___ ISP queries root DNS server
```

---

## Exercise 5: Client-Server Interaction

**Scenario**: Describe the full flow when a user loads a webpage.

Fill in the blanks:

1. User types URL in browser
2. Browser performs __________ lookup to get IP address
3. Browser sends __________ request to server
4. Server processes request and queries __________
5. Server sends __________ response with HTML
6. Browser __________ the HTML and displays page

---

## Exercise 6: Design a Weather API

**Scenario**: Design an API for a weather service.

### Requirements:
- Get current weather for a city
- Get 7-day forecast
- Support temperature in Celsius or Fahrenheit

### Your Tasks:

**A) Design API endpoints:**
```
Current weather:  GET /api/______________________
7-day forecast:   GET /api/______________________
```

**B) Design the response format for current weather:**
```json
{
  // What fields should be included?
  // Consider: temperature, conditions, humidity, wind, etc.
}
```

**C) How would you handle the temperature unit preference?**
```
Option 1: Query parameter: /api/weather?city=London&unit=_______
Option 2: _______________________________________________
Option 3: _______________________________________________
```

---

## Exercise 7: Authentication Design

**Scenario**: Design authentication for a mobile app API.

### Requirements:
- Users register with email and password
- Users login to get access token
- Users use token to access protected endpoints

### Your Tasks:

**A) Design the registration endpoint:**
```http
POST /api/auth/__________

{
  // What fields are needed?
}

Response:
{
  // What should be returned?
}
```

**B) Design the login endpoint:**
```http
POST /api/auth/__________

{
  // What fields are needed?
}

Response:
{
  // What should be returned?
  // Include authentication token!
}
```

**C) How should protected endpoints verify the user?**
```http
GET /api/profile
// What header should be included?
___________________: Bearer token_here
```

---

## Exercise 8: Error Response Design

**Scenario**: Design a consistent error response format.

For each error, design the response:

**A) User not found (ID 999 doesn't exist):**
```json
{
  "status": ___,
  "error": "_______________",
  "message": "_______________"
}
```

**B) Invalid email format during registration:**
```json
{
  "status": ___,
  "error": "_______________",
  "message": "_______________",
  "field": "_______________"
}
```

**C) Server database connection failed:**
```json
{
  "status": ___,
  "error": "_______________",
  "message": "_______________"
}
```

---

## Exercise 9: Pagination Design

**Scenario**: You have 1000 blog posts. Design pagination.

### Your Tasks:

**A) Design URL with pagination parameters:**
```
GET /api/posts?___________&___________
```

**B) Design the response structure:**
```json
{
  "posts": [ /* array of posts */ ],
  "pagination": {
    // What fields help the client navigate?
  }
}
```

**C) If you want 20 posts per page and are on page 3:**
```
URL: GET /api/posts?page=___&limit=___
Shows posts: ___ to ___
```

---

## Exercise 10: Real-World Scenario

**Scenario**: Design a simple TODO list API.

### Requirements:
- Users can create tasks with title and description
- Users can mark tasks as complete/incomplete
- Users can delete tasks
- Users can list all their tasks
- Users can filter by complete/incomplete status

### Your Tasks:

**A) Design all necessary endpoints:**
```
Create task:     ________________________________
List tasks:      ________________________________
Get single task: ________________________________
Update task:     ________________________________
Delete task:     ________________________________
```

**B) Design database schema:**
```
Table: tasks
+----+-------+
| ?? | ??    |  (what columns do you need?)
+----+-------+
```

**C) Design request to create a task:**
```http
POST /api/________
Authorization: Bearer token123

{
  // Request body
}
```

**D) Design response for listing tasks with filter:**
```http
GET /api/tasks?status=incomplete

{
  // Response structure
}
```

---

## Bonus Challenge: Design Twitter's Tweet API

**Requirements**:
- Post a tweet (280 chars max)
- Like a tweet
- Retweet
- Reply to a tweet
- Get user's timeline
- Get trending tweets

Design:
1. All necessary endpoints
2. Request/response formats
3. Database tables needed

---

## Self-Assessment

After completing these exercises, you should be able to:

- [ ] Design RESTful API endpoints
- [ ] Choose appropriate HTTP methods and status codes
- [ ] Structure request and response JSON
- [ ] Design database schemas for APIs
- [ ] Understand DNS resolution process
- [ ] Design authentication flows
- [ ] Implement pagination
- [ ] Create consistent error responses

---

## Tips

1. **Think RESTful**: Resources as nouns, actions as HTTP methods
2. **Be Consistent**: Use the same patterns throughout your API
3. **User-Friendly**: Clear error messages and logical structure
4. **Security First**: Always require authentication for user data
5. **Plan Ahead**: Think about scaling and future features

Check **solutions.md** for detailed answers and explanations!
