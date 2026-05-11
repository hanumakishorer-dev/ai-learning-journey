import os
from openai import OpenAI

# ✅ Initialize client for Windsurf (IMPORTANT: base_url)
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://api.windsurf.ai/v1"   # ✅ Windsurf endpoint
)

# ✅ Read PR diff
with open("diff.txt", "r") as f:
    diff = f.read()

# ✅ Limit size
diff = diff[:15000]

# ✅ Prompt
prompt = f"""
You are a senior software engineer reviewing a pull request.

Focus on:
- Bugs
- Security issues
- Performance issues

Be concise and actionable.

Diff:
{diff}
"""

# ✅ Call model (model name may differ in Windsurf)
response = client.chat.completions.create(
    model="gpt-4o-mini",   # ⚠️ If this fails, see note below
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# ✅ Extract result
review = response.choices[0].message.content

# ✅ Save output
with open("review.txt", "w") as f:
    f.write(review)

print("✅ AI review completed successfully")
