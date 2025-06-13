import openai
import os

# Load your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")  # or set it directly: openai.api_key = "your-key-here"

def fetch_surname_origin(surname):
    prompt = f"What is the country of origin for the surname '{surname}'? Provide a brief explanation."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if you don't have GPT-4 access
            messages=[
                {"role": "system", "content": "You are an expert in genealogy and surname etymology."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=100
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"

def main():
    print("=== Surname Origin Lookup (ChatGPT Edition) ===")
    surname = input("Enter a surname: ").strip()

    if not surname:
        print("You did not enter a surname.")
        return

    print("Fetching from ChatGPT...")
    result = fetch_surname_origin(surname)
    print(f"\nResult for '{surname}':\n{result}")

if __name__ == "__main__":
    main()
