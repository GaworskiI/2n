from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

POSTS_FILE = "posts.json"

if os.path.exists(POSTS_FILE):
    with open(POSTS_FILE, "r", encoding="utf-8") as f:
        posts = json.load(f)
else:
    posts = []

@app.route("/api/posts", methods=["GET"])
def get_posts():
    return jsonify(posts[::-1])

@app.route("/api/posts", methods=["POST"])
def add_post():
    data = request.json
    post = {
        "text": data.get("text", ""),
        "image": data.get("image", None),
        "timestamp": data.get("timestamp", None)
    }
    posts.append(post)

    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
