from orchestrator import run_scan

if __name__ == "__main__":
    result = run_scan("https://juice-shop.herokuapp.com")
    print("\n=== FINAL RESULT ===")
    print(result)
