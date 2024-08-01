data = [
    {"name": "Jostar", "score": 90, "height": 195, "weight": 70},
    {"name": "Joseph", "score": 80, "height": 194, "weight": 60},
    {"name": "Jotaro", "score": 85, "height": 193, "weight": 72},
    {"name": "Josuke", "score": 88, "height": 175, "weight": 68},
    {"name": "Giorno", "score": 95, "height": 178, "weight": 55},
    {"name": "Jolyne", "score": 92, "height": 163, "weight": 50},
    {"name": "Caesar", "score": 89, "height": 182, "weight": 75},
    {"name": "Speedo", "score": 87, "height": 179, "weight": 73},
    {"name": "Dio", "score": 86, "height": 178, "weight": 71},
    {"name": "Kakyoin", "score": 84, "height": 188, "weight": 69},
]

print(data[0]["score"]+data[1]["score"]+data[2]["score"])
for person in enumerate(name):
    score = person["score"]
    height = person["height"]
    weight = person["weight"]
    name = person["name"]
    
    score += score
    print(person)



for i in enumerate(data):

    print(i)
    print(i.get("score"))


anime = {
    "name": "JoJo的奇妙冒險",
    "publisher": "集英社",
    "genre": ["動作", "超自然", "冒險", "奇幻"],
    "author": "荒木飛呂彦",
    "volumes": 134,
    "status": "連載中",
}

for key in anime:
    print(key)

print("---")

for key, value in anime.items():
    print(f"{key}: {value}")

