"""Pytest setup for your eval sprint.

Puts the repo root on the import path so the eval file you write with Claude
can do `from app.agent import respond` — the same import Wednesday's scaffold uses.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
