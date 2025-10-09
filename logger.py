import sys
import logging
import re
from pathlib import Path

def setup_chat_logger(log_file="chat.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    fh = logging.FileHandler(log_file, mode='w')
    fh.setLevel(logging.INFO)
    # Filter out noisy HTTP/traces lines from the file handler
    class _HttpNoiseFilter(logging.Filter):
        def filter(self, record: logging.LogRecord) -> bool:
            msg = record.getMessage()
            # drop lines mentioning HTTP request details or traces ingest endpoints
            if 'HTTP Request:' in msg or 'traces/ingest' in msg:
                return False
            return True
    fh.addFilter(_HttpNoiseFilter())
    fh.setFormatter(logging.Formatter(
        fmt='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

    logger.addHandler(fh)
    
    logger.info("--------- New Session -------------")
    return logger

def convert_logs_to_markdown(log_text: str) -> str:
    lines = log_text.strip().splitlines()
    md_lines = []

    for line in lines:
        # Extract the message part after [INFO]
        match = re.search(r"\[INFO\]\s+(.*)", line)
        if not match:
            continue
        message = match.group(1).strip()

        # Detect session header
        if "New Session" in message:
            md_lines.append("> <p align=\"center\">------------- New Session -------------</p>")
            md_lines.append(">")
            continue

        # Detect Agent/User prefix
        if message.startswith("Agent:"):
            content = message[len("Agent:"):].strip()
            md_lines.append(f"> **Agent:** {content}")
            md_lines.append(">")
        elif message.startswith("User:"):
            content = message[len("User:"):].strip()
            md_lines.append(f"> **User:** {content}")
            md_lines.append(">")

    return "\n".join(md_lines).rstrip(">\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 logger.py input.log output.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    log_text = input_path.read_text(encoding="utf-8")
    markdown_output = convert_logs_to_markdown(log_text)

    output_path.write_text(markdown_output, encoding="utf-8")
    print(f"✅ Converted {input_path} → {output_path}")

