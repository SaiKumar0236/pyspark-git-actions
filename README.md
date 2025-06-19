# PySpark GitHub Actions Example

This is a sample PySpark project demonstrating how to integrate GitHub Actions for CI/CD.

## Features
- A simple PySpark word count job.
- Unit tests for the PySpark job.
- GitHub Actions workflow for automated testing.

## How to Run Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2.Run the PySpark job:
   ```
   python src/word_count.py
   ```
3.Run tests:
   ```
   python -m unittest discover -s tests
   ```
GitHub Actions
The workflow (.github/workflows/ci.yml) runs tests automatically on every push or pull request to the main branch.


---

This project is simple yet effective for demonstrating PySpark development with GitHub Actions. You can expand it further by adding more complex PySpark jobs, integration tests, or deployment steps!
   
