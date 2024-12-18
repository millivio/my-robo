# Robot Spare Bin Bot

This bot automates the process of logging into RobotSpareBinIndustries, extracting sales data from an Excel file, submitting the data via a web form, and exporting the results as a PDF.

## **Solution Design**

## **State Transition Model**
![image](https://github.com/user-attachments/assets/b3445fba-4206-4bce-986b-b97e8c5155c3)

The process follows a structured state transition model similar to the UiPath Reframework. Each state represents a distinct phase in the automation process. The key states are as follows:

1. **Initialization**
   - Load configuration and credentials from `config.json`.
   - Configure browser settings and logging.
   - Open the RobotSpareBin website.

2. **Login**
   - Logs in using the username and password from `config.json`.
   - Handles login failures and exits gracefully if credentials are incorrect.

3. **Data Collection**
   - Downloads an Excel file containing sales data from the website.

4. **Data Processing**
   - Reads the data from the Excel file.
   - Submits each row from the Excel file to the web form on the website.

5. **Summary and Export**
   - Captures a screenshot of the results page.
   - Exports the results as a PDF file.

6. **Logout**
   - Logs out from the platform.

---

## **Design Justification**

- **State Transition Model**: This model allows for clear state separation and error handling.
- **Modularity**: Each phase has a dedicated function, promoting code reusability and easier maintenance.
- **Credential Management**: Uses a secure `config.json` file to avoid hardcoding sensitive information.
- **Error Handling**: Errors in each state are caught and logged without causing a complete process failure.

---

## **Features**

- **Logging**: Logs every key step and error for debugging and monitoring.
- **Credential Management**: Loads login credentials from `config.json`.
- **Data Handling**: Processes data from an Excel file and submits it via a web form.
- **File Export**: Exports the results as a PDF file.

---

## **Setup Instructions**

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the bot**
   ```bash
   python task.py
   ```

---

## **Error Handling**

- **Missing Credentials**: If `config.json` is missing or does not contain the required keys, the bot will exit with a clear error message.
- **Login Failure**: If the login fails, the bot logs the error and exits.
- **Data Processing Issues**: Any issues while processing individual sales entries will be logged and the bot will move on to the next row.
- **File Download Errors**: If the Excel file cannot be downloaded, the process will be logged and halted.

---

## **File Structure**
```
.

├── config.json         # Credentials file 
├── task.py             # Main bot logic
├── LICENSE             # License file for the repository
├── conda.yaml          # Dependency management for the project environment
├── robo.yaml           # Robot configuration file for Robocorp tools
├── SalesData.xlsx      # Sample sales data file for testing
├── README.md           # This readme file
├──  requirements.txt   # Required Python dependencies
└── robot_spare_bin.log #log file for the robot
```

---

## **Technologies Used**

- **Python**: Main programming language.
- **Robocorp Libraries**: Used for browser automation, Excel handling, and PDF creation.
- **Logging**: Built-in logging for tracking execution and debugging.

---

## **Improvements**
- **Retry Logic**: Implement retry logic for network-based operations (e.g., login, file downloads).
- **Dynamic Credential Management**: Use environment variables or a secure secrets manager.
- **Error Recovery**: Add the ability to resume from a specific state if an error occurs.
- **Comprehensive Tests**: Add unit tests to ensure that each function works as expected.

---

## **License**
This project is licensed under the terms of the [LICENSE](LICENSE) file. Click the link to view the full license terms.

---

## **Contact**
For questions or suggestions, please create an issue or submit a pull request in the GitHub repository.
