import pandas as pd 
from fpdf import FPDF 
import os 

# 1. Load Data
def load_data(file_path): 
    # Fallback logic: Create test data if the file does not exist
    if not os.path.exists(file_path): 
        print(f"Notice: '{file_path}' not found. Generating dummy data...") 
        df = pd.DataFrame({ 
            'Department': ['Sales', 'IT', 'Marketing'], 
            'Expenses_EUR': [4500, 8200, 3100], 
            'Active_Lines': [12, 45, 8] 
        }) 
        df.to_excel(file_path, index=False) 
        
    return pd.read_excel(file_path) 

# 2. Analyze Data
def analyze_data(df): 
    # Generate a statistical summary of the dataframe
    summary = df.describe() 
    return summary 

# 3. Generate PDF Report
def create_report(summary_text): 
    pdf = FPDF() 
    pdf.add_page() 
    pdf.set_font("Arial", size=12) 
    pdf.cell(200, 10, txt="Automated Business Report", ln=True, align='C') 
    
    # Insert summary text
    pdf.set_font("Arial", size=10) 
    pdf.multi_cell(0, 10, txt=str(summary_text)) 
    pdf.output("Business_Report.pdf") 

# ========================================== 
# Main Execution Block
# ========================================== 
if __name__ == "__main__": 
    print("Starting report generation process...") 
    file_name = "test_database.xlsx" 
    
    # 1. Load data 
    data = load_data(file_name) 
    
    # 2. Analyze data 
    analysis_result = analyze_data(data) 
    
    # 3. Render PDF 
    create_report(analysis_result) 
    
    print("Success: 'Business_Report.pdf' has been generated.")
