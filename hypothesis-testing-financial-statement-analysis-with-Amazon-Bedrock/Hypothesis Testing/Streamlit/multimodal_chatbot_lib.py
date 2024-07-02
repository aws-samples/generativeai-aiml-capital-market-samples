import boto3
import json
import base64
from io import BytesIO

MAX_MESSAGES = 20

class ChatMessage(): #create a class that can store image and text messages
    def __init__(self, role, message_type, text, bytesio=None):
        self.role = role
        self.message_type = message_type
        self.text = text
        self.bytesio = bytesio

#get a BytesIO object from file bytes
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io

#get a base64-encoded string from file bytes
def get_base64_from_bytes(image_bytes):
    resized_io = get_bytesio_from_bytes(image_bytes)
    img_str = base64.b64encode(resized_io.getvalue()).decode("utf-8")
    return img_str

#load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes
    

def convert_chat_messages_to_messages_api(chat_messages):
    
    messages = []
    
    for chat_msg in chat_messages:
        if (chat_msg.message_type == 'image'):
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": chat_msg.text,
                        },
                    }
                ]
            })
        else:
            messages.append({
                "role": chat_msg.role,
                "content": [
                    {
                        "type": "text",
                        "text": chat_msg.text
                    }
                ]
            })
            
    return messages

#get the stringified request body for the InvokeModel API call
def get_multimodal_chat_request_body(chat_messages):
    
    messages = convert_chat_messages_to_messages_api(chat_messages)
    
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 40000,
        "temperature": 0,
        "messages": messages,
    }
    
    return json.dumps(body)

#generate a response using Anthropic Claude
def chat_with_model(message_history, new_text=None, new_image_bytes=None):
    session = boto3.Session()
    
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    if new_text:
        new_text_message = ChatMessage('user', 'text', text=new_text)
        message_history.append(new_text_message)
        
    elif new_image_bytes:
        image_bytesio = get_bytesio_from_bytes(new_image_bytes)
        image_base64 = get_base64_from_bytes(new_image_bytes)
        new_image_message = ChatMessage('user', 'image', text=image_base64, bytesio=image_bytesio)
        message_history.append(new_image_message)
    
    
    number_of_messages = len(message_history)
    
    if number_of_messages > MAX_MESSAGES:
        del message_history[0 : (number_of_messages - MAX_MESSAGES) * 2] #make sure we remove both the user and assistant responses
    
    
    body = get_multimodal_chat_request_body(message_history)
    
    response = bedrock.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0", contentType="application/json", accept="application/json")
    
    response_body = json.loads(response.get('body').read()) # read the response
    
    output = response_body['content'][0]['text']
    
    response_message = ChatMessage('assistant', 'text', output)
    
    message_history.append(response_message)
    
    return
