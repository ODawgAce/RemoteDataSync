from flask import Flask, jsonify
from remotedatasync.fetcher import DataFetcher
from remotedatasync.processor import DataProcessor

def create_app():
    app = Flask(__name__)

    @app.route('/posts')
    def get_posts():
        fetcher = DataFetcher("https://jsonplaceholder.typicode.com/posts")
        data = fetcher.fetch()
        return jsonify(data)

    @app.route('/stats')
    def get_stats():
        fetcher = DataFetcher("https://jsonplaceholder.typicode.com/posts")
        data = fetcher.fetch()
        processor = DataProcessor(data)
        stats = processor.count_by_user()
        return jsonify(stats)

    return app