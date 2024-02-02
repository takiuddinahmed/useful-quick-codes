import socketio
import requests
 
# client
http_session = requests.Session()
 
sio = socketio.Client(
)
 
# events
@sio.event
def connect():
    print('Successfully connected to socket.io server!')
 
 
@sio.on('notification')
def get_notification(message):
    print(message)
 
# connect
sio.connect(
    #'https://alpha.lambdax.ai/?user_id=a3b614c6-1185-4e49-88cd-4b37fad4cbbf',
    'https://dev.lambdax.ai/?user_id=526a3c93-0c0c-4f8d-a5b6-df818d233270',
    #'http://localhost/?user_id=9835dd8-5fd2-4e00-bc0e-fb08eb8765a1',
    #'https://staging.lambdax.ai/?user_id=6774eb33-5450-4591-98ec-721df500a3b5',
    socketio_path='/api/v1/ws/socket.io',
    wait_timeout=60,
)
sio.wait()
 