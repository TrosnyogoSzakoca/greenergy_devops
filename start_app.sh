#!/bin/bash

# Start the Docker instance
docker run -d -p 5000:5000 --name python_swapcase_webapp_instance python_swapcase_webapp
