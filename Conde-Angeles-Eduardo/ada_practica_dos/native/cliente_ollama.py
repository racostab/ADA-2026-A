#author: eduardo conde
#date: 13/03/2026
from ollama import Client

def clientFactory(host, port):
    client = Client(
        host=f'{host}:{port}',
        headers={'x-some-header': 'some-value'}
    )
    return client

def makeChatPetition(client, model_name, question):
    """
    Usar si queremos simular la conversacion completa y ver el plan de accion del LLM
    """
    try:
        response = client.chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': question,
        },
        ])
        return response
    except Exception as inst:
        print("Ocurrio un error al realizar la peticion:")
        print(type(inst))   #The exception type
        print(inst.args)    #Arguments stored in .args
        print(inst)         #Error

def makeGeneratePetition(client, model_name, prompt_param):
    """
    Generar respuesta única de código puro sin explicaciones ni markdown.
    Generar respuesta unica, no muestra el plan de accion del LLM para responder
    """
    # Definimos el comportamiento estricto del modelo
    """
    system_instruction = (
        "CODE_ONLY_MODE=TRUE. Your output is a direct pipe to a compiler. "
        "Any text that is not valid source code will break the system. "
        "Do not use markdown. Do not use backticks (```). Do not explain. "
        "Start with the code immediately."
    )
    """
    system_instruction = (
        "ROLE: RAW_CODE_GENERATOR. "
        "OUTPUT_RULE: ONLY SOURCE CODE. "
        "CODE_ONLY_MODE=TRUE. Your output is a direct pipe to a compiler. "
        "NO introductory text. NO explanations. NO closing remarks. "
        "NO markdown code blocks (backticks ```). "
        "If you use comments, they must be in the language of the code requested. "
        "Start the response directly with the first line of code."
    )
    try:
        #prompt_param=f"# Language: Python\n# Task: {prompt_param} \nimport"
        result = client.generate(
            model=model_name,
            #system=system_instruction,
            #prompt=prompt_param,
            prompt=prompt_param,           
            raw=True,
            options = {
                "temperature": 0.0,
                "stop": [ "###", "```"],
                "num_predict": 1024, #Longitud máxima de tokens para el código generado
                "top_p": 0.1         #Reduce la probabilidad de elegir palabras irrelevantes
            }
        )
        return result["response"]
    except Exception as inst:
        print("Ocurrio un error al realizar la peticion:")
        print(type(inst))   #The exception type
        print(inst.args)    #Arguments stored in .args
        print(inst)         #Error

def chatToOllama(endPointHost, endPointPort, model_name, question):
    client=clientFactory(endPointHost,endPointPort)
    response = makeChatPetition(client, model_name, question)
    print(f"Respuesta:\n{response}")

def generateToOllama(endPointHost, endPointPort, model_name, prompt):
    client=clientFactory(endPointHost,endPointPort)
    return makeGeneratePetition(client, model_name, prompt)

def save_generated_code(response_text, program_name, language):
    """
    Limpia la respuesta de Ollama y la guarda en un archivo local.
    """
    # Extensiones según el lenguaje
    extensions = {
        "python": ".py",
        "cpp": ".cpp",
        "c": ".c"
    }    
    ext = extensions.get(language.lower(), ".txt")
    filename = f"{program_name}{ext}"    
    # Limpieza básica: eliminamos posibles bloques de markdown si el modelo se saltó el stop
    clean_code = response_text.replace("```python", "").replace("```", "").strip()
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(clean_code)
        print(f"✅ Código guardado exitosamente en: {filename}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

def createAndExecute(endPointHost, endPointPort, model_name, prompt, program_name):
    for i in range(0,5):
        response_text = generateToOllama(endPointHost, endPointPort, model_name, prompt)
        save_generated_code(response_text, f"{program_name}_{i}", "python")    

if __name__ == '__main__':
    #produccion
    endPointHost="http://100.113.158.78"
    endPointPort="11434"
    model_name="qwen3:4B"
    #local
    endPointHost="http://localhost"
    endPointPort="11434"
    model_name='deepseek-coder:1.3b'

    #instrucciones
    program_name="binary_tree_sort"
    lenguaje="python"
    requisito="Immplement the Binary Tree Sort algorythm"
    entrada="A list of numbers separated by the character space"
    salida="List of numbers ordered"
    call_program=f" {program_name} + the input as specified above from the standard input"
    
    #prompt humano no crea solo codigo, siempre hay "amabilidad" del modelo
    prompt=(
            f"Generate a program with the following specs: \n"
            #f"Nombre {program_name}"
            f"Language code: {lenguaje}\n"
            f"Request: {requisito}\n"
            f"Input(s): {entrada}\n"
            f"Output(s): {salida}\n"
            #f"How to call: {call_program} + input(s)"
            f"Expected output: Result related to input in asc order\n"
            f"Output only the code, start directly with the first line of code."
    )
    
    #prompt maquina funciona parcialmente
    prompt = (
        f"# Language: {lenguaje}\n"
        f"# Task: {requisito}\n"
        f"# Input: {entrada}\n"
        f"# Output: {salida}\n"
        f"# Algorithm: {program_name}\n"
    )
    
    #No regresa codigo limpio
    prompt = (
        f"# Language: {lenguaje}\n"
        f"# Task: {requisito}\n"
        f"# Input: {entrada}\n"
        f"# Output: {salida}\n"
        f"# Algorithm: {program_name}\n"
        f"import sys\n"
    )

    #No regresa codigo limpio
    prompt = (
        f"# Language: {lenguaje}\n"
        f"# Task: {requisito}\n"
        f"# Input: {entrada}\n"
        f"# Output: {salida}\n"
        f"# Algorithm: {program_name}\n"
        f"# Execution:{call_program}\n"
        f"# Implementation:\n" # Terminamos con un comentario
    )
    
    #regresa codigo limpio
    prompt = (
        f"# Language: {lenguaje}\n"
        f"# Task: {requisito}\n"
        f"# Input: {entrada}\n"
        f"# Output: {salida}\n"
        f"# Algorithm: {program_name}\n"
        f"# Execution:{call_program}\n"
        f"# Read from command line arguments\n"
    )
    #regresa codigo limpio no funcional
    salida="The list of numbers ordered, separated by spaces, no other character is a valid output"
    prompt = (
        f"# Language: {lenguaje}\n"
        f"# Task: {requisito}\n"
        f"# Input: {entrada}\n"
        f"# Output: {salida}\n"
        f"# Algorithm: {program_name}\n"
        f"# Execution:{call_program}\n"
        f"# Read from command line arguments\n"
    )
    
    #regresa codigo limpio funcional y es el que testeamos
    salida="The list of numbers ordered separated by spaces"
    prompt = (
        f"# Language: {lenguaje}\n"
        f"# Task: {requisito}\n"
        f"# Input: {entrada}\n"
        f"# Output: {salida}\n"
        f"# Algorithm: {program_name}\n"
        f"# Execution:{call_program}\n"
        f"# Read from command line arguments\n"
    )
    createAndExecute(endPointHost, endPointPort, model_name, prompt, "../ia_resultado/ia_3_code_r")
    