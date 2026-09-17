"""Model Context Protocol server for audio and video transcription."""

from __future__ import annotations

import json
import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from audiototext.audio import ensure_ffmpeg
from audiototext.config import CliConfig
from audiototext.providers import local_whisper, openai_api

mcp = FastMCP("audiototext")


@mcp.tool()
def transcribe_file(
    file_path: str,
    model: str = "small",
    language: str = "Auto-Detect",
    task: str = "transcribe",
    prompt: str | None = None,
    api_key: str | None = None,
) -> str:
    """Transcribe a local audio or video file and return JSON with text and timestamps.

    Uses local Whisper by default. Set api_key (or OPENAI_API_KEY) to use the
    OpenAI speech API instead. The file must be readable by the MCP server.
    """
    path = Path(file_path).expanduser().resolve()
    if not path.is_file():
        raise ValueError(f"File not found: {path}")
    if task not in {"transcribe", "translate"}:
        raise ValueError("task must be 'transcribe' or 'translate'")

    selected_key = api_key or os.getenv("OPENAI_API_KEY")
    config = CliConfig(
        audio_files=[path],
        task=task,
        model=model,
        language=language,
        prompt=prompt,
        coherence_preference=True,
        api_key=selected_key,
        output_formats=("json",),
        output_dir=path.parent,
        deepl_api_key=None,
        deepl_target_language=None,
        deepl_coherence_preference=True,
        deepl_formality="default",
        verbose=False,
    )

    ensure_ffmpeg()
    results = openai_api.transcribe_files(config) if selected_key else local_whisper.transcribe_files(config)
    if not results:
        raise RuntimeError("No transcription result returned")

    result = results[0]
    payload = result.to_writer_payload()
    payload["source_file"] = str(path)
    return json.dumps(payload, ensure_ascii=False)


def main() -> None:
    """Run the MCP server over stdio (the default MCP transport)."""
    mcp.run()


if __name__ == "__main__":
    main()
