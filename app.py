from flask import Flask, render_template, request
import os
from groq import Groq

client = Groq(
    api_key="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",
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"You are an avid movie lover who has watched every movie and see movies as a primary form of entertainment and you want others to enjoy movie as much as you do, based on input: {genre}, critic reviews and popularity in pop cultre, pick a single movie, display 3 movie names with short synopsis also describe why you suggest that movie. Note: strictly dont use bold texts or asterisks in answer",
        }
    ],
    model="llama3-70b-8192",
    )
    recommended_movie = chat_completion.choices[0].message.content
    return recommended_movie

if __name__ == '__main__':
    app.run(debug=True)
