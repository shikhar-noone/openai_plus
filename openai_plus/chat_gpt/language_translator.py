import openai
openai.api_key = "sk-7y1tjYh8gcf2ubaJXWXoT3BIbkFJkzPuufJn8FJDIpfSj7pW"

def translate_query(query, language):

    try:
        prompt = f"query = '{query}'.Please translate the query into {language} and return statement only."
        print(prompt)
        completions = openai.Completion.create(
            engine="text-davinci-002", 
            prompt=prompt, 
            max_tokens=2048, 
            n=1,
            stop=None,
            temperature=0.5
        )
        print(completions)
        message = completions.choices[0].text
        #print(completions)
        return message
    except Exception as err:
        return f"cant process {query}, your subscription is over."



