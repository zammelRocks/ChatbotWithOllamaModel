import { useState } from 'react';
import './App.css';

function App() {
    const [input, setInput] = useState('');
    const [response, setResponse] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await fetch('http://localhost:3003/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ prompt: input }),
            });

            const data = await res.json();
            // Process response text to clean and format it
            const formattedResponse = formatResponse(data.response);
            setResponse(formattedResponse);
        } catch (error) {
            console.error('Error:', error);
            setResponse('Error generating response');
        }
    };

    const formatResponse = (responseText) => {
        // Replace Markdown symbols (like **bold** and numbers for lists)
        let formattedText = responseText;

        // Convert bold (**) to <strong> for bold text
        formattedText = formattedText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        
        // Convert numbered lists (1., 2., ...) to <ol> and <li> tags
        formattedText = formattedText.replace(/(\d+\.)\s(.*?)(?=\n|$)/g, (match, number, text) => {
            return `<li>${text}</li>`;
        });

        // Convert newlines into <br /> for line breaks
        formattedText = formattedText.replace(/\n/g, '<br />');
        
        // Convert bullet points (- or *) to <ul><li> for lists
        formattedText = formattedText.replace(/(^|\n)(-|\*)\s(.*?)(?=\n|$)/g, (match, newline, bullet, text) => {
            return `<ul><li>${text}</li></ul>`;
        });

        return formattedText;
    };

    return (
        <div className="chatbot-container">
            {/* Response Section */}
            <div className="flex-grow p-4 overflow-y-auto">
                {response && (
                    <div className="response-container">
                        <div
                            className="response-content"
                            dangerouslySetInnerHTML={{ __html: response }}
                        />
                    </div>
                )}
            </div>
            <h2> Chat with me!</h2>

            {/* Input Form Section */}
            <form className="chatbot-form" onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your message here..."
                    className="chatbot-input"
                />
                <button
                    type="submit"
                    className="chatbot-button"
                >
                    Send
                </button>
            </form>
        </div>
    );
}

export default App;
