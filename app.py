"""Night Owl: answers questions about a team's notes, routing every LLM call through Mubit."""

import os

import anthropic

client = anthropic.Anthropic(
    base_url=os.environ.get("MUBIT_BASE_URL", "https://api.mubit.ai"),
    api_key=os.environ["MUBIT_API_KEY"],
)


def ask(question: str, notes: str) -> str:
    reply = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=400,
        messages=[{"role": "user", "content": f"Notes:\n{notes}\n\nQuestion: {question}"}],
    )
    return reply.content[0].text


if __name__ == "__main__":
    import sys

    from notes import load_notes

    print(ask(sys.argv[2], load_notes(sys.argv[1])))
