from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/add")
def add_word():

    en = request.args.get("en")
    fi = request.args.get("fi")

    word = {
        "en": en,
        "fi": fi
    }

    try:
        with open("dictionary.json", "r") as file:
            dictionary = json.load(file)

    except FileNotFoundError:
        dictionary = []

    dictionary.append(word)

    with open("dictionary.json", "w") as file:
        json.dump(dictionary, file, indent=4)

    return jsonify({"message": "Word added successfully!"})


if __name__ == "__main__":
    app.run(port=3000)