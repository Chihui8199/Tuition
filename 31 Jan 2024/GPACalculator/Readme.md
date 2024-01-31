# Project 1: GPA Calculator

## Introduction
This project focuses on building a GPA Calculator using Flask, a web framework for Python. The development process covers essential concepts, including front-end (HTML, CSS), back-end (Flask), routing, and handling HTTP requests.

## Basics

### Front-End
Front-end involves designing what users see and interact with on a website.

#### HTML (HyperText Markup Language)
HTML is the standard markup language for web documents. It structures content and works in conjunction with CSS and JavaScript.

Example of a basic HTML document structure:
```html
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

#### CSS (Cascading Style Sheets)
CSS is a style sheet language that enhances the presentation of HTML documents.

### Back-End
Back-end controls the logic of applications.

#### Routing
Routing maps URL patterns to specific Python functions. In Flask, decorators facilitate routing.

#### HTTP Requests and Response
- **Request:** A message from a client to a server, asking for an action or information.
- **Response:** A message from a server to a client, containing requested information or indicating success/failure.

#### HTTP Methods: GET and POST
- **GET Method:**
  - Purpose: Retrieve data from a specified resource.
  - Parameters: Sent in the URL as query parameters.
  - Idempotent: Making the same request produces the same result.

  Example GET Request:
  ```http
  GET /articles?id=123 HTTP/1.1
  Host: example.com
  ```

- **POST Method:**
  - Purpose: Submit data to a specified resource.
  - Parameters: Sent in the body of the request.
  - Not Idempotent: Making the same request may result in different outcomes.

  Example POST Request:
  ```http
  POST /submit-form HTTP/1.1
  Host: example.com
  Content-Type: application/x-www-form-urlencoded

  username=johndoe&password=secretpass
  ```

  When to Use Each:
  - **GET:** Safe, idempotent, suitable for data retrieval.
  - **POST:** Involves data submission, may cause side effects on the server.

## Project Structure
```
GPACalculator/
|-- venv/            # Virtual environment
|-- server.py        # Main Python file to run the server
|-- templates/       # HTML templates
|   |-- index.html   # Main HTML file
|-- static/          # Static files (CSS, images, etc.)
|   |-- style.css    # CSS file
```

## Getting Started
1. Install virtual environment and activate it
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install Flask
   ```
   pip install Flask
   ```

3. Create folders as per the project structure and implement the code logic.

4. To run the app
   ```
   python3 server.py
   ```