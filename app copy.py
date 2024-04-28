from flask import Flask, render_template, request
import random
from crewai import Agent, Task, Crew, Process
import os

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] ='llama3-8b-8192'  # Adjust based on available model
os.environ["OPENAI_API_KEY"] ='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'

model = Ollama(model = "llama3")
app = Flask(__name__)


# Movies data
movies = ["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form['genre']
    recommender = Agent(
        role = "Movie Buff",
        goal = "Give 10 movie recomendations which are popular and critically acclaimed",
        backstory = "You are an avid movie lover who has watched every movie and see movies as a primary form of entertainment and you want others to enjoy movie as much as you do",
        verbose = True,
        allow_delegation = False,
    )
    reviewer = Agent(
        role = "Movie critic",
        goal = "Review the recomendations given by the 'recomender' agent and based on critic reviews and popularity in pop cultre, pick a single movie, display movie name with short synopsis",
        backstory = "You are a great enthusiast of movies and also critical about them, you are great at recommending movies from a list of movies",
        verbose = True,
        allow_delegation = False,
    )

    movie = Task(
        description = f"Recommend movies based on: {genre}",
        agent = recommender,
        expected_outcome = "10 movies which are critically acclaimed, popular, cult classics"
    )

    recommended = Task(
    description = f"Recommend a single movie based on: {genre} from the list created by 'recommender' agent.",
    agent = reviewer,
    expected_outcome = "A movie which is highly watchable and recommended"
    )
    crew = Crew(
        agents = [recommender, reviewer],
        tasks = [movie, recommend],
        verbose = 2,
        process = Process.sequential
    )
    recommended_movie = crew.kickoff()
    return recommended_movie

if __name__ == '__main__':
    app.run(debug=True)
