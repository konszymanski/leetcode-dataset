import requests
import pandas as pd
import os
import re
import time
from datetime import datetime
from pathlib import Path

class LeetCodeVoteScraper:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/"
        }
        self.output_dir = "human_medium"
        os.makedirs(self.output_dir, exist_ok=True)
        
        self.cutoff_date = datetime(2022, 11, 30, 23, 59, 59)
        
        self.failed_tasks = []

    def extract_python_code(self, content):
        if not content: return None
        content = content.replace('\\n', '\n').replace('\\t', '\t')
        
        patterns = [
            r'```(?:python3?|py)(.*?)\n(.*?)```',
            r'```\n(.*?)```',
            r'```(.*?)```'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                groups = match.groups()
                code = groups[-1] if len(groups) > 1 else groups[0]
                code = code.strip()
                code = code.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
                return code
        return None

    def run(self, title_slug, problem_id_str, target_count):
        folder_name = f"{problem_id_str}-{title_slug}"
        task_dir = os.path.join(self.output_dir, folder_name)

        if os.path.exists(task_dir):
            existing_files = [f for f in os.listdir(task_dir) if f.endswith('.txt')]
            if len(existing_files) >= target_count:
                print(f"--- Zadanie: [{problem_id_str}] {title_slug} - POMINIĘTO (gotowe: {len(existing_files)}) ---")
                return

        os.makedirs(task_dir, exist_ok=True)
        print(f"\n--- Zadanie: [{problem_id_str}] {title_slug} ---")

        self.headers["Referer"] = f"https://leetcode.com/problems/{title_slug}/solutions/"

        query = """
        query communitySolutions($questionSlug: String!, $skip: Int!, $first: Int!, $orderBy: TopicSortingOption, $languageTags: [String!]) {
          questionSolutions(
            filters: {questionSlug: $questionSlug, skip: $skip, first: $first, orderBy: $orderBy, languageTags: $languageTags}
          ) {
            solutions {
              id
              post {
                creationDate
                voteCount
                content
              }
            }
          }
        }
        """

        saved_count = 0
        skip = 0
        batch_size = 40
        
        error_occurred = False
        error_message = ""

        while saved_count < target_count and skip < 500:
            variables = {
                "questionSlug": title_slug,
                "skip": skip,
                "first": batch_size,
                "orderBy": "most_votes", 
                "languageTags": ["python", "python3"] 
            }

            try:
                r = self.session.post("https://leetcode.com/graphql", json={"query": query, "variables": variables}, headers=self.headers)
                data = r.json()
                
                if 'errors' in data:
                    print(f"  [!] Błąd GraphQL: {data['errors'][0]['message']}")
                    error_occurred = True
                    error_message = data['errors'][0]['message']
                    break
                    
                solutions_data = data.get('data', {}).get('questionSolutions', {})
                if not solutions_data:
                    break
                    
                solutions = solutions_data.get('solutions', [])
                if not solutions:
                    break 

                for sol in solutions:
                    if saved_count >= target_count:
                        break

                    post = sol.get('post')
                    if not post: continue

                    ts = post['creationDate']
                    creation_dt = datetime.fromtimestamp(ts)

                    if creation_dt > self.cutoff_date:
                        continue 

                    clean_code = self.extract_python_code(post['content'])

                    if clean_code and ("return" in clean_code or "class" in clean_code):
                        date_str = creation_dt.strftime('%Y-%m-%d')
                        filename = f"{problem_id_str}-{title_slug}-{date_str}_{saved_count + 1}.txt"
                        path = os.path.join(task_dir, filename)
                        
                        if not os.path.exists(path):
                            with open(path, "w", encoding="utf-8") as f:
                                f.write(clean_code)
                            saved_count += 1
                            print(f"  [OK] Zapisano: {filename}")

                skip += batch_size
                time.sleep(0.5) 

            except Exception as e:
                print(f"  [!] Błąd pętli: {e}")
                error_occurred = True
                error_message = str(e)
                break

        if error_occurred:
            self.failed_tasks.append(f"[{problem_id_str}] {title_slug} -> BŁĄD: {error_message}")
        
        elif saved_count == 0:
            print("  [INFO] Brak rozwiązań spełniających kryteria.")
            self.failed_tasks.append(f"[{problem_id_str}] {title_slug} -> BRAK ROZWIĄZAŃ (0 zapisanych)")
        
        elif saved_count < target_count:
            print(f"  [INFO] Znaleziono tylko {saved_count} z {target_count} rozwiązań.")
            self.failed_tasks.append(f"[{problem_id_str}] {title_slug} -> NIEKOMPLETNE ({saved_count}/{target_count})")

    def save_failed_report(self):
        if not self.failed_tasks:
            print("\n[SUKCES] Wszystkie zadania przetworzone poprawnie, brak uwag do raportowania.")
            return

        report_filename = "_scrapping_report.txt"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"Raport scrapowania z dnia {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            for item in self.failed_tasks:
                f.write(item + "\n")
        
        print(f"\n[INFO] Zapisano raport (błędy/braki) w pliku: {report_filename}")

if __name__ == "__main__":
    CSV_FILE = "leetcode_problems.csv"
    PROMTPS_DIR = Path("prompts")
    
    if not os.path.exists(CSV_FILE):
        print(f"Błąd: Nie znaleziono pliku {CSV_FILE}")
        exit()

    try:
        df = pd.read_csv(CSV_FILE)
        
        if "paidOnly" in df.columns:
            df = df[df["paidOnly"].astype(str).str.lower() == "false"]
        
        if "hasSolution" in df.columns:
            df = df[df["hasSolution"].astype(str).str.lower() == "true"]
        
        if "difficulty" in df.columns:
            df = df[df["difficulty"].astype(str).str.lower() == "medium"]
        
        slugs = df['titleSlug'].to_list()[150:200]
            
        print(f"Załadowano {len(slugs)} zadań do przetworzenia.")

        for idx, file_name in enumerate(sorted(os.listdir(PROMTPS_DIR))):
            slug = file_name[5:-4]
            if slug not in slugs:
                continue
        
            scraper = LeetCodeVoteScraper()

            try:
                question_id = file_name[:4]
                scraper.run(slug, question_id, target_count=50)
                
                time.sleep(1) 

            except Exception as e:
                print(f"!!! Błąd krytyczny przy przetwarzaniu wiersza {question_id}: {e}")
                scraper.failed_tasks.append(f"WIERSZ CSV {question_id} -> CRITICAL ERROR: {e}")
                continue
            
            scraper.save_failed_report()
                
    except Exception as e:
        print(f"Krytyczny błąd programu: {e}")