from flask import Flask
import threading
import os

app = Flask('')

@app.route('/healthz')
def health_check():
    return "I'm alive uwu!", 200

def run():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()
