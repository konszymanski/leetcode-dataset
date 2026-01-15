import requests
import re

def get_all_leetcode_slugs():
    # This endpoint returns the metadata for all problems in the 'all' category
    url = "https://leetcode.com/api/problems/all/"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://leetcode.com/problemset/all/"
    }

    print("Fetching problem list (this may take a few seconds)...")
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch: {response.status_code}")
        return []

    data = response.json()
    
    # The slugs are nested inside 'stat_status_pairs' -> 'stat' -> 'question__title_slug'
    slugs = [
        item["stat"]["question__title_slug"] 
        for item in data["stat_status_pairs"]
        if item["paid_only"] is False
    ]
    
    return slugs


GET_SOLUTIONS_LIST = """
query communitySolutions($questionSlug: String!, $orderBy: TopicSortingOption, $languageTags: [String!]) {
  questionSolutions(
    filters: {questionSlug: $questionSlug, skip: 0, first: 10, orderBy: $orderBy, languageTags: $languageTags}
  ) {
    solutions {
      id
      title
      solutionTags {
        name
      }
    }
  }
}
"""

GET_SOLUTION_CONTENT = """
query communitySolution($topicId: Int!) {
  topic(id: $topicId) {
    post {
      content
    }
  }
}
"""

def get_best_solution_content(title_slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{title_slug}/solutions/"
    }

    # Step 1: Get the ID of the #1 most upvoted solution
    list_vars = {
        "questionSlug": title_slug,
        "languageTags": ["Python3"],
        "orderBy": "most_votes",
    }
    
    list_res = requests.post(url, json={"query": GET_SOLUTIONS_LIST, "variables": list_vars}, headers=headers)
    solutions = list_res.json()["data"]["questionSolutions"]["solutions"]
    
    if not solutions:
        print("No solutions found.")
        return None, None

    # Loop through the solutions until we find one with Python code
    for sol in solutions:
        tags = [tag['name'] for tag in sol.get('solutionTags', [])]
        if 'Python3' in tags:
            top_solution_id = int(sol["id"])
            top_title = sol["title"]

            # Step 2: Get the content using the ID
            content_vars = {"topicId": top_solution_id}
            content_res = requests.post(url, json={"query": GET_SOLUTION_CONTENT, "variables": content_vars}, headers=headers)
            
            full_content = content_res.json()["data"]["topic"]["post"]["content"]
            
            return top_title, full_content


def extract_python_snippets(content):
    """
    Extracts content between ```Python3 [] and the next ```.
    """
    pattern = r"```Python3?\s\[\]\\n(.*?)\\n?```"
    
    snippets = re.findall(pattern, content, flags=re.DOTALL)
    return [code.strip() for code in snippets]


# # Execution
# all_slugs = get_all_leetcode_slugs()
# print(f"Total problems found: {len(all_slugs)}")

# for slug in all_slugs[:20]:
for slug in ["sort-integers-by-the-number-of-1-bits"]:
    title, content = get_best_solution_content(slug)
    if title is None:
        print(f"   ! Skip: No Python3 solutions found for {slug}")
        continue
    code_blocks = extract_python_snippets(content)

    print(f"--- TITLE: {title} ---")
    if code_blocks:
        for i, code in enumerate(code_blocks, 1):
            print(f"--- Snippet {i} ---")
            print(code)
            print("\n" + "="*30 + "\n")
    else:
        print("No Python code snippets found in the content.")