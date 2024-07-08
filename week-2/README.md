## Homework Week 2

**Q:** What's the version of ollama client?

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

### Step 3 check which Ollama Version
```
ollama -v
```

**A:** 
<img width="782" alt="Screenshot 2024-07-08 at 23 21 40" src="https://github.com/zaahirdawood/llm-zoomcamp/assets/109787439/a7fbddfe-bd3c-4012-8016-e1baf425465c">
