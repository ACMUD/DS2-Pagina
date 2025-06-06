FROM python:3.12.3-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install -U scikit-learn

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "src/main.py"]