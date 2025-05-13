import google.generativeai as genai
def callGeminiAPI(prompt):
    # Set the API key
    genai.configure(api_key="AIzaSyCIdC6hLcQwNRNyIHQrtq7HFgodd9Bwv4c")
    model=genai.GenerativeModel('models/gemini-2.0-flash')
    # Call the API with the prompt
    response=model.generate_content(prompt)
    # Print the response
    print(response)
#calling the function
prompt=input("Enter the prompt: ")
callGeminiAPI(prompt)
