from flask import Flask, jsonify

app = Flask(__name__)

news = [
    {
        "title": "Technology News",
        "description": "Latest developments in technology."
    },
    {
        "title": "AI News",
        "description": "Artificial intelligence is changing the world."
    },
    {
        "title": "World News",
        "description": "Latest news from around the world."
    }
]

@app.route("/")
def home():
    return "News Aggregator API is running!"

@app.route("/news")
def get_news():
    return jsonify(news)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
