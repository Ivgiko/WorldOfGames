# WorldOfGames Project

## Overview
This project provides a Docker setup for a Python-based web application with Selenium tests. Due to the unavailability of a pre-built Docker image with both Python and Selenium prerequisites, custom configurations were necessary.

## Docker Configuration
As no suitable Docker image with both Python and Selenium prerequisites was available, the Docker setup includes:

- **Dockerfile**: Configured to install Google Chrome and ChromeDriver as Selenium prerequisites. This ensures that Selenium tests can run correctly within the Docker container.

- **e2e.py Script**: Contains the end-to-end test logic using Selenium. The script is set up to work with the Chrome browser and includes options necessary for running Selenium in a Docker environment.

- **requirements.txt**: Lists the required Python packages, including Selenium and `webdriver-manager`, to ensure all dependencies are installed inside the Docker container.

## Repository Information
- **GitHub Repository**: [Public Repository](https://github.com/Ivgiko/WorldOfGames)  
  No special configurations are required for accessing the repository.

- **DockerHub Repository**: [Public Repository](https://hub.docker.com/repository/docker/ivgiko/worldofgames4-web/general)  
  While the repository is public, pushing images requires authentication. A long-term access token is used inside Jenkins file for authentication to simplify access without sharing passwords.

## Jenkins Pipeline
The Jenkins pipeline is configured to run on both Windows and macOS/Linux environments. You will need to uncomment the relevant section for your operating system:

1. **Checkout Repository**: Clones the GitHub repository.

2. **Build and Run Docker Container**: Builds and runs the Docker container in detached mode.

3. **Test with e2e.py**: Executes the `e2e.py` script to run Selenium tests.

4. **Push to DockerHub**: Tags and pushes the Docker image to DockerHub. Authentication is handled using the provided access token.

5. **Clean Up**: Shuts down the Docker container and cleans up resources.

**Note:** Ensure you uncomment either the Windows or macOS/Linux section in the Jenkins file depending on your operating system.

## Additional Notes
- **Scores.txt**: Since the file is already in the image, I didnt understand what the purpose of mounting it would be, so I skipped that step.

