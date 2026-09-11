# Module 02: Scalability Basics

Learn how to design systems that can grow from 10 users to 10 million users!

## What is Scalability?

**Scalability** is the ability of a system to handle increased load by adding resources. Think of it like:
- A restaurant adding more tables and waiters during busy hours
- A highway adding more lanes to handle traffic
- A store hiring more cashiers during holiday season

## Topic 1: Vertical vs Horizontal Scaling

### Vertical Scaling (Scale Up)

Adding more power to existing server - bigger, faster, more RAM.

```
Before (Small Server):          After (Bigger Server):
┌─────────────┐                ┌──────────────────┐
│   Server    │                │   Server Pro Max │
│             │                │                  │
│  4 GB RAM   │       →        │   32 GB RAM      │
│  2 CPU      │                │   16 CPU         │
│  100 GB SSD │                │   1 TB SSD       │
└─────────────┘                └──────────────────┘
```

**Pros:**
- ✅ Simple - no code changes needed
- ✅ No network complexity
- ✅ Consistent data (single database)

**Cons:**
- ❌ Limited - there's a maximum size
- ❌ Expensive - powerful servers cost a lot
- ❌ Single point of failure
- ❌ Downtime during upgrades

**When to use:** Small to medium applications, databases

### Horizontal Scaling (Scale Out)

Adding more servers to distribute the load.

```
Before (1 Server):         After (Multiple Servers):
┌───────────┐              ┌───────────┐  ┌───────────┐
│  Server   │              │  Server 1 │  │  Server 2 │
│           │     →        │           │  │           │
│  4 GB RAM │              │  4 GB RAM │  │  4 GB RAM │
└───────────┘              └───────────┘  └───────────┘
                                  ┌───────────┐
                                  │  Server 3 │
                                  │           │
                                  │  4 GB RAM │
                                  └───────────┘
```

**Pros:**
- ✅ Nearly unlimited scaling
- ✅ Better fault tolerance (if one fails, others continue)
- ✅ Cost-effective (use commodity hardware)
- ✅ No downtime for adding capacity

**Cons:**
- ❌ More complex architecture
- ❌ Data consistency challenges
- ❌ Network overhead
- ❌ Requires load balancer

**When to use:** Large-scale applications, web services

### Real-World Example

**Netflix:**
- Started with vertical scaling (bigger servers)
- Grew to horizontal scaling (thousands of small servers)
- Now uses cloud auto-scaling (add servers when needed)

## Topic 2: Stateless vs Stateful Services

### Stateless Services

Server doesn't remember anything about previous requests.

```
Request 1                    Request 2
┌────────┐                  ┌────────┐
│ User   │                  │ User   │
└────────┘                  └────────┘
    │                           │
    │  "Show my profile"        │  "Show my profile"
    ▼                           ▼
┌─────────┐                ┌─────────┐
│ Server1 │                │ Server2 │  ← Different server, no problem!
└─────────┘                └─────────┘
    │                           │
    │ Checks token               │ Checks token
    │ Gets data from DB         │ Gets data from DB
    ▼                           ▼
User Profile                User Profile
```

**Characteristics:**
- Each request contains all needed information
- Any server can handle any request
- Easy to scale horizontally
- User session stored in token (JWT) or database

**Example:**
```http
GET /api/profile
Authorization: Bearer eyJhbGc...
```
Token contains user ID, server uses it to fetch data.

### Stateful Services

Server remembers information between requests.

```
Request 1                    Request 2
┌────────┐                  ┌────────┐
│ User   │                  │ User   │
└────────┘                  └────────┘
    │                           │
    │  Login                    │  "Show my profile"
    ▼                           ▼
┌─────────┐                ┌─────────┐
│ Server1 │                │ Server2 │  ← Different server!
│ Session │                │ No       │
│ Stored  │                │ Session! │
└─────────┘                └─────────┘
                                │
                                ▼
                          "Please login again" ❌
```

**Characteristics:**
- Server stores session data in memory
- Must route user to same server (sticky sessions)
- Harder to scale
- If server crashes, sessions are lost

**Recommendation:** Design stateless services when possible!

## Topic 3: Performance Metrics

### Latency

Time from request to response.

```
User clicks button
      │
      │  ← 50ms  → Server responds
      ▼
Page updates
```

**Types:**
- **Network latency**: Time for data to travel
- **Processing latency**: Time server takes to process
- **Database latency**: Time to query database

**Target:** < 100ms for good user experience

### Throughput

Number of requests handled per second.

```
Second 1: ████████████ (1,200 requests)
Second 2: ███████████  (1,100 requests)
Second 3: █████████████ (1,300 requests)

Average: 1,200 requests/second
```

**Measured in:**
- Requests Per Second (RPS)
- Queries Per Second (QPS)
- Transactions Per Second (TPS)

### Response Time Percentiles

Not all requests are equal!

```
100 requests sorted by response time:
Fastest 50 (p50): 20ms  ← Half finish in 20ms
Fastest 95 (p95): 50ms  ← 95% finish in 50ms
Fastest 99 (p99): 200ms ← 99% finish in 200ms
Slowest 1 (p100): 5s    ← Outliers happen!
```

**Why percentiles matter:**
- Average can be misleading
- p99 shows worst-case for most users
- p50 (median) shows typical experience

### Availability

Percentage of time system is operational.

```
Availability = (Uptime / Total Time) × 100%

99% = 3.65 days downtime/year
99.9% (3 nines) = 8.76 hours downtime/year
99.99% (4 nines) = 52.56 minutes downtime/year
99.999% (5 nines) = 5.26 minutes downtime/year
```

**Target:** Most services aim for 99.9% - 99.99%

## Topic 4: Understanding Bottlenecks

A bottleneck is the slowest part of your system that limits overall performance.

### Common Bottlenecks

```
Request Flow:
Client → [Network] → [Server CPU] → [Database] → Response
           ↑            ↑              ↑
         Slow          Maxed         Slow
         Internet      Out            Queries
```

### 1. CPU Bottleneck

**Symptoms:**
- High CPU usage (> 80%)
- Requests queue up
- Slow processing

**Solutions:**
- Optimize algorithms
- Add more servers (horizontal scaling)
- Upgrade CPU (vertical scaling)
- Use caching

### 2. Memory Bottleneck

**Symptoms:**
- High RAM usage
- Swapping to disk
- Out of memory errors

**Solutions:**
- Optimize memory usage
- Add more RAM
- Implement pagination
- Clear unused objects

### 3. Database Bottleneck

**Symptoms:**
- Slow queries
- High database CPU
- Lock contention

**Solutions:**
- Add database indexes
- Optimize queries
- Use caching (Redis)
- Database replication
- Sharding

### 4. Network Bottleneck

**Symptoms:**
- High latency
- Packet loss
- Bandwidth saturation

**Solutions:**
- Use CDN for static content
- Compress data (gzip)
- Optimize payload size
- Upgrade network infrastructure

## Topic 5: Capacity Planning

Estimating resources needed for expected load.

### Example: Design for 1 Million Users

**Step 1: Estimate Usage**
```
Total users: 1,000,000
Daily active users (DAU): 30% = 300,000
Peak concurrent users: 10% of DAU = 30,000
Requests per user per session: 50
Average session length: 30 minutes
```

**Step 2: Calculate Load**
```
Peak requests per second (RPS):
= (30,000 users × 50 requests) / (30 min × 60 sec)
= 1,500,000 / 1,800
= 833 RPS

With safety margin (2x): 1,666 RPS
```

**Step 3: Size Infrastructure**
```
If 1 server handles 100 RPS:
Servers needed = 1,666 / 100 = 17 servers

With redundancy (N+2): 19 servers
```

**Step 4: Storage**
```
Data per user: 1 MB
Total storage: 1,000,000 × 1 MB = 1 TB
With replication (3x): 3 TB
With growth (2 years): 6 TB
```

## Topic 6: Load Testing

Testing system performance under load.

### Types of Load Tests

**1. Baseline Test**
```
Load: Normal traffic
Goal: Establish baseline metrics
```

**2. Stress Test**
```
Load: Gradually increase until system breaks
Goal: Find breaking point
```

**3. Spike Test**
```
Load: Sudden traffic surge
Goal: Test auto-scaling
```

**4. Endurance Test**
```
Load: Sustained normal traffic
Duration: Hours/days
Goal: Find memory leaks, degradation
```

### Example Load Test Plan

```python
# Gradual ramp-up
Stage 1: 100 users for 5 minutes (baseline)
Stage 2: 500 users for 10 minutes
Stage 3: 1,000 users for 10 minutes
Stage 4: 2,000 users for 10 minutes (stress)
Stage 5: 100 users for 5 minutes (cooldown)

Measure:
- Response time (p50, p95, p99)
- Throughput (RPS)
- Error rate
- Resource usage (CPU, RAM, Network)
```

## Topic 7: Scaling Patterns

### Pattern 1: Read-Heavy Application

```
Many reads, few writes (like news site)

Solution:
┌──────────────┐
│    Client    │
└──────────────┘
       │
       ▼
┌──────────────┐
│ Load Balancer│
└──────────────┘
       │
       ├───────┬───────┐
       ▼       ▼       ▼
   ┌────┐  ┌────┐  ┌────┐
   │App │  │App │  │App │  ← Many app servers
   └────┘  └────┘  └────┘
       │       │       │
       └───────┴───────┘
              │
              ▼
       ┌─────────────┐
       │   Cache     │  ← Redis for reads
       │   (Redis)   │
       └─────────────┘
              │
              ▼
       ┌─────────────┐
       │  Database   │  ← Single write DB
       └─────────────┘
```

### Pattern 2: Write-Heavy Application

```
Many writes, fewer reads (like logging system)

Solution:
- Queue writes (Message queue)
- Batch processing
- Asynchronous writes
- Multiple database shards
```

## Scalability Checklist

When designing for scale:

- [ ] Can I make services stateless?
- [ ] What will be the bottleneck?
- [ ] How much traffic do I expect?
- [ ] Can I cache frequently accessed data?
- [ ] Can I process tasks asynchronously?
- [ ] What's my database strategy?
- [ ] How will I monitor performance?
- [ ] What's my disaster recovery plan?

## Real-World Scaling Stories

### Instagram
- **Launch**: Single server
- **1 Million users**: 3 app servers, 1 database
- **10 Million users**: 100+ servers, sharded databases
- **1 Billion users**: Thousands of servers, custom infrastructure

### Key Lessons
1. Start simple, scale when needed
2. Measure before optimizing
3. Cache aggressively
4. Design for failure
5. Automate everything

## Key Takeaways

1. **Vertical Scaling**: Upgrade server (limited but simple)
2. **Horizontal Scaling**: Add more servers (unlimited but complex)
3. **Stateless**: Easier to scale, any server handles any request
4. **Metrics**: Track latency, throughput, availability
5. **Bottlenecks**: Find and fix the slowest part
6. **Capacity Planning**: Estimate before you build
7. **Load Testing**: Test before users complain

## Next Steps

- Check **examples.md** for real-world scaling scenarios
- Practice with **exercises.md**
- Review **solutions.md** for detailed explanations

Then move to [Module 03: Databases and Storage](../03_Databases_and_Storage/) to learn about data persistence!
