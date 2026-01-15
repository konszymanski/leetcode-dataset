import requests
import re
import pandas as pd
import json
import os
import time

CSV_FILE = "leetcode_problems.csv"
IFRAMES_FILE = "iframes.json"
BASE_DIR = "official_solutions"

GET_OFFICIAL_SOLUTION = """
query officialSolution($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    solution {
      id
      title
      content
      contentTypeId
      paidOnly
      hasVideoSolution
      canSeeDetail
    }
  }
}
"""


def get_official_solution(slug, cookies=None):
    url = "https://leetcode.com/graphql"

    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{slug}/solution/",
        "User-Agent": "Mozilla/5.0",
    }

    variables = {"titleSlug": slug}

    try:
        response = requests.post(
            url,
            json={"query": GET_OFFICIAL_SOLUTION, "variables": variables},
            headers=headers,
            cookies=cookies,
        )
        data = response.json()
        solution_data = data.get("data", {}).get("question", {}).get("solution", {})

        if not solution_data:
            return None

        if not solution_data.get("canSeeDetail"):
            print(f"Refused: Official solution for {slug} is locked (Premium).")
            return None

        return solution_data.get("content")
    except Exception as e:
        print(f"Error fetching official solution: {e}")
        return None


FETCH_PLAYGROUND = """
query fetchPlayground($uuid: String!) {
  allPlaygroundCodes(uuid: $uuid) {
    code
    langSlug
  }
}
"""

def extract_code_from_playground(playground_url):
    uuid = playground_url.split("/")[-2]
    url = "https://leetcode.com/graphql"

    # Headers are important to avoid being blocked
    headers = {
        "Content-Type": "application/json",
        "Referer": playground_url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }

    payload = {"query": FETCH_PLAYGROUND, "variables": {"uuid": uuid}}

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        # A playground can contain multiple languages (C++, Java, Python)
        all_codes = data.get("data", {}).get("allPlaygroundCodes", [])

        # Filter for Python
        python_snippets = [
            item["code"]
            for item in all_codes
            if item["langSlug"] in ["python", "python3"]
        ]

        return python_snippets
    except Exception as e:
        print(f"Error fetching playground {uuid}: {e}")
        return []


def extract_official_solutions_iframes(content):
    pattern = (
        r'<iframe\ssrc="(https:\/\/leetcode.com\/playground\/[^"]*)"[^<]*><\/iframe>'
    )
    return re.findall(pattern, content, flags=re.DOTALL)


def get_all_iframes():
    df = pd.read_csv(CSV_FILE)
    free_problems_df = df[df["paidOnly"].astype(str).str.lower() == "false"]
    free_problems_with_solution_df = free_problems_df[
        free_problems_df["hasSolution"].astype(str).str.lower() == "true"
    ]
    slugs = free_problems_with_solution_df["titleSlug"].dropna().tolist()
    ids = free_problems_with_solution_df["frontendQuestionId"].dropna().tolist()

    print(f"Loaded {len(slugs)} free slugs with official solution from {CSV_FILE}.")

    for id, slug in zip(ids, slugs):
        print(f"Processing {id} {slug}...")
        official_content = get_official_solution(slug)
        if official_content:
            iframes = extract_official_solutions_iframes(official_content)
            new_data = {"id": id, "slug": slug, "iframes": iframes}
            with open(IFRAMES_FILE, "r+") as f:
                file_data = json.load(f)
                file_data["iframes"].append(new_data)
                f.seek(0)
                json.dump(file_data, f, indent=4)


def get_all_python_snippets():
    with open(IFRAMES_FILE, "r+") as f:
        file_data = json.load(f)
        for item in file_data["iframes"]:
            trailing_zeros = '0'*(4-(len(str(item['id']))))
            dir_name = f"{trailing_zeros}{item['id']}-{item['slug']}"
            print(dir_name)
            problem_dir = os.path.join(BASE_DIR, "python", dir_name)
            if not os.path.exists(problem_dir):
                os.makedirs(problem_dir)
            
            for i, iframe in enumerate(item['iframes'], 1):
                print(f"Extracting from {iframe}...")
                snippets = extract_code_from_playground(iframe)

                if len(snippets) == 0:
                    print("😔 No snippets in iframe")
                    continue
                if len(snippets) > 1:
                    print(f"🫢 More than one snippets for iframe {iframe}")
                
                file_path = os.path.join(problem_dir, f"solution_{i}.py")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(snippets[0])
                    
                time.sleep(1) # Be nice to the API

if __name__ == "__main__":
    # get_all_iframes()
    get_all_python_snippets()
