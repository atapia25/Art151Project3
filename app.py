from flask import Flask, render_template, jsonify, request, redirect
import requests
import random
from random import randint
from picamera import PiCamera

app = Flask(__name__)

normal = [16, 17, 18, 19, 20, 21, 22, 39, 40, 52, 53, 83, 84, 85, 108, 113, 115, 128, 132, 133, 137, 143, 161, 162, 163, 164]
fire = [4, 5, 6, 37, 38, 58, 59, 77, 78, 126, 136, 146, 155, 156, 157, 218, 219, 228, 229, 240, 244, 250]
water = [7, 8, 9, 54, 55, 60, 61, 62, 72, 73, 79, 80, 86, 87, 90, 91, 98, 99, 116, 117, 118, 119, 120, 121, 129, 130, 131, 134, 138, 139, 140,
141, 158, 159, 160]
grass = [1, 2, 3, 43, 44, 45, 46, 47, 69, 70, 71, 102, 103, 114, 152, 153, 154]
electric = [25, 26, 81, 82, 100, 101, 125, 135, 145, 170, 171, 172, 179, 180, 181, 239, 243]
flying = [6, 12, 16, 17, 18, 21, 22, 41, 42, 123, 130, 142, 144, 145, 146, 149, 163, 164, 165, 166]
ice = [87, 91, 124, 131]
ground = [27, 28, 50, 51, 74, 75, 76, 95, 104, 105, 111, 112]
rock = [74, 75, 76, 95, 111, 112, 138, 139, 140, 141, 142]
fighting = [56, 57, 62, 66, 67, 68, 106, 107]
ghost = [92, 93, 94]
bug = [10, 11, 12, 13, 14, 15, 46, 47, 48, 49, 123, 127, 165, 166]
steel = [81, 82, 205, 208, 212, 227]
psychic = [63, 64, 65, 79, 80, 96, 97, 102, 103, 121, 122, 124, 150, 151, 177, 178]
dark = [197, 198, 215, 228, 229, 248]
dragon = [147, 148, 149]
fairy = [35, 36, 39, 40, 122]
poison = [1, 2, 3, 13, 14, 15, 23, 24, 29, 30, 31, 32, 33, 34, 41, 42, 43, 44, 45, 48, 49, 69, 70, 71, 72, 73, 88, 89, 109, 110]

pokeTypeArray = [normal, fire, water, grass, electric, flying, ice, ground, rock, fighting, ghost, bug, steel, psychic, dark, dragon, fairy, poison]
#set up the camera
#camera = PiCamera()

#This array will change based on the color that is picked from the camera, when I get that

#since we are just returning a jsonified dictionary and not a usable html page, we don't need to make an imgandtitle html file
@app.route("/imgandtitle", methods=['GET', 'POST'])
def pokedexCall():

    #get random pokemon value
    pokeType = random.choice(pokeTypeArray)
    pokeNumber = random.choice(pokeType)
    #call the pokemon API with the random value
    base_url = f'https://pokeapi.co/api/v2/pokemon/{pokeNumber}'
    #value = randint(0, 100)
    #base_url = f'https://picsum.photos/{value}'
    pokeResults = requests.get(base_url)

    name = pokeResults.json()['name'].upper()
    #in case there are any spaces in a Pokemon's name, such as Mr. Mime
    name = name.replace('-', ' ')
    #url containing the picture
    picURL = pokeResults.json()['sprites']['other']['official-artwork']['front_default']
    #print(picture)
    HP = str(pokeResults.json()['stats'][0]['base_stat'])
    Attack = str(pokeResults.json()['stats'][1]['base_stat'])
    Defense = str(pokeResults.json()['stats'][2]['base_stat'])
    SpecialAttack = str(pokeResults.json()['stats'][3]['base_stat'])
    SpecialDefense = str(pokeResults.json()['stats'][4]['base_stat'])
    Speed = str(pokeResults.json()['stats'][5]['base_stat'])

    #Since we are replacing an attribute, all we need to do is get the new url as a string
    #use full h2 tag since we are replacing the html object with a new one
    pokeName = f'<h2 id=title>{name}</h2>'
    pokeHP = f'<h2 id=hp>HP: {HP}</h2>'
    pokeAtk = f'<h2 id=atk>Attack: {Attack}</h2>'
    pokeDef = f'<h2 id=def>Defense: {Defense}</h2>'
    pokeSpAtk = f'<h2 id=spatk>Special Attack: {SpecialAttack}</h2>'
    pokeSpDef = f'<h2 id=spdef>Special Defense: {SpecialDefense}</h2>'
    pokeSpd = f'<h2 id=spd>Speed: {Speed}</h2>'

    Data = {
        'title': pokeName,
        'url' : picURL,
        'hp' : pokeHP,
        'atk' : pokeAtk,
        'def' : pokeDef,
        'spatk' : pokeSpAtk,
        'spdef' : pokeSpDef,
        'spd' : pokeSpd
    }

    #return the json file
    return jsonify(**Data)

@app.route("/", methods = ['GET', 'POST'])
#define app function
def index():
    Hello = "Opening the PokéDex..."
    #value = randint(0, 100)
    #url = f'https://picsum.photos/{value}'
    pokeType = random.choice(pokeTypeArray)
    pokeNumber = random.choice(pokeType)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokeNumber}'
    pokeResults = requests.get(url)
    picURL = pokeResults.json()['sprites']['other']['official-artwork']['front_default']
    HP = str(pokeResults.json()['stats'][0]['base_stat'])
    Attack = str(pokeResults.json()['stats'][1]['base_stat'])
    Defense = str(pokeResults.json()['stats'][2]['base_stat'])
    SpecialAttack = str(pokeResults.json()['stats'][3]['base_stat'])
    SpecialDefense = str(pokeResults.json()['stats'][4]['base_stat'])
    Speed = str(pokeResults.json()['stats'][5]['base_stat'])
    print(picURL)
    Data = {
        'title' : Hello,
        'img' : picURL,
        'hp' : HP,
        'atk' : Attack,
        'def' : Defense,
        'spatk' : SpecialAttack,
        'spdef' : SpecialDefense,
        'spd' : Speed
    }
    return render_template('index.html', **Data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)