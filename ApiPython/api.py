import requests
import logging

logger = logging.getLogger(__name__)

class Choices:
    def __init__(self, choices: list[str]):
        self.choices = choices
        self.count_rounds = len(choices)

    def get_data(self) -> str:
        formatted_choices = []
        for i, choice in enumerate(self.choices, start=1):
            formatted_choices.append(f"round{i}:{choice}")
        return ','.join(formatted_choices)

class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def __str__(self):
        return f"{self.username}"

class Room:
    def __init__(self, room_id, creator: User):
        self.users:list[User] = []
        self.room_id = room_id
        self.creator = creator
    
    def set_users(self, users):
        self.users = users

class Game:
    def __init__(self, player1_id, room_id, bet, time_create, choice_p1, game_id):
        self.game_id = game_id

        self.player1_id = player1_id
        self.room_id = room_id
        self.bet = bet
        self.time_create = time_create
        self.choice_p1 = choice_p1
        
        self.player2_id = None
        self.choice_p2 = None

        self.winner_id = None
    
    def connect_game(self, player2_id, choice_p2):
        self.player2_id = player2_id
        self.choice_p2 = choice_p2

    def get_winner(self, winner_id):
        self.winner_id = winner_id

class GamePlatformApi:
    def __init__(self, API_URL='http://127.0.0.1:8000/api/'):
        self.API_URL = API_URL

    def __make_request(self, method, endpoint, token=None, data=None):
        url = f'{self.API_URL}{endpoint}'
        headers = self.__get_headers(token) if token else {}
        
        response = requests.request(method, url, headers=headers, json=data)
        logger.info(f"Request {method} {url} returned status {response.status_code}")
        if response.status_code in [200, 201]:
            return response.json()
        else:
            logger.error(f"Request {method} {url} failed with status {response.status_code}: {response.text}")
            response.raise_for_status()
    
    def __get_headers(self, token):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def register_user(self, username, email, password, wallet_address) -> dict:
        data = {
            'username': username,
            'email': email,
            'password': password,
            'wallet_address': wallet_address
        }
        
        user_data = self.__make_request('POST', 'users/register/', data=data)
        return user_data

    def login_user(self, username, password) -> str:
        data = {'username': username, 'password': password}
        json_response = self.__make_request('POST', 'users/token/', data=data)
        return json_response.get('access')

    def room_create(self, token: str) -> Room:
        room_data = self.__make_request('POST', 'rooms/create-room/', token)
        room = Room(room_id=room_data['id'], creator=User(room_data['creator']['username'], room_data['creator']['id']))
        return room

    def room_leave(self, token: str, id_room: int) -> dict:
        return self.__make_request('POST', f'rooms/{id_room}/leave-room/', token)

    def room_join(self, token: str, id_room: int) -> dict:
        return self.__make_request('POST', f'rooms/{id_room}/join-room/', token)

    def get_users_in_room(self, token: str, id_room: int) -> list[User]:
        users_data = self.__make_request('GET', f'rooms/{id_room}/users/', token)
        users = [User(user['username'], user['id']) for user in users_data]
        return users

    def get_rooms(self, token: str) -> list[Room]:
        rooms_data = self.__make_request('GET', 'rooms/', token)
        rooms = []
        
        for room_json in rooms_data:
            creator = User(room_json['creator']['username'], room_json['creator']['id'])
            users = [User(user['username'], user['id']) for user in room_json['users']]
            room = Room(room_json['id'], creator)
            room.set_users(users)
            rooms.append(room)
        
        return rooms
    
    def game_create(self, token: str, room_id: int, choices: Choices, bet: float) -> dict:
        data = {
            'room_id': room_id,
            'bet': bet,
            'choices': choices.get_data()
        }
        return self.__make_request('POST', 'games/create-game/', token, data)
    
    


#test 
platform = GamePlatformApi()


token = platform.login_user('admin', '111')
rooms = platform.get_rooms(token)

for room in rooms:
    print(f'id: {room.room_id}\ncreator:{room.creator.username}')
    print('users: ',end='')
    for user in room.users:
        print(user.username, end=' ')
    print('\n\n')