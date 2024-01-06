# Space Satellite Coordinator

## Overview

The interactive web application is designed to provide real-time satellite information and solar system insights. It allows users to locate nearby satellites and explore detailed information about the planets in our solar system. Built using Python with Streamlit, it combines the functionality of APIs, real-time data, and AI-driven responses to user queries about space.

## Features
1. **Satellite Tracking**: Enter a location (latitude, longitude) to find the ten closest satellites Alternatively, use your current location to discover satellites overhead.
1. **Solar System Exploration**: Engage with a chatbot powered by OpenAI's GPT-3.5 model to ask questions about any planet or space-related topics.
1. **Dynamic Content**: The application dynamically updates with images and information about planets in our solar system.
1. **User-Friendly Interface** : Streamlit-powered interface with background images from space, enhancing user experience.

## Preview Image
![spacesatcoord](https://github.com/dlaskowski23/Girlhacks23-app/assets/123746346/ec9c3100-29c4-489e-805e-37b134ff6ee8)


## Installation
1. Clone the repository
```
git clone https://github.com/dlaskowski23/Girlhacks23-app
```
2. Install Dependencies
```    
pip install streamlit requests openai
```
3. Run the Application
```
streamlit run app.py
```

## Usage
**Satellite Tracking**
* Input your geographic coordinates (latitude, longitude) or use the button to find satellites based on your current location.
* The application will display the names and altitudes of the closest satellites.

**Solar System Exploration**
* Choose a planet from the solar system.
* Interact with the AI chatbot to get information about the selected planet.
* View detailed descriptions and images for each planet.

**API Keys**
* The application requires API keys for N2YO (for satellite data) and OpenAI (for the chatbot).
* Ensure you have your API keys set up in the code.

**Contributions**
* David Laskowski, Steven Alvarado, Daniel Lobo, Jay Santamaria 

