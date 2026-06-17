import ollama

def query_llm(model_name, prompt):
    """
    Envía un prompt a un modelo local de Ollama y retorna la respuesta.
    """
    print(f"\n[{model_name}] Generando respuesta...")
    try:
        response = ollama.generate(
            model=model_name,
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"Error con el modelo {model_name}: {e}"

def generate_prompts(thesis_topic, problem_statement, articles_text, version="v1"):
    """
    Genera los 4 prompts requeridos basados en los textos extraídos y los detalles de la tesis.
    Soporta múltiples versiones de prompts para cumplir con los requerimientos.
    """
    # Para no saturar el contexto de los LLMs, podemos truncar el texto si es muy grande.
    context = ""
    for name, text in articles_text.items():
        # Tomamos solo los primeros 4000 caracteres de cada artículo para evitar errores de contexto
        context += f"--- Artículo: {name} ---\n{text[:4000]}\n\n"

    if version == "v2":
        # Versión 2: Prompts con persona experta y más detalle
        prompts = {
            "A_Problemas_No_Resueltos": f"Actúa como un investigador experto en '{thesis_topic}'. Analiza minuciosamente los siguientes artículos y extrae los gaps o problemas de investigación que aún no han sido resueltos por los autores. Presenta tu respuesta en viñetas.\n\nArtículos:\n{context}",
            "B_Viabilidad_Problema": f"Eres un sinodal de maestría estricto. Lee este planteamiento de problema: '{problem_statement}'. Basándote en el estado del arte provisto en estos artículos, evalúa críticamente: ¿es este problema real, metodológicamente pertinente y factible de ser resuelto en un plazo de 18 meses? Da un veredicto final justificado.\n\nArtículos:\n{context}",
            "C_Metodologias": f"Como experto en revisión de literatura, desglosa la metodología aplicada en cada uno de estos artículos. Necesito que estructures la respuesta dando el nombre formal de la metodología usada y una enumeración paso a paso de lo que hicieron los autores.\n\nArtículos:\n{context}",
            "D_Revision_Sistematica": f"Imagina que vamos a escribir un artículo de revisión sistemática sobre '{thesis_topic}'. Basado en los artículos proporcionados, ¿cuáles son las referencias clave, palabras clave y enfoques bibliográficos que deberíamos considerar sin falta?\n\nArtículos:\n{context}",
            "E_Generar_Cita": f"Como bibliotecario experto, extrae los metadatos (título, autores, año) del texto de estos artículos y genera su respectiva cita en formato BibTeX (estilo IEEE). Devuelve ÚNICAMENTE los bloques de código BibTeX, sin introducciones ni explicaciones.\n\nArtículos:\n{context}"
        }
    else:
        # Versión 1 (v1): Prompts directos (por defecto)
        prompts = {
            "A_Problemas_No_Resueltos": f"Basado en los siguientes artículos sobre '{thesis_topic}', ¿qué problemas de investigación no están resueltos? Sé conciso y enlista los problemas.\n\nArtículos:\n{context}",
            "B_Viabilidad_Problema": f"Dado el siguiente planteamiento del problema: '{problem_statement}', y considerando la información de estos artículos, ¿el problema es real, pertinente y factible de resolver en 18 meses? Justifica tu respuesta.\n\nArtículos:\n{context}",
            "C_Metodologias": f"Analiza los siguientes artículos e identifica qué metodología se usó en cada uno. Dame el nombre de la metodología y una lista resumida de los pasos para cada artículo.\n\nArtículos:\n{context}",
            "D_Revision_Sistematica": f"Para realizar una revisión sistemática (Survey, Overview, etc.) del tema '{thesis_topic}', ¿qué referencias específicas o tipos de referencias se deben considerar a partir de los artículos dados?\n\nArtículos:\n{context}",
            "E_Generar_Cita": f"Extrae los metadatos de los siguientes artículos y genera sus citas en formato BibTeX (IEEE). Devuelve solamente el código BibTeX.\n\nArtículos:\n{context}"
        }
        
    return prompts
