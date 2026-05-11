import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["WINDSURF_API_KEY"])

# Read diff
with open("diff.txt", "r") as f:
    diff = f.read()

# Limit size (important!)
diff = diff[:15000]

prompt = f"""
You are a senior software engineer doing a pull request review.

Analyze the following git diff and provide:

1. Bugs or risks
2. Security issues
3. Performance concerns
4. Code quality improvements

Give concise, actionable feedback.
Do NOT repeat the code.

Diff:
{diff}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}]
)

review = response.choices[0].message.content

# Save review
with open("review.txt", "w") as f:
    f.write(review)
