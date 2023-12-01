import os
from app import app
from dotenv import load_dotenv

load_dotenv()

port = os.getenv('PORT') or 80
host = os.getenv('HOST') or "0.0.0.0"

if __name__ == "__main__":
    app.run(debug=app.debug, port=port, host=host)
