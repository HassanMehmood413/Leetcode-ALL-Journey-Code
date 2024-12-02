const readline = require('readline');
const fetch = require('node-fetch');  // Ensure you have node-fetch installed

// Create an interface for user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const generateText = async (userPrompt) => {
    const baseUrl = "https://us-south.ml.cloud.ibm.com"; // Base URL for the us-south region
    const url = `${baseUrl}/ml/v1/text/generation?version=2023-05-29`;

    // Set the headers with your API key
    const headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 0BKzMaKhfUpSjF8qg376QmJ4jK-uYVL_wobtafrbLWJZ"  // Replace with your actual API key
    };

    // Set the body for the request with the user's prompt
    const body = {
        input: userPrompt,
        parameters: {
            decoding_method: "greedy",
            max_new_tokens: 900,
            min_new_tokens: 0,
            stop_sequences: [],
            repetition_penalty: 1
        },
        model_id: "meta-llama/llama-3-8b-instruct",  // The model ID you're using
        project_id: "7a78f733-6524-44ea-bd00-e71314499c69"  // Replace with your actual project ID
    };

    try {
        console.log("Sending request to the API...");

        // Make the API request
        const response = await fetch(url, {
            headers,
            method: "POST",
            body: JSON.stringify(body),
        });

        console.log(`Response Status: ${response.status}`);

        // Check for successful response
        if (!response.ok) {
            throw new Error(`Non-200 response: ${response.statusText}`);
        }

        // Parse the response as JSON
        const result = await response.json();
        console.log("Generated Text:", result);
        return result;
    } catch (error) {
        console.error("Error:", error);
    }
};

// Prompt the user for input
rl.question('Please enter your prompt: ', (userPrompt) => {
    generateText(userPrompt).then(() => {
        rl.close();  // Close the input stream after the response is received
    });
});a
