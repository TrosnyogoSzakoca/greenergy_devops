# Python Swapcase Web Application

Your task is to develop, qualify and pack a Python web application for deployment.
The application should expect POST requests with a parameter named 'string' and a
string-type value. Upon arrival, the application should return the same string with
swapped case as the body of the response ('abcDEF' would become 'ABCdef').
Errors should be handled appropriately by the application. The application should be
served using gunicorn.

## Installation and Running Locally

1. Clone this repository to your local machine.
2. Make sure you have Python and Docker installed on your system.

To run the application  with Docker:
```bash
./build_docker_image.sh
./start_app.sh
```

To test application:
```bash
pytest test_app.py
```

To remove application:
```bash
./stop_app.sh
```
