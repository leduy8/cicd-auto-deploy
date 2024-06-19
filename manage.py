import os

from main import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.environ.get("PORT", 5001))
