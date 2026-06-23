#!/usr/bin/env python3
"""
================================================================================
LESSON 8: ASYNCIO — SOLUTION
================================================================================
"""
import asyncio
import time

async def turn_on_lights():
    print("💡 [SmartHome] Turning on the lights...")
    await asyncio.sleep(0.5)
    print("💡 [SmartHome] Lights are now bright!")
    return "💡 Lights: ON"

async def brew_coffee():
    print("☕ [SmartHome] Brewing morning coffee...")
    await asyncio.sleep(2.0)
    print("☕ [SmartHome] Coffee is ready! ☕")
    return "☕ Coffee: BREWED"

async def fetch_news():
    print("📰 [SmartHome] Downloading daily news briefing...")
    await asyncio.sleep(1.0)
    print("📰 [SmartHome] News downloaded!")
    return "📰 News: DOWNLOADED"

async def morning_routine():
    print("🌅 Good morning! Starting routine...")
    
    # Run all three coroutines concurrently
    results = await asyncio.gather(
        turn_on_lights(),
        brew_coffee(),
        fetch_news()
    )
    
    print("\n--- Morning Routine Summary ---")
    for result in results:
        print(f"  * {result}")
    print("-------------------------------")


# --- TEST CODE ---
async def run_exercise_test():
    print("\n==================================================")
    print("RUNNING EXERCISE 8: SMART HOME MORNING ROUTINE")
    print("==================================================")
    start = time.time()
    await morning_routine()
    end = time.time()
    print(f"⏱️ Morning routine completed in {end - start:.2f} seconds! (Target: ~2.0s)")

if __name__ == "__main__":
    asyncio.run(run_exercise_test())
