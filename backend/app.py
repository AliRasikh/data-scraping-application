"""
This module provides a Flask web application for scraping static
websites and saving the output to a TXT file.
It includes endpoints for scraping a website,
downloading the scraped content as a TXT file, and managing URLs in a database.
Endpoints:
- /scrape_with_bs4 (POST): Scrapes a static website and returns the raw HTML.
- /download/txt (GET): Downloads the scraped HTML content as a TXT file.

"""

<<<<<<< HEAD
from config import app #, db
from flask import request, jsonify

from core.scraper import scrape_with_bs4, scrape_with_requests
from core.file_handler import scraped_data_to_txt_file, get_txt_file
=======
import os
from os import path
from config import app, db
from flask import request, jsonify
from core.scraper import scrape_with_bs4, scrape_with_requests
from core.file_handler import scraped_data_to_txt_file, get_txt_file
from core.repository import store_user_history
from core.models import User, History
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_login import login_user, login_required, logout_user, current_user
>>>>>>> origin/signup_login_ali


@app.route("/scrape", methods=["POST"])
def scrape():
    """
    Endpoint to scrape a static website and save the output to a TXT file.
    Expects a JSON body with a "url" key.
<<<<<<< HEAD
    """
    # retrieve the json data from the post request
    data = request.json
    print("received data:", data)
    url = data.get("url")
    scraping_method = data.get("scraping_method")
    print(f"Received URL: {url}, Scraping Method: {scraping_method}")


    # if no url is provides , return an error with http 400 status(bad request)
    if not url:
        return jsonify({"error": "URL is required"}), 400
    if not scraping_method:
        return jsonify({"error": "Scraping method is required"}), 400

    if scraping_method == "requests":
        # call the scrape website func for the scraped result
        raw_html = scrape_with_requests(url)
    elif scraping_method == "bs4":
        # call the scrape website func for the scraped result
        raw_html = scrape_with_bs4(url)
    else:
        return jsonify({"error": "Invalid scraping method"}), 400

    # AICI S-A MODIFICAT:
    # Verificăm dacă `raw_html` este un dicționar cu eroare și returnăm răspunsul JSON
    # if isinstance(raw_html, dict) and "error" in raw_html:
    #     return jsonify(raw_html), 400  # Return JSON error response with status 400
    
    # print(f"Saving to file: {type(raw_html)}")  # Afișează tipul de date al `raw_html`
    # if isinstance(raw_html, dict):
    #     print(f"Dictionary content: {raw_html}")  # Afișează conținutul dacă e `dict`

    scraped_data_to_txt_file(raw_html)


    return (
        jsonify(
            {
                "message": f"URL Scraped with {scraping_method} and content saved to TXT file"
=======
    json response: status: 1 -> success, if 2 -> error
    """
    print("test")
    # retrieve the json data from the post request
    data = request.json
    url = data.get("url")
    scraping_method = data.get("scraping_method")

    # if no url is provides , return an error with http 400 status(bad request)
    if not url:
        return jsonify({"error": "URL is required", "status": 2}), 400
    if not scraping_method:
        return jsonify({"error": "Scraping method is required", "status": 2}), 400

    if scraping_method == "requests":
        # call the scrape website func for the scraped result
        scrape_result = scrape_with_requests(url)
    elif scraping_method == "bs4":
        # call the scrape website func for the scraped result
        scrape_result = scrape_with_bs4(url)
    else:
        return jsonify({"error": "Invalid scraping method", "status": 2}), 400

    scraped_data_to_txt_file(scrape_result)
    if current_user.is_authenticated:
        store_user_history(url, scraping_method, scrape_result, current_user.id)
    return (
        jsonify(
            {
                "message": f"URL Scraped with {scraping_method} and content saved",
                "scrape_result": scrape_result,
>>>>>>> origin/signup_login_ali
            }
        ),
        201,
    )


@app.route("/download/txt", methods=["GET"])
def download_txt():
    """
    Endpoint to download a text file.

    This route handles GET requests to download a text file generated by the
    get_txt_file function.

    Returns:
        Response: A Flask response object containing the text file.
    """
    txt_file = get_txt_file()
    return txt_file


<<<<<<< HEAD
if __name__ == "__main__":
    with app.app_context():
       # db.create_all()

        app.run(debug=True)

# def url_to_db(url):
#     url: str = Url(url=url)
#     try:
#         db.session.add(url)
#         db.session.commit()
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

#     return jsonify({"message": "URL stored successfully to database"}), 201


# @app.route("/api/urls", methods=["GET"])
# def get_urls():
#     urls = Url.query.all()
#     json_urls = [url.to_json() for url in urls]

#     return jsonify(json_urls)


# @app.route("/api/remove_url/<int:id>", methods=["DELETE"])
# def remove_url(id: int):
#     url = Url.query.get(id)

#     if not url:
#         return jsonify({"error": "URL not found"}), 404

#     db.session.delete(url)
#     db.session.commit()

#     return jsonify({"message": "URL removed successfully"})
=======
@app.route("/login", methods=["GET"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            return jsonify({"message": "Logged in successfully!"})
        else:
            return jsonify({"error": "Incorrect password, try again."})
    else:
        return jsonify({"error": "Email does not exist."})


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"Message": "Logged out successfully."})


@app.route("/sign-up", methods=["POST"])
def sign_up():
    email = request.json.get("email")
    first_name = request.json.get("firstName")
    password1 = request.json.get("password1")
    password2 = request.json.get("password2")

    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"error": "Email already exists."})
    elif len(email) < 4:
        return jsonify({"error": "Email must be greater than 3 characters."})
    elif len(first_name) < 2:
        return jsonify({"error": "First name must be greater than 1 character."})
    elif password1 != password2:
        return jsonify({"error": "Passwords don't match."})
    elif len(password1) < 7:
        return jsonify({"error": "Password must be at least 7 characters."})
    else:
        new_user = User(
            email=email,
            first_name=first_name,
            password=generate_password_hash(password1, method="pbkdf2:sha256"),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        return jsonify({"message": "Account created successfully!"})


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/history", methods=["GET"])
@login_required
def history():
    user_history = (
        History.query.filter_by(user_id=current_user.id)
        .order_by(History.date.desc())
        .all()
    )

    history_list = [
        {
            "url": record.url,
            "scraped_data": record.content,
            "date": record.date.strftime("%Y-%m-%d %H:%M:%S") if record.date else None,
        }
        for record in user_history
    ]

    return jsonify(history_list), 200


if __name__ == "__main__":
    with app.app_context():
        if not path.exists("instance/" + str(os.getenv("DATABASE_NAME"))):
            db.create_all()
            print("Database created!")
        app.run(debug=True)
>>>>>>> origin/signup_login_ali
