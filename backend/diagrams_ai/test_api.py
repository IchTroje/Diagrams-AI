from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<api-key",
)

completion = client.chat.completions.create(
  # extra_headers={
  #   "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
  #   "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  # },
  extra_body={},
  model="nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
  messages=[
    {
      "role": "user",
      "content": "What is apple?"
    }
  ]
)
print(completion.choices[0].message.content)