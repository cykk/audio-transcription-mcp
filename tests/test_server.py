from __future__ import annotations

import unittest
from pathlib import Path
from tempfile import NamedTemporaryFile

from audiototext_mcp.server import mcp, transcribe_file


class ServerTests(unittest.TestCase):
    def test_transcribe_tool_is_registered(self) -> None:
        tool_names = {tool.name for tool in mcp._tool_manager.list_tools()}
        self.assertIn("transcribe_file", tool_names)

    def test_missing_file_is_rejected(self) -> None:
        with self.assertRaises(ValueError) as error:
            transcribe_file(str(Path("definitely-missing-audio-file.wav")))
        self.assertIn("File not found", str(error.exception))

    def test_invalid_task_is_rejected(self) -> None:
        with NamedTemporaryFile(suffix=".wav") as audio_file:
            with self.assertRaises(ValueError) as error:
                transcribe_file(audio_file.name, task="invalid")
        self.assertIn("task must be", str(error.exception))


if __name__ == "__main__":
    unittest.main()
