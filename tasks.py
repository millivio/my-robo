from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP
from RPA.Excel.Files import Files
from RPA.PDF import PDF
import json
import logging

# Logging setup
logging.basicConfig(
    filename="robot_spare_bin.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and export it as a PDF"""
    try:
        browser.configure( slowmo=100,)
        open_the_intranet_website()
        log_in()
        download_excel_file()
        fill_form_with_excel_data()
        collect_results()
        export_as_pdf()
        log_out()    
    except Exception as e:
        logging.error(f"Unexpected error during execution: {e}")

def open_the_intranet_website():
    """Navigates to the given URL"""
    try:
        browser.goto("https://robotsparebinindustries.com/")
        logging.info("Website opened successfully.")
    except Exception as e:
        logging.error(f"Error opening website: {e}")

def read_credentials(file_path="config.json"):
    """Load credentials from the configuration file"""
    try:
        with open(file_path, 'r') as file:
            logging.info("Credentials loaded successfully.")
            return json.load(file)
    except Exception as e:
        logging.error(f"Failed to load credentials: {e}")
        sys.exit(1)

def log_in():
    """Logs in to the website using the credentials"""
    try:
        credentials = read_credentials()
        username = credentials.get("username")
        password = credentials.get("password")
        page = browser.page()
        page.fill("#username",username)
        page.fill("#password", password)
        page.click("button:text('Log in')")
        logging.info("Successfully logged in.")
    except Exception as e:
        logging.error(f"Login failed: {e}")

def fill_and_submit_sales_form(sales_rep):
    """Fills in the sales data and click the 'Submit' button"""
    try: 
        page = browser.page()
        page.fill("#firstname", sales_rep["First Name"])
        page.fill("#lastname", sales_rep["Last Name"])
        page.select_option("#salestarget", str(sales_rep["Sales Target"]))
        page.fill("#salesresult", str(sales_rep["Sales"]))
        page.click("text=Submit")
    except Exception as e:
        logging.error(f"Error submitting sales form for {sales_rep}: {e}")

def download_excel_file():
    """Downloads excel file from the given URL"""
    try:
        http = HTTP()
        http.download(url="https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)
        logging.info("Excel file downloaded successfully.")
    except Exception as e:
        logging.error(f"Failed to download Excel file: {e}")

def fill_form_with_excel_data():
    """Read data from excel and fill in the sales form"""
    try:
        excel = Files()
        excel.open_workbook("SalesData.xlsx")
        worksheet = excel.read_worksheet_as_table("data", header=True)
        excel.close_workbook()

        for row in worksheet:
            fill_and_submit_sales_form(row)
    except Exception as e:
        logging.error(f"Failed to process Excel data: {e}")

def collect_results():
    """Take a screenshot of the page"""
    try:
        page = browser.page()
        page.screenshot(path="output/sales_summary.png")
        logging.info("Screenshot saved successfully.")
    except Exception as e:
        logging.error(f"Failed to collect screenshot: {e}")

def export_as_pdf():
    """Export the data to a pdf file"""
    try:
        page = browser.page()
        sales_results_html = page.locator("#sales-results").inner_html()
        pdf = PDF()
        pdf.html_to_pdf(sales_results_html, "output/sales_results.pdf")
        logging.info("PDF exported successfully.")
    except Exception as e:
        logging.error(f"Failed to export PDF: {e}")

def log_out():
    """Presses the 'Log out' button"""
    try:
        page = browser.page()
        page.click("text=Log out")
        logging.info("Successfully logged out.")
    except Exception as e:
        logging.error(f"Logout failed: {e}")