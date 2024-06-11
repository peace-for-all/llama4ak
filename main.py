from llama_cpp import Llama

print(f"Enter your prompt:")
prompt = str(input())
llm = Llama(
      model_path="./models/llama-2-13b.Q5_K_M.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      n_ctx=2048 # Tokens
)
output = llm(
      prompt,
      max_tokens=128, # How many tokens to generate
      # stop=["\n"], # Stop generating just before the model would generate a new question
      # echo=True # If uncommented, response contains the question
)
# print(output)

print(output['choices'][0]['text'])

# {'id': 'cmpl-81d9f0fc-93e0-4c64-8987-2c6c91dd9a8a', 'object': 'text_completion', 'created': 1718102880, 'model': './models/llama-2-13b.Q5_K_M.gguf', 'choices': [{'text': "ping how are you? i love your blog!\nHey, I'm a new follower from the Friday Follow hop.\nFollow back if you can at my blog.\nHi!! Newest follower...hope you can check out my site as well and follow back!\nI have 100+ followers so I am having a contest for 500 followers...hop on over to enter!!", 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 6, 'completion_tokens': 86, 'total_tokens': 92}}
