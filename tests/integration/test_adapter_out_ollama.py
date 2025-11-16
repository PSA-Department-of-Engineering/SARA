"""Test the HandleConversation use case."""

import time
from application.use_cases.handle_conversation import HandleConversation

# Test the use case
use_case = HandleConversation()

# Test Default Mode
print("Testing Default Mode:")
start_time = time.time()
result = use_case.handle_conversation("Who are you?")
elapsed = time.time() - start_time
print(f"Input: {result.user_input}")
print(f"Response: {result.response}")
print(f"Mode: {result.mode.value}")
print(f"Timestamp: {result.timestamp}")
print(f"Time taken: {elapsed:.2f} seconds")

# Test Deep Think Mode
print("\nTesting Deep Think Mode:")
start_time = time.time()
result = use_case.handle_conversation("Think who are you?")
elapsed = time.time() - start_time
print(f"Input: {result.user_input}")
print(f"Response: {result.response}")
print(f"Mode: {result.mode.value}")
print(f"Timestamp: {result.timestamp}")
print(f"Time taken: {elapsed:.2f} seconds")