import json
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FILE = os.path.join(
    BASE_DIR,
    "archive",
    "arxiv-metadata-oai-snapshot.json"
)

OUTPUT_FILE = os.path.join(
    BASE_DIR,
    "arxiv_dataset.csv"
)

MAX_PAPERS = 10000

count = 0
with open(INPUT_FILE, "r", encoding="utf-8") as infile, \
     open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:

    writer = csv.writer(outfile)

    writer.writerow([
        "title",
        "abstract",
        "authors",
        "categories",
        "published"
    ])

    for line in infile:

        try:
            paper = json.loads(line)
        except:
            continue

        categories = paper.get("categories", "")

        # Keep only Computer Science papers
        if not categories.startswith("cs."):
            continue

        title = paper.get("title", "").replace("\n", " ").strip()
        abstract = paper.get("abstract", "").replace("\n", " ").strip()
        authors = paper.get("authors", "")
        published = paper.get("update_date", "")

        writer.writerow([
            title,
            abstract,
            authors,
            categories,
            published
        ])

        count += 1

        if count % 500 == 0:
            print(f"{count} papers processed...")

        if count >= MAX_PAPERS:
            break

print("\nDone!")
print(f"Saved {count} Computer Science papers to {OUTPUT_FILE}")