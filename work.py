import parser
import pandas as pd

def main():
    books_data = parser.parser()
    if books_data and len(books_data) > 0:
        df = pd.DataFrame(books_data)
        output_file = "Lab1_Variant10_Result.xlsx"
        df.to_excel(output_file, index=False)

if __name__ == "__main__":
    main()