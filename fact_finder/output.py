import google.generativeai as genai

# Set up the Gemini API client
def gem(summary):
	genai.configure(api_key="AIzaSyDUl_6Ll4iamZy7gp9Ipv4uc_EbFMRxqHk")

	# Create a GenerativeModel object
	model = genai.GenerativeModel('gemini-pro')

	# Set the prompt
	prompt = f"Confirm if {summary}, with various sources also provide links for the resources"

	# Generate a response from the model
	response = model.generate_content(prompt)
	# Print the response
	print(response.text) 	