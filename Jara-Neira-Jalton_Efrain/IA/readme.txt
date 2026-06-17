readme.txt
1. Las bibliotecas instaladas hasta el momento de la ejecución correcta del programa se encuentran en el archivo: requirements.txt Para instalarlas, ejecutar en la terminal:

> pip install -r .\requirements.txt

2. Copiar a la carpeta donde se va a ejecutar el programa los archivos: revision_llm.py y config.yaml

3. Guardar los artículos a analizar en una carpeta "./articulos/" se puede cambiar el nombre de la carpeta en el archivo config.yaml.

4. Para la ejecución del programa, indicar el modelo que se desea utilizar:

> python revision_llm.py --modelo mistral:7B 
