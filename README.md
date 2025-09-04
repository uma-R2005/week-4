# Week-4 Async I/O + Threading Projects

This repository contains Python projects that demonstrate real-world use cases of asynchronous I/O (asyncio) combined with threading.  
Each project simulates practical applications such as servers, chat apps, games, and more.

---

## Projects Included

### 1. High-Performance Web Server (web_server.py)
Description: Simulates a web server that processes multiple client requests while performing CPU-heavy operations in the background.  
Features:  
Handles multiple incoming requests asynchronously  
Runs encryption tasks in a separate thread  

---

### 2. Media Streaming Service (media_service.py)
Description: Mimics a video streaming service where video chunks are streamed to users while being transcoded in real-time.  
Features:  
Streams video chunks asynchronously  
Performs video transcoding in a background thread  

---

### 3. Financial Trading Platform (trading_platform.py)
Description: Simulates a trading platform that streams live market data while executing trading algorithms in parallel.  
Features:  
Streams real-time market price updates asynchronously  
Runs trading algorithm logic in a separate thread  

---

### 4. Online Multiplayer Game (multiplayer_game.py)
Description: Represents a multiplayer game server where players’ moves are processed in real time while physics calculations are handled in parallel.  
Features:  
Handles multiple player movements asynchronously  
Runs physics engine calculations in a separate thread  

---

### 5. Real-Time Chat Application (chat_app.py)
Description: Simulates a chat app that receives multiple messages asynchronously while saving chat history to a database in the background.  
Features:  
Receives chat messages asynchronously  
Saves messages to database using a background thread  

---

