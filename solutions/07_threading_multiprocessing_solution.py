#!/usr/bin/env python3
"""
================================================================================
LESSON 7: CONCURRENCY — SOLUTION
================================================================================
"""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def download_image(image_id):
    print(f"📡 [Thread] Downloading image #{image_id}...")
    time.sleep(1.0)
    print(f"✅ [Thread] Finished download for image #{image_id}!")
    return image_id

def apply_filter(image_id):
    print(f"🧠 [Process] Applying vintage filter to image #{image_id}...")
    # Heavy CPU calculation
    total = sum(i for i in range(10_000_000))
    print(f"✅ [Process] Applied filter to image #{image_id}!")
    return image_id

def process_images_concurrently():
    image_ids = [1, 2, 3, 4]
    
    # Step 1: Download images concurrently (I/O-bound)
    print("\n--- Starting Concurrent Downloads (Threading) ---")
    with ThreadPoolExecutor(max_workers=4) as thread_executor:
        downloaded = list(thread_executor.map(download_image, image_ids))
        
    # Step 2: Apply filters concurrently (CPU-bound)
    print("\n--- Starting Concurrent Filtering (Multiprocessing) ---")
    with ProcessPoolExecutor(max_workers=4) as process_executor:
        filtered = list(process_executor.map(apply_filter, downloaded))
        
    print("\n🎉 Batch processing completed successfully!")


# --- TEST CODE ---
if __name__ == "__main__":
    print("\n==================================================")
    print("RUNNING EXERCISE 7: BATCH IMAGE PIPELINE - SOLUTION")
    print("==================================================")
    pipeline_start = time.time()
    process_images_concurrently()
    pipeline_end = time.time()
    print(f"⏱️ Entire pipeline took {pipeline_end - pipeline_start:.2f} seconds!")
