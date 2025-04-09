users:list=[
    {"name":"Maja","location":"Inowroclaw","posts":2},
    {"name":"Oliwier","location":"Zamosc","posts":3},
    {"name":"Kuba","location":"Warszawa","posts":500},
    {"name":"Konrad","location":"Lublin","posts":10},
]



def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twoj znajomy {user["name"]} z miejscowosci {user["location"]} opublikował {user["posts"]} postow.")

get_user_info(users)