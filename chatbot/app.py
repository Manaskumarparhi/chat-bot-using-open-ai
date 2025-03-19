from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "open ai api key"

@app.route("/")
def home():
    return render_template("index.html")  # This serves the HTML page

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
        )
        bot_reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
