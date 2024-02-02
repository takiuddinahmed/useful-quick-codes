import requests

def get_http_response():
    url = 'http://localhost:8080/api/v1/flow-orchestrator/steps'
    
    response = requests.get(url)
    return response.json()


def get_date():
    res = get_http_response()
    list = res.get('data')

    # save data to csv
    with open('node_list.csv', 'w') as f:
        f.write("Title,Category,Type\n")
        for item in list:
            f.write(f"{item['description']},{item['category']},{item['type']}\n")


if __name__ == '__main__':
    get_date()