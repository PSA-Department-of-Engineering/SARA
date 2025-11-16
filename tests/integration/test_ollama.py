"""Test the HandleConversation use case."""

from use_cases.handle_conversation import HandleConversation

# Test the use case
use_case = HandleConversation()

# Test Default Mode
print("Testing Default Mode:")
result = use_case.execute("Hello!")
print(f"Input: {result.user_input}")
print(f"Response: {result.response}")
print(f"Mode: {result.mode.value}")
print(f"Timestamp: {result.timestamp}")

# Test Deep Think Mode
print("\nTesting Deep Think Mode:")
result = use_case.execute("Think hello!")
print(f"Input: {result.user_input}")
print(f"Response: {result.response}")
print(f"Mode: {result.mode.value}")
print(f"Timestamp: {result.timestamp}")