import redis
from uuid import uuid4


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def publish_to_stream(stream_name, message):
    redis_client.xadd(stream_name, message)

# Example usage
if __name__ == "__main__":

    user_data =  {"id":"95dcd87b-9d0a-409d-ac89-18d32a6e5a55", "firstname": "Takim", "lastname": "Uddin", "email": "taki+108@user.com" }
    agreement_appoval_data = {
    "user_id": "95dcd87b-9d0a-409d-ac89-18d32a6e5a55",
    "agreement_id": "95dcd87b-9d0a-409d-ac89-18d32a6e5a55",
    "agreement_role_id": "95dcd87b-9d0a-409d-ac89-18d32a6e5a55",
    "level": "test_level",
}
    stream_name = "user_agreement_role_assign"
    data = agreement_appoval_data
    publish_to_stream(stream_name,data)
