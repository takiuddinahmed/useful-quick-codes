import redis
from uuid import uuid4


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def publish_to_stream(stream_name, message):
    redis_client.xadd(stream_name, message)

# Example usage
if __name__ == "__main__":
    data =  {"id":str(uuid4()), "first_name": "John", "last_name": "Doe" }
    publish_to_stream('user_created',data,)
    print("data sent to stream",data)