

 Cross Platform Application Launcher

Table of Contents
- Introduction
- Features
- Requirements
- Installation
- Usage
- Project Structure
- License

 Introduction
The Cross Platform Application Launcher is a web-based application that allows users to add, launch, and manage applications from a centralized interface. The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. It is designed to be accessible from various devices, including Windows, Mac, Android, and iPhone.

 Features
- Add Applications: Users can add applications by specifying the path and parameters.
- Launch Applications: Users can launch applications directly from the web interface.
- Edit/Delete Applications: Users can manage (edit/delete) applications through a settings page.
- Dynamic Icons: Application icons are dynamically fetched and displayed.
- Responsive Design: The interface is designed to be responsive and accessible from different devices.

 Requirements
- Python 3.x
- Flask
- HTML, CSS, JavaScript knowledge

 Installation
1. Clone the Repository:
  
   git clone https://github.com/KCDeeksha/application-launcher.git
   cd application-launcher

2. Create a Virtual Environment:

   python -m venv venv
   source venv/bin/activate   
   On Windows: venv\Scripts\activate
 

3. Install Dependencies:

   pip install Flask
   

4. Set Up Flask Environment:
   
   export FLASK_APP=app.py              On Windows: set FLASK_APP=app.py
   export FLASK_ENV=development    On Windows: set FLASK_ENV=development
   

5. Run the Application:
 
   flask run
  

6. Access the Application:
   Open your web browser and navigate to `http://localhost:2354`.

 Usage
1. Home Page:
   - View the list of added applications.
   - Click on the "Launch" button under an application to start it.

2. Settings Page:
   - Click on the "Settings" icon to navigate to the settings page.
   - Add a new application by entering the path and parameters in the provided form.
   - Edit or delete existing applications by clicking the respective buttons.

 Project Structure

application-launcher/
├── static/
          ├── images/
          ├── bg.jpg
          └── opezee.png (etc images)
├── templates/
│   ├── index.html
│   └── settings.html
├── app.py
├── applications.json
└── README.md
```

- static Contains static files like images.
- templates: Contains HTML templates for the Flask application.
- app.py: The main Flask application file.
- applications.json: Stores the application data.



