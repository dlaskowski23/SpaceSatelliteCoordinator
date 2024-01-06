import streamlit as st
import streamlit.components.v1 as components
import requests

import os

import openai

import codecs



st.title("Space Satellite Coordinator")

bg_img = '''
    <style>
    .stApp {
    background-image: url("https://images.pexels.com/photos/998641/pexels-photo-998641.jpeg");
    background-size: cover;
    }
    </style>
    '''

st.markdown(bg_img, unsafe_allow_html=True)

##st.image("images/Weather Satellite Images_ If the Earth Took a Selfie.jpeg", width=300)

# Function to get satellite info based on location
def get_satellite_info(location):
    latitude, longitude = map(float, location.split(","))
    api_key = "VVELHC-KKU8DP-Q7D92Q-54GM"

    url = f"https://api.n2yo.com/rest/v1/satellite/above/{latitude}/{longitude}/0/70/0/?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    return data

# Text input for user location
user_input_location = st.text_input("Enter any location to find the 10 closest satellites floating above it in space. (latitude, longitude) press Enter: ")

# Button to fetch satellite information based on user input
if st.button("Or find the 10 closest satellites using your current location"):
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        if "loc" in data:
            current_location = data["loc"]
            satellite_data = get_satellite_info(current_location)
            st.write("10 closest satellites above your current location:")
            for i, sat in enumerate(satellite_data['above']):
                if i >= 10:  # Display only the first 10 satellites
                    break
                st.write(f"Name: {sat['satname']}, Altitude: {sat['satalt']} km")
        else:
            st.error("Error fetching user location.")
    except Exception as e:
        st.error(f"Error fetching user location: {e}")

elif user_input_location:
    satellite_data = get_satellite_info(user_input_location)
    st.write(f"Satellites above the specified location ({user_input_location}):")
    for i, sat in enumerate(satellite_data['above']):
        if i >= 10:  # Display only the first 10 satellites
            break
        st.write(f"Name: {sat['satname']}, Altitude: {sat['satalt']} km")
        
        
        
def callApi(input, planet):
    

    openai.api_key = "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"
    messages = [ {"role": "system", "content": 
              "You are a intelligent SPACE assistant. You are to act as a chatbot for my space and solar system website to provide answers to questions about any planet or anything space related. Always stay on the topic of space and be as informative as you can. Limit your responses to 50 words."} ]
    
    messages.append(
         {"role": "user", "content": input}
        )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response['choices'][0]['message']['content']


    st.write(reply)

    

def get_planet_info(planet_name):
    planet_info = {
        "Mercury": "Mercury is the closest planet to the Sun, with extreme temperature variations. It has a very thin atmosphere and no moons. Temperature: Extremely hot (up to 430°C) and cold (as low as -180°C), Size: Smallest terrestrial planet in the Solar System, Distance from Earth: Varies between 77.3 million km and 261 million km, Eccentric Orbit: Mercury has a highly eccentric orbit, causing significant temperature variations.",
        "Venus": "Venus is known for its thick, toxic atmosphere and scorching surface temperatures. It rotates in the opposite direction to most planets. Temperature: Hottest planet with surface temperatures around 467°C, Size: Similar in size to Earth, often called Earth's 'sister planet', Distance from Earth: Varies between 38 million km and 261 million km, Super-Rotation: Venus has a super-rotational atmosphere, with winds faster than its rotation.",
        "Earth": "Earth is our home, known for its diverse ecosystems and moderate climate. It has one natural satellite, the Moon. Temperature: Moderate temperatures suitable for life, Size: Fifth-largest planet with a diverse range of ecosystems, Distance from Earth: Always at a distance of 0 km (it's our home!), Life Support: Earth is the only known planet to support a wide variety of life forms.",
        "Mars": "Mars is the Red Planet with a thin atmosphere and evidence of past water flows. It has the largest volcano in the solar system. Temperature: Cold with average temperatures around -80°C, Size: Fourth planet, often referred to as the 'Red Planet', Distance from Earth: Varies between 54.6 million km and 401 million km, Volcanic Giant: Mars has the tallest volcano, Olympus Mons, and the deepest canyon, Valles Marineris, in the solar system.",
        "Jupiter": "Jupiter is a gas giant, the largest planet, and has a strong magnetic field. It has a complex system of rings and many moons. Temperature: Very cold in the upper atmosphere but extremely hot at its core, Size: Largest planet in the Solar System, mainly composed of gas, Distance from Earth: Varies between 588 million km and 968 million km, Giant Magnet: Jupiter has a strong magnetic field and the Great Red Spot, a massive storm.",
        "Saturn": "Saturn is famous for its stunning rings, made up of ice and rock particles. It is less dense than water and could float in a giant bathtub. Temperature: Cold in the upper atmosphere, hot at its core, Size: Famous for its stunning ring system, Distance from Earth: Varies between 1.2 billion km and 1.68 billion km, Ringed Beauty: Saturn's rings are made up of countless individual ringlets and are incredibly thin.",
        "Uranus": "Uranus is an ice giant, known for its tilted axis and unique blue-green color. It rotates almost on its side. Temperature: Extremely cold, with temperatures as low as -224°C, Size: Seventh planet, known for its unique blue-green color, Distance from Earth: Varies between 2.6 billion km and 3 billion km, Tilted Axis: Uranus has a highly inclined rotational axis, making it appear to roll on its side.",
        "Neptune": "Neptune is the farthest planet from the Sun, with strong winds and icy storms. It has a dark spot known as the 'Great Dark Spot.' Temperature: Extremely cold, with temperatures as low as -220°C, Size: Eighth and farthest planet from the Sun, Distance from Earth: Varies between 4.3 billion km and 4.7 billion km, Windy Giant: Neptune has the fastest winds in the Solar System, reaching up to 2,100 km/h."
    }

    planet_description = planet_info.get(planet_name, "No information available")

    return planet_description


def get_planet_picture_url(planet_name):
    planet_picture_urls = {
        "Mercury": "./imgs/mercury.jpg",
        "Earth": "./imgs/earth.jpg",
        "Mars": "./imgs/mars.png",
        "Saturn": "./imgs/saturn.png",
        "Jupiter": "./imgs/jupiter.jpg",
        "Venus": "./imgs/venus.png",
        "Uranus": "./imgs/uranus.jpg",
        "Neptune": "./imgs/neptune.jpg",
        
    }
    return planet_picture_urls.get(planet_name, "./imgs/solar.jpg")

def get_prompt(planet_name):
    planet_prompts = {
        "Mercury": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Earth": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Mars": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Saturn": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Jupiter": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Venus": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Uranus": f"Ask questions about {planet_name} with our interactive space expert AI!",
        "Neptune": f"Ask questions about {planet_name} with our interactive space expert AI!",
    }
    return planet_prompts.get(planet_name, "")
    
    
planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]



st.title("Solar System Planets")


main_container = st.container()
main_container.write(f"Here is our Solar System!")

pic, info = st.columns(2)
ai = st.container()


planet_name = "Solar System"
planet_info = "The solar system is a vast celestial family centered around the Sun, comprising eight planets, numerous moons, asteroids, comets, and other celestial objects, all orbiting in the cosmos. It serves as a cosmic laboratory, unraveling the mysteries of the universe and offering glimpses into the origins of our world."
planet_picture_url="./imgs/solar.png"






with pic:
    st.header(planet_name)
    st.image(planet_picture_url, use_column_width=True)

with info:
    st.header("Information")
    st.write(planet_info)
question = st.text_input(label="Chatbot",placeholder="Got a question about our "+ planet_name+"? Ask away!")
if question:
    callApi(question, planet_name)

    
def update():
    with pic:
        st.header(planet_name)
        st.image(planet_picture_url, use_column_width=True)

    with info:
        st.header("Information")
        st.write(planet_info)

for i in range(0, 8, 2):
    col1, col2 = st.columns(2)
    col1.image(get_planet_picture_url(planet_names[i]), width=80)
    if col1.button(planet_names[i]):
        planet_name = planet_names[i]
        planet_info = get_planet_info(planet_name)
        planet_picture_url = get_planet_picture_url(planet_name)
        ai.write(get_prompt(planet_names[i]))
        update()

    
    col2.image(get_planet_picture_url(planet_names[i+1]), width=80)
    if col2.button(planet_names[i + 1]):
        planet_name = planet_names[i + 1]
        planet_info = get_planet_info(planet_name)
        planet_picture_url = get_planet_picture_url(planet_name)
        ai.write(get_prompt(planet_names[i + 1]))
        update()
        



