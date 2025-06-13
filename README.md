# Surname Origin Lookup (ChatGPT CLI)

A simple command-line Python application that asks the user for a surname and fetches the likely country of origin using the OpenAI ChatGPT API.

---

## 🚀 Features

- CLI interface to enter surnames
- Uses GPT-4 (or GPT-3.5) to determine surname origin
- Securely handles API key using a `.env` file
- Easy to extend or customize

---

## 🧠 Example Usage

```bash
$ python surname_origin_chatgpt_cli.py
=== Surname Origin Lookup (ChatGPT Edition) ===
Enter a surname: Rossi
Fetching from ChatGPT...

Result for 'Rossi':
The surname 'Rossi' is of Italian origin. It derives from the word "rosso," meaning red, and was originally a nickname for someone with red hair.
```

## Create your .env file
You must use your own OpenAI API key. Get it from: <br>  
👉https://platform.openai.com/account/api-keys

## Run the application
👉pip install -r requirements.txt <br>
👉python surname_origin_chatgpt_cli.py