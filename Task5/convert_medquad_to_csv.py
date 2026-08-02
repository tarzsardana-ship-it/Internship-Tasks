import os
import xml.etree.ElementTree as ET
import pandas as pd

DATASET_PATH = "Task3/MedQuAD-master"

data = []

for root, dirs, files in os.walk(DATASET_PATH):
    for file in files:
        if file.endswith(".xml"):
            file_path = os.path.join(root, file)

            try:
                tree = ET.parse(file_path)
                xml_root = tree.getroot()

                qapairs = xml_root.find("QAPairs")

                if qapairs is not None:
                    for qa in qapairs.findall("QAPair"):

                        question = qa.find("Question")
                        answer = qa.find("Answer")

                        if question is not None and answer is not None:

                            q_text = question.text.strip() if question.text else ""
                            a_text = answer.text.strip() if answer.text else ""

                            if q_text and a_text:
                                data.append({
                                    "prompt": q_text,
                                    "response": a_text
                                })

            except Exception as e:
                print(f"Error in {file_path}")
                print(e)

df = pd.DataFrame(data)

df.to_csv("medical_dataset.csv", index=False, encoding="utf-8")

print("="*50)
print(f"Total Question-Answer pairs: {len(df)}")
print("medical_dataset.csv created successfully!")
print("="*50)