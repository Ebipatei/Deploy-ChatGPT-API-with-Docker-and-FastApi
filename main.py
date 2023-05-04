import openai
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel
import uvicorn

load_dotenv()

app = FastAPI()

openai.api_key = "YOUR_OPENAI_API_KEY"

@app.get("/")
async def root():
    return {"message": "It's working!"}  #this get request isn't necessary and can be omitted completely. It's just a webpage that prints a message on the screen to show that it's working.

class UserData(BaseModel):
    prompt: str

chat_history = [] #list to store the chat history for context. Can be replaced by a database
#chat_history = [{"role": "system", "content": f"You are a clinical therapist"}] #uncomment this line if you wanna precondition chatgpt, e.g you want it to be a therapist.

'''roles:
    system = conditioned chatgpt e.g a therapist as opposed a general assistant
    user = you
    assistant = chatgpt
'''


@app.post("/generate")
async def chatgpt(prompt: UserData):
    chat_history.append({"role": "user", "content": f"{prompt}"})  #append the user's prompts to chat history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )
    response_text = response.choices[0]['message']['content'].replace('\n','  ')
    if response_text:
        chat_history.append({"role": "assistant", "content": f"{response_text}"})   #append chatgpt's response to chat history
        return {response_text}
    else:
        raise HTTPException(status_code=404, detail="Response not found.")


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000) #uncomment these two lines to run locally
