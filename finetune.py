import openai

# Define a function to open a file and return its content as a string.
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    
# Define a function to save content to a file
def save_file(filepath, content):
    with open (filepath, 'a' , encoding='utf-8') as outfile:
        outfile.write(content)

# Set the OpenAI API keys by reading them from files
api_key = open_file('openaiapikey.txt')
openai.api_key = api_key

# Assuming the file name is 'convsersations.jsonl'
with open("/Users/yuvraj/Documents/University Files/Srivastava Lab/HIV-Chatbot/conversations.jsonl", "rb") as file:
    response = openai.File.create(
        file=file, 
        purpose= 'fine-tune'
    )

file_id = response['id']
print(f"File uploaded successfully with ID: {file_id}")