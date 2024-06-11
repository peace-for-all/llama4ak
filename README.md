# Demo of a LLM running on llama.cpp (python bindings)

## Setup

### Prep virtualenv

Prerequisite: have python3 installed.

```bash
python3 -m venv venv # creates venv directory
source venv/bin/activate # enters virtual environment
pip install llama-cpp-python \
  --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu # rm extra-index-url part if runs on GPU
```

### Put a model into models/ dir

- I've tested with [llama-2-13b.Q5_K_M.gguf](https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q5_K_M.gguf?download=true) (warning! 9Gb on local disk!)
- `llama_cpp_python` author suggests pulling [from HuggingFace directly - link to howto](https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file#pulling-models-from-hugging-face-hub).

### Edit main.py
Model path: has to have your model file name.

### Run main.py

```bash
python3 main.py 2>error.log
```
NOTE: by default the model writes a lot of information out into STDERR. I filter that out with 2>error.log for you to see later.
If you want to see all output, remove 2>error.log, just run `python3 main.py`.
