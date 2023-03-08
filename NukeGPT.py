import nuke

def ui(script):
    n = nuke.createNode("NoOp", "name NukeGPT")
    n.addKnob(nuke.Text_Knob("","GPT"))
    n.addKnob(nuke.Multiline_Eval_String_Knob("txt", "txt", "Create 3 blur nodes"))
    n.addKnob(nuke.Multiline_Eval_String_Knob("code", "code",))
    n.addKnob(nuke.PyScript_Knob("run_script", "Run AI", script.__name__ + "()"))
    n.addKnob(nuke.nuke.String_Knob("API key","API key",""))

def script():
    import requests
    import json
    import os
    import nuke

    node = nuke.thisNode()

    api_endpoint = 'https://api.openai.com/v1/engines/text-davinci-002/completions'
    api_key = node["API key"].value()


    txt_value = node["txt"].value()
    prompt = "Generate a python script in Nuke that will " + node["txt"].value() + "\nAlways follow the following rules:\n1- Don't use the import statement\n2- Only generate executable code\n3- Make sure the code don't have incorrect indents or extra spaces\n4- Keep the comments on the code short under 10 words"
    print(prompt)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 2048,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
    }
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers=headers,
        data=json.dumps(data),
    )
    response_text = response.text
    response_json = json.loads(response_text)

    print(response_json)
    aicode = response_json["choices"][0]["text"].strip()

    print(aicode)
    node["code"].setValue(aicode)
    exec(aicode)

ui(script)
