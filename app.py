from flask import Flask, request, jsonify
from ai_generator import generate

app = Flask(__name__)

@app.route("/generate", method="GET")
def get_blog():
    keyword = request.args.get("keyword")
    if not keyword:
        return "Missing keyword in the parameter",400

    blog_post = generate(keyword)

    return jsonify({
        "keyword": keyword,
        "blog_post": blog_post
    })

def scheduler():
    pass

if __name__ == "__main__":
    app.run(debug=True)