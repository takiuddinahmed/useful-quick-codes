import redis
from uuid import uuid4


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def publish_to_stream(stream_name, message):
    redis_client.xadd(stream_name, message)

# Example usage
if __name__ == "__main__":
    data =  {"id":"95dcd87b-9d0a-409d-ac89-18d32a6e5a55", "firstname": "Takim", "lastname": "Uddin", "email": "taki+108@user.com" }
    # publish_to_stream('user_created',data)
    publish_to_stream('user_deleted',data,)
    # publish_to_stream('user_updated',data)
    # publish_to_stream('user_test',data)
    print("data sent to stream", data)