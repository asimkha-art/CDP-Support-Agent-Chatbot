import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Function to fetch Segment documentation
def fetch_segment_docs():
    url = 'https://segment.com/docs/?ref=nav'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('section')  
    doc_content = '\n'.join([section.text for section in content])
    return doc_content

# Function to fetch mParticle documentation
def fetch_mparticle_docs():
    url = 'https://docs.mparticle.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('article')
    doc_content = '\n'.join([article.text for article in content])
    return doc_content

# Function to fetch Lytics documentation
def fetch_lytics_docs():
    url = 'https://docs.lytics.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('section')
    doc_content = '\n'.join([section.text for section in content])
    return doc_content

# Function to fetch Zeotap documentation
def fetch_zeotap_docs():
    url = 'https://docs.zeotap.com/home/en-us/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find_all('div', class_='doc-content')
    doc_content = '\n'.join([div.text for div in content])
    return doc_content

# Enhanced Search with Fuzzy Matching
def search_in_documentation(query, documentation_content):
    lines = documentation_content.split('\n')
    
    # Use fuzzy matching to find the best result
    best_match = process.extractOne(query, lines, scorer=fuzz.partial_ratio)
    
    if best_match and best_match[1] > 70:  # If match score is higher than 70%
        return best_match[0]
    else:
        return "Sorry, I couldn't find a close match in the documentation."

# Initialize Flask App
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the CDP Support Chatbot!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()

    # Determine which CDP the user is asking about
    if 'segment' in user_message:
        doc_content = fetch_segment_docs()
        reply = search_in_documentation(user_message, doc_content)
    elif 'mparticle' in user_message:
        doc_content = fetch_mparticle_docs()
        reply = search_in_documentation(user_message, doc_content)
    elif 'lytics' in user_message:
        doc_content = fetch_lytics_docs()
        reply = search_in_documentation(user_message, doc_content)
    elif 'zeotap' in user_message:
        doc_content = fetch_zeotap_docs()
        reply = search_in_documentation(user_message, doc_content)
    else:
        reply = "Sorry, I couldn't identify the CDP you are asking about."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
