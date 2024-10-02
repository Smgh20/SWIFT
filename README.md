# SWIFT Autonomous Tool-Carrying Robot

## Project Overview
The **SWIFT Autonomous Tool-Carrying Robot** is designed to minimize the repetitive movements of technicians during industrial maintenance tasks. The robot uses artificial intelligence and machine learning algorithms to optimize the pathfinding process, detect tools, and communicate with operators through a web-based interface. This project aims to reduce downtime in industrial production lines by delivering tools efficiently.

## Features
- **Tool Detection System**: Uses a convolutional neural network (CNN) to classify and detect mechanical tools with a high degree of accuracy.
- **Pathfinding Algorithms**: Implements the **RRT** and **A*** algorithms to determine the optimal path in a simulated industrial environment.
- **Communication System**: A web-based interface built with **Streamlit** allows operators to request tools and monitor the robot’s progress in real-time.
- **Simulation**: The robot's behavior is simulated in **Webots**, an open-source robotics simulator, to test its performance in avoiding obstacles and reaching the target.

## Technologies Used
- **TensorFlow/Keras**: For tool detection and classification.
- **Python**: Main programming language for the project.
- **Pygame**: Used to visualize the pathfinding algorithms.
- **Streamlit**: For building the user interface and web-based communication system.
- **Webots**: For simulating the robot’s behavior in a virtual environment.
## Project Architecture

### Tool Detection System:
- Built using a CNN model (Keras Sequential) with layers of convolution and pooling to classify mechanical tools.
- Overfitting is managed with data augmentation techniques like rotation and flipping.

### Pathfinding System:
- **Rapidly-exploring Random Tree (RRT)**: For dynamically calculating the path.
- **A*** algorithm: For finding the shortest and most optimal path to the destination.

### Communication System:
- A web interface built using **Streamlit** allows operators to request tools and view the robot’s real-time status and movement.

### Simulation:
- The robot is simulated in **Webots**, where it navigates around obstacles and retrieves tools based on operator requests.

## Future Work
- Enhance the tool detection model by adding more tool categories.
- Implement real-time feedback from the robot to adjust its pathfinding dynamically.
- Integrate more advanced obstacle detection sensors.
- Test the system in a real-world industrial setting.
