from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/leap-year/<int:year>")
def check_leap_year(year):
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    if is_leap_year:
        message = f"Year {year} is a leap year"
    else:
        message = f"Year {year} is not a leap year"

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
   
    
