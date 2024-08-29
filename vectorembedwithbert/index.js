import axios from "axios";

const HUGGING_FACE_API_KEY = "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";

async function getBertEmbeddings(data) {
    try {
        const response = await axios.post(
            "https://api-inference.huggingface.co/models/bert-base-uncased",
            {
                headers: {
                    Authorization: `Bearer ${HUGGING_FACE_API_KEY}`,
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data)
            },
        );
        console.log(response.data);
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 429) {
            console.error('Rate limit reached. Please check your API usage or upgrade your plan.');
        } else {
            console.error('Error fetching BERT embeddings:', error.response ? error.response.data : error.message);
        }
    }
}

const text = {"text":'how are [MASK]'};
const data = {"inputs": "The answer to the universe is [MASK]."}
const vector = getBertEmbeddings(text);
console.log(vector);