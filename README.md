# CDP-Support-Agent-Chatbot
A smart chatbot that provides guidance on using Segment, mParticle, Lytics, and Zeotap by extracting information from their official documentation.

Project Overview

The CDP Support Agent Chatbot is designed to assist users in answering "how-to" questions related to four Customer Data Platforms (CDPs):

Segment

mParticle

Lytics

Zeotap

The chatbot dynamically retrieves and processes information from official documentation to guide users in performing tasks or achieving specific outcomes within each platform.

Key Features

Answer "How-to" Questions

Provides step-by-step instructions for tasks like setting up sources, building audience segments, or integrating data.

Dynamic Documentation Retrieval

Extracts and processes information from live documentation using web scraping and text analysis.

Variation Handling

Handles different phrasing and variations in user questions effectively using fuzzy matching.

Cross-CDP Comparisons

Offers insights into differences in features or approaches between CDPs.

Advanced Questions

Supports platform-specific, advanced configurations, and use cases.

Core Libraries and Their Functionalities

Flask: Backend framework to handle API endpoints and user interactions.

BeautifulSoup: Scraping and parsing official documentation.

FuzzyWuzzy: Matching user queries to documentation content based on similarity.

Jinja2: Rendering dynamic responses in the chatbot interface.

HTML/CSS/JavaScript: Building the chatbot's front-end interface for an interactive user experience.

How to Use

Clone the repository:

git clone https://github.com/username/CDP-Support-Agent-Chatbot.git  

Install dependencies:

pip install -r requirements.txt  

Start the Flask server:

python app.py  

Open your browser and navigate to http://localhost:5000 to interact with the chatbot.

Screenshots

![flassk](https://github.com/user-attachments/assets/f1198953-db93-4443-af8c-2a12f0e6e3f3)

![cmd](https://github.com/user-attachments/assets/64ffd135-3c7a-4ad4-bc96-e507723e0746)

![gui](https://github.com/user-attachments/assets/0abbbc18-7ead-4b7a-b87c-2644108d415d)
![typing](https://github.com/user-attachments/assets/47cb195c-3c6e-4935-94a2-8ea88e8746fc)
![done](https://github.com/user-attachments/assets/c6376e69-9c40-4615-9f49-96bcc975de05)


Coordinator
Asim Khan
