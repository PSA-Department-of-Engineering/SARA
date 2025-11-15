import ollama
import time

# Test Gemma 2 (Default Mode)
print("Testing Gemma 2 (Default Mode):")
start_time = time.time()
response = ollama.generate(model='gemma2:2b', prompt='Hello!')
end_time = time.time()
print(response['response'])
print(f"Response time: {end_time - start_time:.2f} seconds")

# Test Phi-3 Mini (Deep Think Mode)
print("\nTesting Phi-3 Mini (Deep Think Mode):")
start_time = time.time()
response = ollama.generate(model='phi3:3.8b', prompt='Hello!')
end_time = time.time()
print(response['response'])
print(f"Response time: {end_time - start_time:.2f} seconds")