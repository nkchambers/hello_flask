from flask import Flask, render_template  # Import Flask to allow us to create our app, 
                                            #added render_template to connect server to html file
                                            

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html')  # Return/send content from html file

@app.route('/success')
def success():
    return 'Success'

@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return f"Hello {name * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 