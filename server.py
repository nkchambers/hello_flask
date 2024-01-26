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


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 