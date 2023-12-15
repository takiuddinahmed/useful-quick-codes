import asyncio
import redis.asyncio as aioredis
import json

async def main():
    # Create a Red
    # is connection
    redis = aioredis.from_url("redis://localhost:6379")
    
    try:
        data = {
            "event": "agreement_created",
            "data": {
                "agreement_id": "7d439a8c-3de5-4b6c-a188-e192333a6480",
                "user_id": "0000",
            }
        }

        data_json = json.dumps(data)

        # Publish the message
        await redis.publish("lax", data_json)
    finally:
        # Close the Redis connection
        await redis.close()

if __name__ == "__main__":
    asyncio.run(main())
