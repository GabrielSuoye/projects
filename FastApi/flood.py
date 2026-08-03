import asyncio
import httpx
import time

TARGET_URL = "http://127.0.0.1:8000/books"
TOTAL_REQUESTS = 300


async def send_single_request(client, request_id):
    try:
        response = await client.get(TARGET_URL)
        print(
            f"[Req {request_id}] Status: {response.status_code} | Response: {response.json()}"
        )
    except Exception as e:
        print(f"[Req {request_id}] Connection Failed: {e}")


async def main():
    print(f"Starting load test against {TARGET_URL}...")
    start_time = time.time()

    async with httpx.AsyncClient() as client:
        tasks = [send_single_request(client, i) for i in range(TOTAL_REQUESTS)]
        await asyncio.gather(*tasks)

    duration = time.time() - start_time
    print(f"\nTest finshed. Sent {TOTAL_REQUESTS} requests in {duration:2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
