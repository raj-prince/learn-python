import asyncio
import time
from aiohttp import web, ClientSession

async def fast_stream(request):
    resp = web.StreamResponse(headers={"Content-Type": "application/octet-stream"})
    await resp.prepare(request)
    chunk = b"X" * (256 * 1024)
    for _ in range(200):  # 50 MB total
        await resp.write(chunk)
    await resp.write_eof()
    return resp

async def run_benchmark():
    app = web.Application()
    app.router.add_get("/stream", fast_stream)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", 8999)
    await site.start()

    # 1. Slow: 4 KB chunks
    async with ClientSession() as session:
        t0 = time.perf_counter()
        total = 0
        async with session.get("http://127.0.0.1:8999/stream") as resp:
            async for chunk in resp.content.iter_chunked(4 * 1024):
                total += len(chunk)
        t_4k = time.perf_counter() - t0

    # 2. Fast: 256 KB chunks
    async with ClientSession() as session:
        t0 = time.perf_counter()
        total = 0
        async with session.get("http://127.0.0.1:8999/stream") as resp:
            async for chunk in resp.content.iter_chunked(256 * 1024):
                total += len(chunk)
        t_256k = time.perf_counter() - t0

    # 3. Fast: iter_any() (Consume whatever TCP buffer already has without re-slicing)
    async with ClientSession() as session:
        t0 = time.perf_counter()
        total = 0
        async with session.get("http://127.0.0.1:8999/stream") as resp:
            async for chunk in resp.content.iter_any():
                total += len(chunk)
        t_any = time.perf_counter() - t0

    # 4. Fast: read(256 * 1024) in a while loop
    async with ClientSession() as session:
        t0 = time.perf_counter()
        total = 0
        async with session.get("http://127.0.0.1:8999/stream") as resp:
            while True:
                chunk = await resp.content.read(256 * 1024)
                if not chunk:
                    break
                total += len(chunk)
        t_read_256k = time.perf_counter() - t0

    mb = 50.0
    print("=" * 70)
    print("50 MB ASYNC NETWORK STREAMING OPTIMIZATION BENCHMARK")
    print("=" * 70)
    print(f"1. 4 KB chunks (iter_chunked(4KB)):     {t_4k*1000:6.2f} ms ({mb/t_4k:7.1f} MB/s)")
    print(f"2. 256 KB chunks (iter_chunked(256KB)): {t_256k*1000:6.2f} ms ({mb/t_256k:7.1f} MB/s)")
    print(f"3. Zero-Slicing (iter_any()):           {t_any*1000:6.2f} ms ({mb/t_any:7.1f} MB/s)")
    print(f"4. Direct Read (read(256KB)):           {t_read_256k*1000:6.2f} ms ({mb/t_read_256k:7.1f} MB/s)")
    print("=" * 70)

    await runner.cleanup()

if __name__ == "__main__":
    asyncio.run(run_benchmark())
