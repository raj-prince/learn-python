import asyncio
import time
from aiohttp import web, ClientSession, TCPConnector

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
    site = web.TCPSite(runner, "127.0.0.1", 8997)
    await site.start()

    # 1. Default aiohttp ClientSession (read_bufsize = 64 KB default)
    async with ClientSession() as session:
        t0 = time.perf_counter()
        async with session.get("http://127.0.0.1:8997/stream") as resp:
            contents = await resp.read()
        t_default = time.perf_counter() - t0

    # 2. Optimized aiohttp ClientSession (read_bufsize = 2 MB + tuned TCPConnector)
    connector = TCPConnector(limit=100, keepalive_timeout=60, enable_cleanup_closed=True)
    async with ClientSession(connector=connector, read_bufsize=2 * 1024 * 1024) as session:
        t0 = time.perf_counter()
        async with session.get("http://127.0.0.1:8997/stream") as resp:
            contents = await resp.read()
        t_optimized = time.perf_counter() - t0

    mb = 50.0
    print("=" * 70)
    print("50 MB `await resp.read()` (NON-STREAMING) OPTIMIZATION BENCHMARK")
    print("=" * 70)
    print(f"1. Default Session (64 KB read_bufsize):    {t_default*1000:6.2f} ms ({mb/t_default:7.1f} MB/s)")
    print(f"2. Optimized Session (2 MB read_bufsize):  {t_optimized*1000:6.2f} ms ({mb/t_optimized:7.1f} MB/s)")
    print(f"🚀 Speedup Factor:                         {t_default/t_optimized:6.2f}x faster")
    print("=" * 70)

    await runner.cleanup()

if __name__ == "__main__":
    asyncio.run(run_benchmark())
