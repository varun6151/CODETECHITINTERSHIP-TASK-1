# CODETECHITINTERSHIP-TASK-1
### NAME : SRINIVAS POTHARAJU
### COMPANY :CODETECH IT SOLUTIONS
### ID:CT08DS3454
### DOMAIN :MACHINE LEARNING
### DURATION : JULY TO AUGUST 2024
### MENTOR : Neela Santhosh Kumar 
# BMI Calculator

## Overview
![task-1bmiapp](https://github.com/user-attachments/assets/aa69eb75-da06-4ef4-8326-459391ed7d2e)


This project is a web-based application that calculates the Body Mass Index (BMI) of users based on their input for height and weight. The application provides users with an easy-to-use interface to determine their BMI and understand their weight classification (underweight, normal weight, overweight, or obese) based on standard BMI ranges.

## Objective

The primary objective of this project is to develop an intuitive and interactive BMI calculator that helps users understand their health status based on their BMI.

## Key Activities

### Frontend Development

- **Design and Implement the User Interface (UI)**: Create a user-friendly interface with an input form for weight and height. Design the interface to be responsive and visually appealing using HTML and CSS.
- **Form Handling and Validation**: Implement client-side form validation to ensure users enter valid and positive values for weight and height.
- **Display Results**: Show the calculated BMI and corresponding weight classification dynamically after the user submits the form.

### Backend Development

- **Set Up Flask Server**: Create a Flask application to handle HTTP requests.
- **API Endpoint for BMI Calculation**: Develop a RESTful API endpoint that receives weight and height, calculates BMI, and returns the result along with the weight classification.
- **Error Handling**: Implement error handling to manage invalid or negative inputs and return appropriate error messages.

### Integration

- **Connect Frontend to Backend**: Use JavaScript (Fetch API) to send user input from the frontend form to the backend API endpoint and retrieve the BMI result.
- **Dynamic Content Update**: Update the DOM to display the BMI result and classification to the user without reloading the page.

## Technologies Used

### Frontend

- **HTML5**: Structure the content and elements of the application.
- **CSS3**: Style the application for a visually appealing and responsive design.
- **JavaScript**: Handle form submissions, fetch API calls, and dynamically update the DOM with the results.

### Backend

- **Python**: Program the logic for BMI calculation and error handling.
- **Flask**: Create a lightweight web server to handle API requests and serve the HTML page.

### Additional Tools and Libraries

- **JSON**: Format data for API requests and responses.
- **Fetch API**: Make asynchronous HTTP requests from the frontend to the backend.

## Installation and Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/bmi-calculator.git
    cd bmi-calculator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    python app.py
    ```

5. Open your browser and go to `http://127.0.0.1:5000` to access the BMI Calculator.

## Usage

1. Enter your weight in kilograms.
2. Enter your height in meters.
3. Click the "Calculate BMI" button.
4. Your BMI and corresponding classification will be displayed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Thanks to the open-source community for providing valuable resources and tools.

---

Feel free to modify this README file to better fit your project's needs.

