import os
import sys

def main():
    param1 = os.getenv('PARAM1')
    param2 = os.getenv('PARAM2')
    
    if not param1 or not param2:
        print("Environment variables PARAM1 and PARAM2 must be set.")
        sys.exit(1)
    
    print(f"Received parameters: {param1} and {param2}")
    
    # Sample logic based on parameters
    if param1 == "greet" and param2:
        print(f"Hello, {param2}!")
    else:
        print(f"Unrecognized parameters: {param1}, {param2}")

if __name__ == "__main__":
    main()
