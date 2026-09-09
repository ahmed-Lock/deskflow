from flask import Flask, jsonify, render_template

app = Flask(
    __name__,
    template_folder="../frontend"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/status")
def status():
    return jsonify({
        "status": "online",
        "service": "DeskFlow"
    })


@app.route("/api/tasks")
def tasks():
    return jsonify([
        {
            "id": 1,
            "title": "Review notes",
            "completed": False
        },
        {
            "id": 2,
            "title": "Update dashboard",
            "completed": True
        }
    ])


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
