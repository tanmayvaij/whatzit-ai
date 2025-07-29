# Whatzit AI

A FastAPI-based web service that generates random structured data using Google's Gemini AI model. Whatzit AI can create realistic objects of any category with unique IDs, names, and descriptions.

## 🚀 Features

- **AI-Powered Generation**: Uses Google's Gemini AI model for intelligent data generation
- **RESTful API**: Clean, documented API endpoints with automatic OpenAPI documentation
- **Flexible Categories**: Generate data for any category (products, books, food, etc.)
- **Structured Output**: Consistent JSON responses with validated data
- **Easy to Use**: Simple HTTP endpoints with optional parameters

## 🛠️ Tech Stack

- **FastAPI** - Modern, fast web framework for building APIs
- **Google GenAI** - Official Google Generative AI client library
- **LangChain** - Framework for developing applications powered by language models
- **Pydantic** - Data validation and settings management
- **Uvicorn** - ASGI server for production deployment
- **Python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI API key
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanmayvaij/whatzit-ai.git
   cd whatzit-ai
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_MODEL=<gemini-model-name>
   GEMINI_API_KEY=<gemini-api-key>
   ```
   
   **Note**: You'll need to obtain a Google AI API key and configure it according to Google's documentation.

## 🚀 Running the Application

### Development Mode
```bash
uvicorn main:app --reload
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## 🔌 API Endpoints

### 1. Welcome Endpoint

**GET** `/`

Returns a welcome message from the AI system.

**Response:**
```json
{
  "message": "Welcome to Whatzit AI! I'm your random data generator..."
}
```

### 2. Generate Data Endpoint

**GET** `/generate/sample`

Generates random objects of a specified category.

**Parameters:**
- `category` (string, required): The type of objects to generate
- `num` (integer, optional): Number of objects to generate (default: 8)

**Example Request:**
```
GET /generate/sample?category=electronics&num=5
```

**Response:**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Wireless Bluetooth Headphones",
    "description": "High-quality wireless headphones with noise cancellation"
  },
  {
    "id": "550e8400-e29b-41d4-a716-446655440001",
    "name": "Smart LED Desk Lamp",
    "description": "Adjustable brightness desk lamp with touch controls"
  }
  // ... more objects
]
```

> **Note:** All API responses are strictly valid JSON with no markdown or code blocks, as enforced by the prompt templates.

## 💡 Usage Examples

### Generate Electronics
```bash
curl "http://localhost:8000/generate/sample?category=electronics&num=3"
```

### Generate Books
```bash
curl "http://localhost:8000/generate/sample?category=books&num=10"
```

### Generate Food Items
```bash
curl "http://localhost:8000/generate/sample?category=food&num=5"
```

### Get Welcome Message
```bash
curl "http://localhost:8000/"
```

## 🔒 Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GEMINI_MODEL` | Google Gemini model to use | Yes | - |
| `GEMINI_API_KEY` | Google Gemini API Key | Yes | - |

## 🏗️ Project Structure

```
whatzit-ai/
├── main.py              # Main FastAPI application
├── agent.py             # Agent logic for interacting with Gemini AI
├── models.py            # Pydantic models for API responses
├── prompt_templates.py  # Prompt templates for the AI
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker container setup
├── .gitignore           # Git ignore rules
├── README.md            # This file
├── venv/                # Virtual environment (not in repo)
├── __pycache__/         # Python cache (not in repo)
└── .git/                # Git repository
```

## 🧪 Testing

You can test the API using:
- The interactive docs at `/docs`