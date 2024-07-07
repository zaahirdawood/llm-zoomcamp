from openai import OpenAI

    
client = OpenAI(
base_url='http://localhost:11434/d2/', #http://localhost:11434/v1/
api_key='ollama'
)

def main():
    prompt = "What's the formula for energy?"
    response = llm(prompt)
    return response
    

def llm(prompt):
    response = client.chat.completions.create(
        model='ollama-gemma2b', #gemma:2b, ollama-gemma2b
        messages=[{"role": "user","content": prompt}],
        temperature=0.0
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    main()