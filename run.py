from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='wwwroot', static_url_path='')

@app.route('/')
def serve_index():
    return send_from_directory('wwwroot', 'index.html')

@app.route('/greet')
def greet():
    # Print "Hello" to the console
    print("Hello")
    
    # Write "123" to a file named "AutoCreated.txt" in the local directory
    file_path = "AutoCreated.txt"
    with open(file_path, 'w') as file:
        file.write("123")
    
    return "Greeting and file creation done!"

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=8000)
