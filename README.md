jieba
requests


## Motivation & Core Logic

Before building this script, I was struggling with a limited RAM budget. Vector databases are too resource-intensive, and models easily forget context over time.

To solve this, I implemented a TXT keyword-based text retrieval method to help the model recall past information. By utilizing disk-based TXT searches, the script offloads tasks that would otherwise consume excessive RAM.

Essentially, the workflow is:

1. Your input is sent to the script.
2. The script performs a keyword search across local TXT files.
3. The retrieved memory and your prompt are bundled together and sent to the local model.

Memory Management

When your conversation reaches three rounds, the model packs these three rounds of dialogue, performs a core summarization, and saves the result into a local TXT file.

Future Optimizations

You are welcome to optimize any part of this code. I believe the following features would be great additions:

· Retrieval based on date/time.
· Automatically creating a new TXT file when the existing file reaches maximum capacity.

Usage & Deployment Notes

· Launcher: When running the launcher inside the ai.jy folder, remember to place the entire llama.cpp package inside that directory. Only then will the script be able to locate and execute it.
· Tested Environment:
  · Deployment framework: llama-b11429-bin-win-cuda-12.4-x64
  · Model: Qwen2.5 (Tested)
  · Prompt Template: The official ChatML template is used. If you switch to a different model, please remember to modify the prompt template in the code.

Disclaimer

The rights of the model belong to the official Alibaba Qwen team.
