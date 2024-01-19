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
                "agreement_id": "a47b2e31-1a26-44f1-981d-bffb1fad895f",
                "user_id": "0000",
            }
        }

        data_json = json.dumps(data)

        # Publish the message
        await redis.publish("lax", data_json)
    finally:
        # Close the Redis connection
        await redis.aclose()

if __name__ == "__main__":
    asyncio.run(main())
