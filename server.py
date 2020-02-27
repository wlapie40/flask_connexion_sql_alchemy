from flask import (
    Flask,
    render_template
)
import connexion

# # Create the application instance
# app = Flask(__name__, template_folder="templates")

# creating the application instance using Connexion rather than Flask
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)