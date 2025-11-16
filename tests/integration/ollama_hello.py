import ollama
import time

# Test Gemma 3 1B (Default Mode)
print("Testing Gemma 3 1B (Default Mode):")
start_time = time.time()
response = ollama.generate(model='gemma3:1b', prompt='Hello!')
end_time = time.time()
print(response['response'])
print(f"Response time: {end_time - start_time:.2f} seconds")

# Test Dolphin-Phi (Deep Think Mode)
print("\nTesting Dolphin-Phi (Deep Think Mode):")
start_time = time.time()
response = ollama.generate(model='dolphin-phi', prompt='Hello!')
end_time = time.time()
print(response['response'])
print(f"Response time: {end_time - start_time:.2f} seconds")