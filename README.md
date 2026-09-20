# Audio & Video Transcription MCP

An [MCP](https://modelcontextprotocol.io/) server for local audio and video transcription with local Whisper or the OpenAI transcription API.

Package and CLI name: `audio-transcription-mcp`.

## Requirements

- Python 3.11+
- `ffmpeg` available on `PATH`
- For local transcription: install the `local` extra of `cykk-audio-transcriber`
- For OpenAI transcription: install the `api` extra and set `OPENAI_API_KEY`

## Install from source

```bash
git clone https://github.com/cykk/audiototext-mcp.git
cd audiototext-mcp
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

## License

MIT
