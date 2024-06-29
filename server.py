from flask import Flask, request, render_template, jsonify
import os
import json
import logging
import webbrowser

app = Flask(__name__, static_url_path='/static')

# Enable logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Store the list of applications and their parameters
applications = []

# Load applications from file
def load_applications():
    global applications
    if os.path.exists('applications.json'):
        with open('applications.json', 'r') as f:
            applications = json.load(f)

# Save applications to file
def save_applications():
    with open('applications.json', 'w') as f:
        json.dump(applications, f)

# Initial load of applications
load_applications()

# Function to fetch icon URL based on parameter
def fetch_icon_url(param):
    if param == 'google.com':
        return 'https://www.google.com/favicon.ico'
    elif param == 'youtube.com':
        return 'https://www.youtube.com/favicon.ico'
    elif param == 'facebook.com':
        return 'https://www.facebook.com/favicon.ico'
    elif param == 'twitter.com':
        return 'https://www.twitter.com/favicon.ico'
    elif param == 'instagram.com':
        return 'https://www.instagram.com/favicon.ico'
    elif param == 'linkedin.com':
        return 'https://www.linkedin.com/favicon.ico'
    elif param == 'github.com':
        return '/static/gh.png'
    elif param == 'amazon.com':
        return 'https://www.amazon.com/favicon.ico'
    elif param == 'stackoverflow.com':
        return 'https://www.stackoverflow.com/favicon.ico'
    else:
        return '/static/default_icon.jpg'

@app.route('/')
def index():
    return render_template('index.html', applications=applications)

@app.route('/settings')
def settings():
    return render_template('settings.html', applications=applications)

@app.route('/add', methods=['POST'])
def add_application():
    app_path = request.form['app_path']
    app_param = request.form['app_param']
    icon_url = fetch_icon_url(app_param)  # Fetch icon URL based on parameter

    applications.append({'path': app_path, 'param': app_param, 'icon_url': icon_url})
    save_applications()
    logging.info(f"Added application: {app_path} with parameter: {app_param}")
    return jsonify(success=True)

@app.route('/launch', methods=['POST'])
def launch_application():
    app_param = request.form['app_param']
    try:
        webbrowser.open_new_tab(f'http://{app_param}')
        return jsonify(success=True)
    except Exception as e:
        logging.error(f"Failed to launch application: {e}")
        return jsonify(success=False, error=str(e))

@app.route('/delete', methods=['POST'])
def delete_application():
    index = int(request.form['index'])
    if 0 <= index < len(applications):
        app = applications.pop(index)
        save_applications()
        logging.info(f"Deleted application: {app['path']} with parameter: {app['param']}")
        return jsonify(success=True)
    else:
        logging.error("Invalid index for deletion")
        return jsonify(success=False, error="Invalid index")

@app.route('/edit', methods=['POST'])
def edit_application():
    index = int(request.form['index'])
    new_path = request.form['new_path']
    new_param = request.form['new_param']
    if 0 <= index < len(applications):
        applications[index] = {'path': new_path, 'param': new_param}
        save_applications()
        logging.info(f"Edited application at index {index}: new path: {new_path}, new param: {new_param}")
        return jsonify(success=True)
    else:
        logging.error("Invalid index for editing")
        return jsonify(success=False, error="Invalid index")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2354)
