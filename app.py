import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Here's a Python function that checks whether a word is a palindrome.\nAdd 10 different unit tests for this snippet with comments. Follow up with a short explanation of what was done.\n\n\n```\ndef is_palindrome(word):\n  \"\"\"\n  Checks whether a word is a palindrome.\n\n  Args:\n    word: The word to check.\n\n  Returns:\n    True if the word is a palindrome, False otherwise.\n  \"\"\"\n\n  # Convert the word to lowercase and remove non-alphanumeric characters.\n  word = ''.join(char.lower() for char in word if char.isalnum())\n\n  # Check if the word is the same forwards and backwards.\n  return word == word[::-1]\n```",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)