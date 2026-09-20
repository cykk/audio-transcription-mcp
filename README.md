# Audio Transcription MCP

An [MCP](https://modelcontextprotocol.io/) server for local audio and video transcription with local Whisper or the OpenAI transcription API.

Package and CLI name: `audio-transcription-mcp`.

## Requirements

- Python 3.11+
- `ffmpeg` available on `PATH`
- For local transcription: install the `local` extra of `cykk-audio-transcriber`
- For OpenAI transcription: install the `api` extra and set `OPENAI_API_KEY`

Install `ffmpeg` separately if it is not already available on your `PATH`.
On Debian/Ubuntu, use `sudo apt install ffmpeg`; on macOS with Homebrew, use
`brew install ffmpeg`; on Windows, install an FFmpeg build and add its `bin`
directory to `PATH`.

## Install from source

```bash
git clone https://github.com/cykk/audio-transcription-mcp.git
cd audio-transcription-mcp
pip install ".[local]"
```

To use the OpenAI transcription API instead:

```bash
pip install ".[api]"
```

## Install from PyPI

After the package is published to PyPI, install it directly:

```bash
pip install "audio-transcription-mcp[local]"
```

For the OpenAI transcription API:

```bash
pip install "audio-transcription-mcp[api]"
```

## Run

```bash
audio-transcription-mcp
```

For backward compatibility, `audiototext-mcp` remains available as an alias.

The server uses MCP stdio transport. Configure the command in an MCP client such as Claude Desktop, Cursor, or another compatible host:

```json
{
  "mcpServers": {
    "audio-transcription": {
      "command": "audio-transcription-mcp"
    }
  }
}
```

## Tool

`transcribe_file` accepts a local `file_path` and optional `model`, `language`, `task`, `prompt`, and `api_key` arguments. It returns JSON containing the detected language, full text, and timestamped segments.

The server reads local files, so only configure it in clients you trust. API keys should preferably be supplied through `OPENAI_API_KEY` rather than tool arguments.

## Verify

After adding the server to an MCP client, call `transcribe_file` with a readable local audio or video file path. A successful response contains the detected language, full transcript, and timestamped segments.

To verify the package before configuring an MCP client, run:

```bash
python -c "import asyncio; from audiototext_mcp.server import mcp; print([tool.name for tool in asyncio.run(mcp.list_tools())])"
```

The command should include `transcribe_file`. A real transcription also requires
an installed local Whisper extra or a valid `OPENAI_API_KEY` for the API extra.

## License

MIT
