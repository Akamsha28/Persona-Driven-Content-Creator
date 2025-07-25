import os
import google.generativeai as genai

try:
    genai.configure(api_key="GOOGLE_API_KEY")
except Exception as e:
    print(f"Error configuring API key: {e}")
    exit()

def generate_content(persona_file, topic):
    """
    Generates content based on a persona file and a topic using the Gemini API.
    """
    print(f"--- Generating content for persona: {persona_file} ---")

    try:
        with open(persona_file, 'r') as f:
            system_prompt = f.read()
    except FileNotFoundError:
        return f"Error: Persona file '{persona_file}' not found."

    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-1.5-flash')

        # The system prompt and user topic are sent together
        response = model.generate_content(f"{system_prompt}\n\nTOPIC: {topic}")
        
        # Access the generated text
        return response.text
    except Exception as e:
        return f"An error occurred while generating content: {e}"

# This block runs the code and prints the result.
if __name__ == "__main__":
    my_topic = "The challenge of keeping data pipelines efficient as data volume grows."

    # Call the function to get the content
    linkedin_post = generate_content("my_linkedin_persona.txt", my_topic)
    
    # Print the final result to the console
    print("\n----- Generated LinkedIn Post -----")
    print(linkedin_post)