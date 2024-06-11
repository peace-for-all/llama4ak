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

- Download 8.6G file of model -> [llama-2-13b.Q5_K_M.gguf](https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q5_K_M.gguf?download=true), place in models/ dir.

### Run main.py

```bash
python3 main.py 2>error.log
```
NOTE: by default the model writes a lot of information out into STDERR. I filter that out with 2>error.log for you to see later.
If you want to see all output, remove 2>error.log, just run `python3 main.py`.


## Notes

- `llama_cpp_python` library used here supports pulling models [from HuggingFace directly - link to howto](https://github.com/abetlen/llama-cpp-python?tab=readme-ov-file#pulling-models-from-hugging-face-hub). This allows experiments with other models.


# RAG script

## Setup

### Script env
```bash
python3 -m venv venv # creates venv directory
source venv/bin/activate # enters virtual environment
pip install -r requirements.txt
```
### Data for RAG
1. Create directory `data_rag_ru` in this project;
2. Put there PDF files to get the answers data from.

## Run

```bash
python3 rag_from_pdf.py
```
then ask your questions from it.

Cheers.
