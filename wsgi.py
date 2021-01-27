"""
    wsgi

    This module runs the spotify_extender application
"""
from spotify_extender import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=5001, threaded=True, host='0.0.0.0')
