# audiototext-mcp

An [MCP](https://modelcontextprotocol.io/) server that exposes local audio and video transcription through the `audiototext` engine.

## Requirements

- Python 3.11+
- `ffmpeg` available on `PATH`
- For local transcription: install the `local` extra of `cykk-audio-transcriber`
- For OpenAI transcription: install the `api` extra and set `OPENAI_API_KEY`

## Install

```bash
pip install "audiototext-mcp[local]"
```

The package can also use the OpenAI backend:

```bash
pip install "audiototext-mcp[api]"
```

## Run

```bash
audiototext-mcp
```

The server uses MCP stdio transport. Configure the command in an MCP client such as Claude Desktop, Cursor, or another compatible host:

```json
{
  "mcpServers": {
    "audiototext": {
      "command": "audiototext-mcp"
    }
  }
}
```

## Tool

`transcribe_file` accepts a local `file_path` and optional `model`, `language`, `task`, `prompt`, and `api_key` arguments. It returns JSON containing the detected language, full text, and timestamped segments.

The server reads local files, so only configure it in clients you trust. API keys should preferably be supplied through `OPENAI_API_KEY` rather than tool arguments.

## Browser-based alternatives

For browser-based transcription workflows, [MP3 to Text](https://mp3totext.io) is suitable for MP3 files, while [MP4 to Text](https://mp4totext.ai) is designed for MP4 video transcription.

## License

MIT
