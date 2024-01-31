
Project 1: GPA Calculator 
● Getting started with Flask 
● HTML and CSS refresher (in Flask) 
● HTML form elements 
● HTTP requests (GET and POST) 
● Back-end data handling with Jinja 
● Rendering templates with arguments 
● Server logic with Jinja statements  


## Basics

### Front-End 
- Basically what "designing" what you can see
- HTML (HyperText Markup Language): It is the standard markup language for documents designed to be displayed in a web browser. HTML can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.
Example of most basic structure of HTML documents:
    ```
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your Title Here</title>
    </head>
    <body>
        <!-- Your HTML content goes here -->
    </body>
    </html>
    ```
Let's break down each part:

<!DOCTYPE html>: This declaration defines the document type and version of HTML. It helps browsers to render the document correctly.

<html lang="en">: The root element of an HTML page. The lang attribute specifies the language of the document, typically set to "en" for English.

<head>: Contains meta-information about the HTML document, such as character set, viewport settings, and the document title.

<meta charset="UTF-8">: Specifies the character encoding for the document (UTF-8 is widely used for internationalization).To display an HTML page correctly, a web browser must know which character set (character encoding) to  use. ASCII was limited so generally today, we use UTF-8

<meta name="viewport" content="width=device-width, initial-scale=1.0">: Sets the viewport properties, ensuring proper scaling on various devices.

<title>Your Title Here</title>: Defines the title of the HTML document, which appears in the browser's title bar or tab.

<body>: Contains the main content of the HTML document, such as text, images, links, forms, and other elements.


- CSS (Cascading Style Sheets): It is a style sheet language used for describing the look and formatting of a document written in HTML. It enables separation of content and presentation.

### Back-End
- Usually used to control the logic of the applications
Routing:
- In the context of web development, routing refers to the mechanism by which an application's endpoints (URLs) respond to client requests. In Flask, routing is achieved using decorators that map URL patterns to specific Python functions.


HTTP Requests and Response
Request:

Explanation: A request is a message sent by a client (typically a web browser) to a server, asking it to perform a certain action or provide specific information.
Example: When you type a URL in your browser and press Enter, your browser sends a request to the server associated with that URL, asking for the webpage's content.
Response:

Explanation: A response is a message sent by a server to a client in reply to its request. It contains the requested information or indicates the success/failure of the requested action.
Example: After receiving your request for a webpage, the server sends back a response containing the HTML, CSS, and other resources needed to display the webpage.
Client:

Explanation: A client is a device or software application that initiates communication by sending requests to a server. In the context of the web, a client is often a web browser, mobile app, or other user-facing software.
Example: Your web browser (like Chrome, Firefox, or Safari) is a client. When you visit a website, the browser acts as a client by sending requests to the server hosting the site.
Server:

Explanation: A server is a computer or software application that processes requests from clients and provides responses. Servers host websites, applications, or services and handle tasks like data storage, processing, and serving content to clients.
Example: The computer hosting a website is a server. It receives requests from clients (web browsers) and responds by sending the requested content (webpages, images, etc.).
**HTTP Methods: GET and POST**

**GET Method:**
- **Purpose:** Retrieve data from a specified resource.
- **Parameters:** Sent in the URL as query parameters.
- **Idempotent:** Making the same request produces the same result.

**Example GET Request:**
```http
GET /articles?id=123 HTTP/1.1
Host: example.com
```

**POST Method:**
- **Purpose:** Submit data to a specified resource.
- **Parameters:** Sent in the body of the request.
- **Not Idempotent:** Making the same request may result in different outcomes.

**Example POST Request:**
```http
POST /submit-form HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=johndoe&password=secretpass
```

**When to Use Each:**
- **GET:** Safe, idempotent, suitable for data retrieval.
- **POST:** Involves data submission, may cause side effects on the server.



#### Project Structure
GPACalculator/
|-- venv/            # Virtual environment
|-- server.py        # Main Python file to run the server
|-- templates/       # HTML templates
|   |-- index.html   # Main HTML file
|-- static/          # Static files (CSS, images, etc.)
|   |-- style.css    # CSS file

#### Steps
1. Install virtual environment and activate it 
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install Flask
```
pip install Flask
```

3. Create folders as per project structure and write the code logic

4. To run the app
```
python3 server.py
```