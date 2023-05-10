from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        return f'Hello, {first_name} {last_name}!<br>({email})<br>'
    else:
        return '''
            <!DOCTYPE html>
            <!DOCTYPE html>
            <html>
            <head>
                <title>SQlink Simple Flask App</title>
                <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
            </head>
            <body>
                <form method="POST">
                    <label>First name:</label><br>
                    <input type="text" name="first_name"><br>
                    <label>Last name:</label><br>
                    <input type="text" name="last_name"><br>
                    <label>Email:</label><br>
                    <input type="email" name="email"><br><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>      
        '''


if __name__ == '__main__':
    app.run(debug=True)
