import os

def load_prompts(folder):

    prompts = {}

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            with open(
                os.path.join(folder,file),
                encoding="utf-8"
            ) as f:

                prompts[file] = f.read()

    return prompts