
import openai

def summarize_text_with_openai(text):
    # Set your OpenAI API key
    api_key = "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"
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following text:\n{text}\n\nSummary:",
        max_tokens=100,
    )

    summary = response["choices"][0]["text"]
    return summary
