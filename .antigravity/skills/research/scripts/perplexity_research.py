#!/usr/bin/env python3
"""
perplexity_research.py
Part of the 'research' skill for Michael's executive assistant workspace.

Calls the Perplexity API with a context-aware system prompt built from
Michael's live context files (priorities, goals, work, profile).

Usage:
    python perplexity_research.py --query "your research topic"
    python perplexity_research.py --query "your research topic" --save

Requirements:
    pip install python-dotenv requests
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

# ── Dependency checks ────────────────────────────────────────────────────────

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv not installed.\nRun: pip install python-dotenv requests")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("Error: requests not installed.\nRun: pip install python-dotenv requests")
    sys.exit(1)

# ── Paths ─────────────────────────────────────────────────────────────────────

# Script lives at: .antigravity/skills/research/scripts/perplexity_research.py
# Workspace root is 4 levels up
WORKSPACE_ROOT = Path(__file__).resolve().parents[4]
load_dotenv(WORKSPACE_ROOT / ".env")

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_ENDPOINT = "https://api.perplexity.ai/chat/completions"
MODEL = "sonar-pro"

# ── Context loading ───────────────────────────────────────────────────────────

def load_file(relative_path: str) -> str:
    """Load a file from the workspace root. Returns a placeholder if missing."""
    path = WORKSPACE_ROOT / relative_path
    if path.exists():
        content = path.read_text(encoding="utf-8").strip()
        return content if content else f"[{relative_path} is empty]"
    return f"[{relative_path} not found]"


def load_active_projects() -> str:
    """Load README files from any active project folders."""
    projects_dir = WORKSPACE_ROOT / "projects"
    readmes = []
    if projects_dir.exists():
        for readme in projects_dir.glob("*/README.md"):
            readmes.append(f"### Project: {readme.parent.name}\n{readme.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(readmes) if readmes else "[No active projects]"


def build_system_prompt() -> str:
    """Dynamically build a context-aware system prompt from workspace files."""
    me = load_file("context/me.md")
    work = load_file("context/work.md")
    priorities = load_file("context/current-priorities.md")
    goals = load_file("context/goals.md")
    projects = load_active_projects()

    return f"""You are a research assistant for Michael, an AI consultant based in Dallas-Fort Worth, TX.

Your job is to conduct deep, actionable research tailored to his current business context.
Always frame findings in terms of practical value — what this means for landing clients,
growing his consulting business, or applying AI to help businesses.

=== WHO MICHAEL IS ===
{me}

=== BUSINESS & SERVICES ===
{work}

=== CURRENT PRIORITIES ===
{priorities}

=== Q3 2026 GOALS ===
{goals}

=== ACTIVE PROJECTS ===
{projects}

=== RESEARCH GUIDELINES ===
- Prioritize findings relevant to landing clients and generating revenue
- When discussing AI tools or trends, frame them as consulting opportunities
- Be specific and practical — not academic or generic
- Use bullet points over paragraphs
- Clearly separate: Key Findings / Actionable Takeaways / Sources
- Cite sources inline where possible
- Flag anything that directly supports Michael's #1 priority: getting first clients
"""


# ── API call ──────────────────────────────────────────────────────────────────

def run_research(query: str) -> dict:
    """Call the Perplexity API. Returns dict with content and citations."""
    if not PERPLEXITY_API_KEY or PERPLEXITY_API_KEY == "your_perplexity_api_key_here":
        return {
            "content": "Error: PERPLEXITY_API_KEY not set in .env — open the .env file and paste your key.",
            "citations": [],
        }

    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": query},
        ],
        "max_tokens": 2048,
        "temperature": 0.2,
        "return_citations": True,
        "search_recency_filter": "month",
    }

    try:
        response = requests.post(PERPLEXITY_ENDPOINT, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()

        content = data["choices"][0]["message"]["content"]
        citations = data.get("citations", [])
        return {"content": content, "citations": citations}

    except requests.exceptions.HTTPError:
        return {"content": f"API Error {response.status_code}: {response.text}", "citations": []}
    except requests.exceptions.ConnectionError:
        return {"content": "Connection error — check your internet connection.", "citations": []}
    except requests.exceptions.Timeout:
        return {"content": "Request timed out after 60s — try again.", "citations": []}
    except (KeyError, IndexError) as e:
        return {"content": f"Unexpected API response format: {e}", "citations": []}


# ── Output formatting ─────────────────────────────────────────────────────────

def format_output(query: str, result: dict) -> str:
    """Format the research result as structured markdown."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    content = result["content"]
    citations = result.get("citations", [])

    output = f"## Research: {query}\n\n"
    output += f"**Date:** {date_str}  \n"
    output += f"**Model:** {MODEL}\n\n"
    output += "---\n\n"
    output += content

    if citations:
        output += "\n\n### Sources\n"
        for i, url in enumerate(citations, 1):
            output += f"{i}. {url}\n"

    return output


def save_output(query: str, formatted: str) -> Path:
    """Save research output to references/research/."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = "".join(c if c.isalnum() or c == " " else "" for c in query)
    slug = slug.strip().replace(" ", "-")[:50].lower()

    save_dir = WORKSPACE_ROOT / "references" / "research"
    save_dir.mkdir(parents=True, exist_ok=True)

    save_path = save_dir / f"{date_str}-{slug}.md"
    save_path.write_text(formatted, encoding="utf-8")
    return save_path


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Context-aware research via Perplexity AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python perplexity_research.py --query \"AI consulting market DFW\" --save"
    )
    parser.add_argument("--query", "-q", required=True, help="Research question or topic")
    parser.add_argument("--save", "-s", action="store_true", help="Save output to references/research/")
    args = parser.parse_args()

    print(f"\nResearching: {args.query}")
    print("=" * 60)
    print("Loading context and calling Perplexity...\n")

    result = run_research(args.query)
    formatted = format_output(args.query, result)

    print(formatted)

    if args.save:
        saved_path = save_output(args.query, formatted)
        rel = saved_path.relative_to(WORKSPACE_ROOT)
        print(f"\nSaved to: {rel}")


if __name__ == "__main__":
    main()
