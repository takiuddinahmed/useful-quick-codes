import redis
from uuid import uuid4


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def publish_to_stream(stream_name, message):
    redis_client.xadd(stream_name, message)

# Example usage
if __name__ == "__main__":
    data =  {"id":"1ad0109e-fea4-4afc-8d3b-ce726fd054c6", "firstname": "Taki", "lastname": "Uddin", "email": "taki+104@user.com" }
    publish_to_stream('user_created',data)
    # publish_to_stream('user_deleted',data,)
    print("data sent to stream",data)