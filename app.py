from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Sample data for CDP responses
cdp_responses = {
    "segment": {
        "new source": "To set up a new source in Segment:\n"
                      "1. Log in to your Segment workspace.\n"
                      "2. Click on 'Sources' from the main menu.\n"
                      "3. Select 'Add Source' and choose the type of source you want to add.\n"
                      "4. Follow the setup instructions specific to the source.\n"
                      "5. Save the configuration and start sending data.",
    },
    "mparticle": {
        "user profile": "To create a user profile in mParticle:\n"
                        "1. Log in to the mParticle dashboard.\n"
                        "2. Navigate to the 'Users' section.\n"
                        "3. Click 'Create User Profile' and fill in the required details.\n"
                        "4. Save the profile to make it active.",
    },
    "lytics": {
        "audience segment": "To build an audience segment in Lytics:\n"
                            "1. Log in to the Lytics platform.\n"
                            "2. Go to the 'Audiences' tab.\n"
                            "3. Click 'Create Audience' and define your segment criteria.\n"
                            "4. Save the audience segment and use it for targeting.",
    },
    "zeotap": {
        "connect crm": "To connect Zeotap to a CRM:\n"
                       "1. Log in to your Zeotap dashboard.\n"
                       "2. Navigate to the 'Integrations' section.\n"
                       "3. Select your CRM provider (e.g., Salesforce, HubSpot).\n"
                       "4. Follow the on-screen instructions to authenticate and map your data fields.\n"
                       "5. Save and activate the integration.\n"
                       "For more details, visit: https://docs.zeotap.com/integrations/"
    }
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower().strip()  # Convert to lowercase and remove extra spaces

    # Search for a relevant response
    for cdp, tasks in cdp_responses.items():
        if cdp in user_message:  # Check if the CDP name is in the message
            for task, response in tasks.items():
                if all(word in user_message for word in task.split()):  # Match task keywords
                    return jsonify({"reply": response.split("\n")})  # Return the response as a list

    # If no match is found
    return jsonify({"reply": ["Sorry, I couldn't find relevant information for your query."]})

if __name__ == '__main__':
    app.run(debug=True)
