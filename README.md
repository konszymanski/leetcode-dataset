# Investigating Code Similarity Patterns in LLM-Generated and Human-Written Programming Solutions - CSEDU 2026

This repository contains the dataset and analysis scripts for the research paper: **"Investigating Code Similarity Patterns in LLM-Generated and Human-Written Programming Solutions"**. The paper was accepted to the 18th International Conference on Computer Supported Education (CSEDU 2026) in Benidorm, Spain (https://csedu.scitevents.org/Home.aspx).

---

### **Authors**
* Paulina Gacek
* Bartosz Gdowski
* Konrad Szymański
* Wojciech Żmuda

(*AGH University of Krakow, Faculty of Electrical Engineering, Automatics, IT and Biomedical Engineering*)

---
### **Original respository**

[https://github.com/sprawdzarka-aisd/plagiarism-detection-tools-comparison](https://github.com/paulinagacek/leetcode-dataset)

---

### **Setup & Installation**

To set up the environment and replicate the analysis:

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### **Dataset Overview**
The dataset comprises **9,000 solutions** for **100 LeetCode Medium** algorithmic tasks, distributed as follows:
* **Human Solutions (5,000):** Collected from pre-2023 community submissions to ensure no AI contamination.
* **GPT-5.2 Solutions (2,000):** Generated via zero-shot prompting using OpenAI's GPT-5.2 (2026).
* **Gemini 3.0 Flash Solutions (2,000):** Generated using Google DeepMind's Gemini 3.0 Flash (2026).

Tasks cover diverse paradigms, including dynamic programming, graph traversal, and greedy algorithms.

---

### **Methodology**
The analysis evaluates code similarity across three primary dimensions:
1.  **Structural Similarity:** Computed using Jaccard overlap of **AST (Abstract Syntax Tree) subtree hashes** on normalized code.
2.  **Comment Analysis:** Lexical convergence of natural language documentation measured via **TF-IDF cosine similarity**.
3.  **Identifier Diversity:** Measurement of naming variability using **Shannon entropy** and cross-solution Jaccard overlap of user-defined identifiers.

---

### **Key Findings**
* **Structural Convergence:** LLM solutions occupy a highly concentrated region of the solution space. Intra-group structural similarity for AI models exceeds **75%**, compared to only **28%** for human-written solutions.
* **Model-Specific Signatures:** AI models exhibit unique "fingerprints." GPT-5.2 tends toward sparse, structurally cloned outputs, while Gemini 3.0 Flash produces verbose, templated documentation.
* **Lexical Determinism:** LLMs demonstrate a constrained algorithmic vocabulary, frequently reusing identical identifier sets and commentary patterns across independent generations.
