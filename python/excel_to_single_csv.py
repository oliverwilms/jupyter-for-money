import pandas as pd
import os
import sys

def excel_to_single_csv(excel_path, csv_path):
    try:
        # Validate file existence
        if not os.path.isfile(excel_path):
            raise FileNotFoundError(f"File not found: {excel_path}")
        
        # Load Excel file
        xls = pd.ExcelFile(excel_path)
        
        if not xls.sheet_names:
            raise ValueError("The Excel file contains no sheets.")
        
        all_sheets = []
        
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            
            # Optional: Add a column to track the sheet name
            df["__sheet_name__"] = sheet
            
            all_sheets.append(df)
        
        # Merge all sheets into one DataFrame
        merged_df = pd.concat(all_sheets, ignore_index=True)
        
        # Save to CSV
        merged_df.to_csv(csv_path, index=False)
        print(f"✅ Successfully saved merged CSV to: {csv_path}")
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    excel_file = "workbook.xlsx"  # Replace with your file path
    output_csv = "merged.csv"     # Output CSV path
    excel_to_single_csv(excel_file, output_csv)
