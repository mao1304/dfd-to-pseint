# DFD to PSeInt Translator

This project provides a tool to translate Data Flow Diagrams (DFD) into PSeInt pseudocode using machine learning. It offers both local (Docker) and cloud (Google Colab) deployment options.

## Features

- Translates DFD files into PSeInt pseudocode
- Web API endpoint for easy integration
- Pre-trained model included
- Supports both local and cloud execution

## Deployment Options

### Option 1: Google Colab (Recommended for quick testing)

1. **Open the Notebook**:
   - Go to [Google Colab](https://colab.research.google.com/)
   - Upload `google-colab/dfd_to_pseint_translate.ipynb` from this repository
   - upload dataset.csv into colab, and run for train de model
  
     1.1 **if you do not want to run your own model load the model into best-model, place it in a folder, and make sure the path in the code corresponds to the location of the “best-model” folder.**

2. **Run the Notebook**:
   - Execute all cells sequentially (Runtime > Run all)
   - The API will start automatically on port 5000

3. **Access the Interface**:
   - load the index.html file found in the extra folder 
   - Use the URL provided by Colab after running the last cell
   - Upload `.dfd` files to get translated PSeInt code

### Option 2: Local Docker Deployment

1. **Prerequisites**:
   - Install [Docker](https://docs.docker.com/get-docker/)
   - Install [Docker Compose](https://docs.docker.com/compose/install/)

2. **Setup**:
   ```bash
   git clone https://github.com/mao1304/dfd-to-pseint.git
   cd dfd-to-pseint/local

3. **Run the Application**:
   docker-compose up --build
   
5. **Access the API**:
  Web interface: http://localhost:5000
  API endpoint: http://localhost:5000/translate

## API Usage
**Endpoints**

POST /translate - Upload a DFD file
  Input: .dfd file
  Output: .txt file with PSeInt code

GET /test - API status check

**Example Requests into colab**
import requests

url = "http://localhost:5000/translate"
files = {"file": open("diagram.dfd", "rb")}
response = requests.post(url, files=files)

with open("output.txt", "wb") as f:
    f.write(response.content)

.
## 📂 Project Structure

📁 google-colab/ # Colab implementation
│ ├── dfd_to_pseint_translate.ipynb
│ └── dfd_to_pseint_translate.py
│
📁 local/ # Local deployment
│ ├── app/
│ │ ├── app.py # Flask application
│ │ └── templates/
│ │ └── index.html # Web interface
│ ├── .dockerfile
│ ├── constants.py
│ ├── docker-compose.yml
│ ├── helpers.py
│ └── requirements.txt
│
📁 extra/ # Additional resources
│ ├── dataset.csv # Training data
│ └── index.html # Interface for Google Colab
    
## Model Information
Metric	Score
ROUGE-L F1	36.36%
Keyword Match	66.67%
Structure Similarity Score: 66.67%

## 🎥 Video Demostración

[![Cómo usar DFD to PSeInt Translator](https://img.youtube.com/vi/6rLExoJoZIE/0.jpg)](https://youtu.be/6rLExoJoZIE)


## License
MIT License - See LICENSE for details.

For questions or issues, please open an issue on the GitHub repository.

if you want to update or work with this project do not hesitate to do so.

## 👨‍💻 Developer

This project is developed and maintained by [@mao1304](https://github.com/mao1304).

**Want to contribute?**  
Feel free to fork this repository and submit pull requests! All improvements and suggestions are welcome.


