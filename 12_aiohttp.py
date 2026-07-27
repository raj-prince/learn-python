#!/usr/bin/env python3
"""
================================================================================
LESSON 12: AIOHTTP — ASYNCHRONOUS HTTP CLIENT AND SERVER IN PYTHON
================================================================================

In Lesson 8, we introduced `asyncio`, Python's built-in module for cooperative 
multitasking. However, standard library modules like `urllib` or popular third-party 
libraries like `requests` are SYNCHRONOUS (blocking). If you call `requests.get()` 
inside an async coroutine, it will freeze the entire event loop!

To perform asynchronous HTTP requests, we use `aiohttp` — an asynchronous HTTP 
client/server framework built on top of `asyncio`.

--------------------------------------------------------------------------------
1. WHY AIOHTTP?
--------------------------------------------------------------------------------
- Non-blocking I/O: Allows your application to send hundreds or thousands of HTTP 
  requests concurrently without spawning heavy OS threads.
- High Performance: Essential for web scrapers, API aggregators, microservices, 
  and real-time web applications.
- Full Stack: Acts as both an HTTP Client (to consume APIs) and an HTTP Server 
  (to build web APIs).

--------------------------------------------------------------------------------
2. KEY CONCEPTS & BEST PRACTICES
--------------------------------------------------------------------------------
1. `aiohttp.ClientSession()`:
   - Manages a pool of persistent connections (HTTP Keep-Alive).
   - DO NOT create a new session for every request! Create ONE session per application 
     or worker task and reuse it.
2. `async with`:
   - Both the session and the response objects are Async Context Managers.
   - You must use `async with session.get(...) as response:` to clean up resources automatically.
3. Awaiting Response Methods:
   - Response bodies are streamed asynchronously.
   - Use `await response.text()` for string content.
   - Use `await response.json()` for JSON decoding.
   - Use `await response.read()` for raw bytes.
"""

import asyncio
import time
import aiohttp
from aiohttp import web

# ================================================================================
# PART 1: AIOHTTP CLIENT EXAMPLES
# ================================================================================

# --- 1. Basic Single Request ---
async def fetch_single_url(session, url):
    """Fetches a single URL asynchronously using an existing ClientSession."""
    print(f"🌐 Fetching {url}...")
    async with session.get(url) as response:
        print(f"Status Code: {response.status}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        # Await the response body parsing
        data = await response.json()
        return data


# --- 2. Concurrent Requests with asyncio.gather ---
async def fetch_pokemon(session, pokemon_name):
    """Fetch details of a Pokemon from PokéAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            name = data['name'].capitalize()
            height = data['height']
            weight = data['weight']
            types = [t['type']['name'] for t in data['types']]
            return f"✨ {name}: Height={height}, Weight={weight}, Types={types}"
        else:
            return f"❌ Failed to fetch {pokemon_name} (Status: {response.status})"


async def run_concurrent_client_demo():
    print("\n==================================================")
    print("DEMO 1: CONCURRENT HTTP REQUESTS (POKÉAPI)")
    print("==================================================")
    
    pokemon_list = ["pikachu", "charizard", "bulbasaur", "squirtle", "gengar"]
    
    start_time = time.time()
    
    # Best Practice: Use ONE session for all requests
    async with aiohttp.ClientSession() as session:
        # Schedule all requests concurrently
        tasks = [fetch_pokemon(session, poke) for poke in pokemon_list]
        results = await asyncio.gather(*tasks)
        
        for res in results:
            print(res)
            
    elapsed = time.time() - start_time
    print(f"⏱️ Fetched {len(pokemon_list)} APIs concurrently in {elapsed:.2f} seconds!")


# --- 3. Rate Limiting with asyncio.Semaphore ---
async def fetch_with_semaphore(semaphore, session, item_id):
    """Limit concurrent requests using an asyncio.Semaphore."""
    async with semaphore:
        url = f"https://jsonplaceholder.typicode.com/todos/{item_id}"
        async with session.get(url) as response:
            data = await response.json()
            print(f"  [Task {item_id}] Completed: {data.get('title')[:30]}...")
            return data


async def run_semaphore_demo():
    print("\n==================================================")
    print("DEMO 2: CONCURRENCY CONTROL WITH SEMAPHORE")
    print("==================================================")
    
    # Limit max concurrent connections to 3
    semaphore = asyncio.Semaphore(3)
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_semaphore(semaphore, session, i) for i in range(1, 10)]
        await asyncio.gather(*tasks)


# --- 4. Timeout and Error Handling ---
async def run_error_handling_demo():
    print("\n==================================================")
    print("DEMO 3: TIMEOUT AND ERROR HANDLING")
    print("==================================================")
    
    # Configure a custom 2-second total timeout
    timeout = aiohttp.ClientTimeout(total=2.0)
    
    async with aiohttp.ClientSession(timeout=timeout) as session:
        # A) Test Timeout on a delayed response endpoint
        print("Testing Timeout (httpbin delay 3s with 2s timeout)...")
        try:
            async with session.get("https://httpbin.org/delay/3") as resp:
                await resp.text()
        except asyncio.TimeoutError:
            print("⚠️ Request timed out as expected!")
        except aiohttp.ClientError as e:
            print(f"⚠️ Client error: {e}")

        # B) Handling status errors automatically with raise_for_status()
        print("Testing raise_for_status() on 404 endpoint...")
        try:
            async with session.get("https://httpbin.org/status/404") as resp:
                resp.raise_for_status()
        except aiohttp.ClientResponseError as err:
            print(f"⚠️ Handled response status error: Status {err.status} - {err.message}")


# ================================================================================
# PART 2: AIOHTTP SERVER EXAMPLE
# ================================================================================

async def handle_hello(request):
    """HTTP GET Request Handler."""
    name = request.match_info.get('name', "World")
    text = f"Hello, {name}! Welcome to aiohttp web server."
    return web.Response(text=text)

async def handle_json_api(request):
    """HTTP POST / API Request Handler receiving JSON."""
    try:
        data = await request.json()
        response_data = {
            "status": "success",
            "received": data,
            "server_timestamp": time.time()
        }
        return web.json_response(response_data)
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=400)


def build_app():
    """Create and configure the aiohttp Web Application."""
    app = web.Application()
    app.add_routes([
        web.get('/', handle_hello),
        web.get('/hello/{name}', handle_hello),
        web.post('/api/echo', handle_json_api),
    ])
    return app


# ================================================================================
# MAIN ENTRY POINT
# ================================================================================

async def main():
    # Run Client Demos
    await run_concurrent_client_demo()
    await run_semaphore_demo()
    await run_error_handling_demo()
    
    print("\n==================================================")
    print("DEMO 4: EMBEDDED AIOHTTP SERVER DEMO")
    print("==================================================")
    app = build_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 8080)
    await site.start()
    print("🚀 Server started on http://127.0.0.1:8080")
    
    # Test client sending requests to our own server!
    async with aiohttp.ClientSession() as session:
        # GET /hello/PythonLearner
        async with session.get("http://127.0.0.1:8080/hello/PythonLearner") as resp:
            text = await resp.text()
            print(f"GET Response: {text}")
            
        # POST /api/echo
        async with session.post("http://127.0.0.1:8080/api/echo", json={"topic": "aiohttp", "difficulty": "intermediate"}) as resp:
            json_res = await resp.json()
            print(f"POST Response: {json_res}")

    # Clean shutdown of server
    await runner.cleanup()
    print("🛑 Server shutdown gracefully.")

if __name__ == "__main__":
    asyncio.run(main())
