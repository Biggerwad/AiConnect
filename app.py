
from flask import Flask, request, jsonify
import openai 
from decouple import config

OPENAIKEY = config('OPENAIKEY')
DEBUG = config('DEBUG', default=False, cast=bool)

app = Flask(__name__)

# Passing openai credentials
api_key = OPENAIKEY
openai.api_key = api_key

# EXPOSING API
@app.route('/api/ask_openai', methods=['POST'])
def ask_openai():
    # Getting the request from user endpoint
    input_text = request.json.get('input_text','')

    prompt = input_text

    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_token=50
        )
        # Providing OpenAI response
        generated_text = response.choices[0].text
    
    # Converting to JSON, the result
        return jsonify({'generated_text':generated_text})
    
    # Catering for errors
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    
    # RUNNING THE APP
    app.run(DEBUG)