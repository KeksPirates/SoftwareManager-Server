from flask import Flask, jsonify, request
from data.scrapers.rutracker import scrape_rutracker, init
from data.models import SearchResponse, Post
import time

app = Flask(__name__)

debug = False
port = 8080
cache = {}

init()


@app.route('/search/<search_term>')
def search_old(search_term):
    posts = [
        Post(
            id=i,
            title="Please update SoftwareManager (API Changes)",
            url="",
            author="Update"
        )
        for i in range(1, 101)
    ]
    response = SearchResponse(success=True, query="UPDATE", data=posts, count=100)
    return jsonify(response.to_dict()), 400

@app.route('/search')
def search():
    search_term = request.args.get("q", "")

    if search_term is None or "":
        err = SearchResponse(success=False, query="", data=[], count=0)
        return jsonify(err.to_dict()), 400

    current_time = time.time()
    
    expired_keys = [key for key, (response, timestamp) in cache.items() if current_time - timestamp >= 300]
    for key in expired_keys:
        del cache[key]
    
    if search_term in cache:
        response, timestamp = cache[search_term]
        response.cached = True
        return jsonify(response.to_dict()), 200
    
    try:
        response = scrape_rutracker(search_term)
        cache[search_term] = (response, current_time)
        return jsonify(response.to_dict()), 200
    except RuntimeError as e:
        err = SearchResponse(success=False, query=search_term, data=[], count=0)
        return jsonify(err.to_dict()), 502

@app.route("/search")
def search_empty():
    err = SearchResponse(success=False, query="", data=[], count=0)
    return jsonify(err.to_dict()), 400

@app.route("/ping")
def upping():
    return jsonify({"message": "pong"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)