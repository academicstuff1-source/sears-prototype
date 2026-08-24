#!/usr/bin/env python3
"""
tavily_research.py
Part of the 'research' skill for Michael's executive assistant workspace.

Runs context-aware research using the Tavily Search API.
Loads Michael's workspace context files to enrich queries and frame output.

Usage:
    python tavily_research.py --query "your research topic"
    python tavily_research.py --query "your research topic" --save

Requirements:
    pip install tavily-python python-dotenv
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

# ── Dependency checks ─────────────────────────────────────────────────────────

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv not installed.\nRun: pip install tavily-python python-dotenv")
    sys.exit(1)

try:
    from tavily import TavilyClient
except ImportError:
    print("Error: tavily-python not installed.\nRun: pip install tavily-python python-dotenv")
    sys.exit(1)

# ── Paths ─────────────────────────────────────────────────────────────────────

# Script lives at: .agents/skills/research/scripts/tavily_research.py
# Workspace root is 4 levels up (.agents/skills/research/scripts → root)
WORKSPACE_ROOT = Path(__file__).resolve().parents[4]
load_dotenv(WORKSPACE_ROOT / ".env")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

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
            readmes.append(f"Project: {readme.parent.name}\n{readme.read_text(encoding='utf-8').strip()}")
    return "\n\n".join(readmes) if readmes else "No active projects."


def load_context() -> dict:
    """Load all relevant context files and return as a dict."""
    return {
        "me": load_file("context/me.md"),
        "work": load_file("context/work.md"),
        "priorities": load_file("context/current-priorities.md"),
        "goals": load_file("context/goals.md"),
        "projects": load_active_projects(),
    }


def build_context_summary(ctx: dict) -> str:
    """Build a readable context block for display."""
    return f"""=== CONTEXT ===
{ctx['me']}

{ctx['priorities']}

{ctx['goals']}

Active Projects: {ctx['projects']}
"""

# ── Research ──────────────────────────────────────────────────────────────────

def run_research(query: str, ctx: dict) -> dict:
    """Run a Tavily advanced search and return structured results."""
    if not TAVILY_API_KEY or TAVILY_API_KEY == "your_tavily_api_key_here":
        return {
            "answer": "Error: TAVILY_API_KEY not set in .env — open .env and paste your key from https://app.tavily.com",
            "results": [],
            "query": query,
        }

    # Enrich query with business context for better relevance
    enriched_query = f"{query} — context: AI consulting business, client acquisition, DFW Texas"

    try:
        client = TavilyClient(api_key=TAVILY_API_KEY)
        response = client.search(
            query=enriched_query,
            search_depth="advanced",
            include_answer=True,
            include_raw_content=False,
            max_results=7,
        )
        return {
            "answer": response.get("answer", "No synthesized answer returned."),
            "results": response.get("results", []),
            "query": query,
        }
    except Exception as e:
        return {
            "answer": f"Search failed: {e}",
            "results": [],
            "query": query,
        }


# ── Output formatting ─────────────────────────────────────────────────────────

def format_output(query: str, data: dict, ctx: dict) -> str:
    """Format research results as structured markdown."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    lines = []

    lines.append(f"## Research: {query}")
    lines.append(f"\n**Date:** {date_str}")
    lines.append(f"**Priority connection:** Review against `context/current-priorities.md`\n")
    lines.append("---\n")

    lines.append("### AI Summary")
    lines.append(data["answer"])
    lines.append("")

    if data["results"]:
        lines.append("### Top Sources & Snippets")
        for r in data["results"]:
            score = round(r.get("score", 0), 2)
            lines.append(f"\n**[{r['title']}]({r['url']})** (relevance: {score})")
            lines.append(f"> {r.get('content', '').strip()[:300]}...")

        lines.append("\n---\n")
        lines.append("### Sources")
        for i, r in enumerate(data["results"], 1):
            lines.append(f"{i}. [{r['title']}]({r['url']})")

    lines.append("\n---")
    lines.append("\n### Actionable Takeaways")
    lines.append("- [ ] *(Review findings above and fill in takeaways relevant to current priorities)*")

    return "\n".join(lines)


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
        description="Context-aware research via Tavily AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Example:\n  python tavily_research.py --query \"AI consulting trends 2025\" --save"
    )
    parser.add_argument("--query", "-q", required=True, help="Research question or topic")
    parser.add_argument("--save", "-s", action="store_true", help="Save output to references/research/")
    args = parser.parse_args()

    ctx = load_context()

    print(f"\nResearching: {args.query}")
    print("=" * 60)
    print("Loading context and calling Tavily...\n")

    data = run_research(args.query, ctx)
    formatted = format_output(args.query, data, ctx)

    print(formatted)

    if args.save:
        saved_path = save_output(args.query, formatted)
        rel = saved_path.relative_to(WORKSPACE_ROOT)
        print(f"\nSaved to: {rel}")


if __name__ == "__main__":
    main()
