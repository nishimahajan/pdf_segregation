import streamlit as st
import os
import shutil

def segregate_files(folder_path, output_folder):
  """
  Segregates files based on PAN and quarter_year information in the filename.

  Args:
      folder_path: Path to the folder containing the files.
      output_folder: Path to the folder where segregated files will be stored.

  Returns:
      A list of missing PDFs (if any).
  """
  missing_pdf = []
  for filename in os.listdir(folder_path):
    pan = filename[:10]
    quarter_year = filename[11:21]

    mid_folder = os.path.join(output_folder, quarter_year)
    os.makedirs(mid_folder, exist_ok=True)
    label_folder = os.path.join(mid_folder, pan)
    os.makedirs(label_folder, exist_ok=True)

    pdf = os.path.join(folder_path, filename)
    destination_path = os.path.join(label_folder, filename)

    if not os.path.exists(pdf):
      missing_pdf.append(pdf)
      continue

    shutil.copy(pdf, destination_path)
  return missing_pdf

def main():
  """
  Streamlit app for file segregation.
  """
  st.title("File Segregation App")

  folder_path = st.text_input("Enter folder path containing files:")
  output_folder = st.text_input("Enter output folder path:")

  if st.button("Segregate Files"):
    if not folder_path or not output_folder:
      st.error("Please enter both folder paths.")
      return
    missing_pdf = segregate_files(folder_path, output_folder)
    if missing_pdf:
      st.error(f"The following PDFs were not found: {missing_pdf}")
    else:
      st.success("Data sorted and organized into folders.")

if __name__ == "__main__":
  main()
