import traceback
from elasticsearch import Elasticsearch


def run():
    with get_elastic_search() as es:
        body = {
            "settings": {"number_of_shards": 4, "number_of_replicas": 1}
        }
        try:
            es.indices.create(index="anc", body=body)
        except Exception as e:
            print(traceback.format_exc())


def get_elastic_search():
    es = None

    es = Elasticsearch('http://localhost:9200',  request_timeout=20,
    retry_on_timeout=True,
    max_retries=5)
    # Check if the connection is successful
    if es.ping():
        return es
    else:
        raise Exception("Could not connect to Elasticsearch")


if __name__ == "__main__":
    run()
