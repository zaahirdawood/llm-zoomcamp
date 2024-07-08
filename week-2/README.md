>## Homework Week 2

**Q1:-** What's the version of ollama client?

### Step 1 run ollama container 

```
docker run -it \
    --rm \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

### Step 2 exec container in bash

```
docker exec -it ollama bash
```

Gemma Contents


### Step 3 check which Ollama Version
```
ollama -v
```

**A1:** 
<img width="782" alt="Screenshot 2024-07-08 at 23 21 40" src="https://github.com/zaahirdawood/llm-zoomcamp/assets/109787439/a7fbddfe-bd3c-4012-8016-e1baf425465c">

**Q2-Q3:-** Running the LLM/ Run a question to the model

While in your docker ollama bash console. To run the model we automatically asumme Q2 was fulfilled

```
ollama run gemma:2b
```

```
cat /root/.ollama/models/manifests/registry.ollama.ai/library/gemma/2b
```

<img width="1225" alt="Screenshot 2024-07-08 at 23 42 35" src="https://github.com/zaahirdawood/llm-zoomcamp/assets/109787439/4734f454-87ac-4625-b9c2-81000f384cee">

**A2-A3:** 
<img width="441" alt="Screenshot 2024-07-08 at 23 29 22" src="https://github.com/zaahirdawood/llm-zoomcamp/assets/109787439/4e5edd5e-d1ef-4203-8285-cae5a23c585a">


**Q4:-** What's the size of the ollama_files/models folder?

```
du -h /root/.ollama/models/
```

**A4:** 
<img width="747" alt="Screenshot 2024-07-08 at 23 38 45" src="https://github.com/zaahirdawood/llm-zoomcamp/assets/109787439/91479808-2bea-425b-b727-72c93c35c5c0">

**Q5:-= Load Gemma:2b model into new container to avoid pulling it each time we run.

**A5:** 

```
FROM ollama/ollama

COPY ./ollama_files /root/.ollama
```

