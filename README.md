# Structured Outputs with Pydantic

This repository contains my learning exercise on generating **structured JSON outputs** from a Large Language Model (LLM) using the **Groq API** and validating the response using **Pydantic**.

The objective of this lesson is to understand how LLMs can return machine-readable JSON instead of plain text and how to parse and validate that data in Python.

---

## Learning Objectives

In this lesson, I learned how to:

- Generate structured JSON responses from an LLM
- Define schemas using Pydantic
- Validate AI-generated responses
- Parse JSON into Python objects
- Extract structured information from unstructured customer text

---

## Concepts Covered

### 1. Pydantic Models

Pydantic provides data validation using Python type hints.

Example:

```python
class Ticket(BaseModel):
    name: str
    email: str
    issue: str
```

The model defines the expected JSON structure returned by the LLM.

---

### 2. JSON Schema

Pydantic automatically generates a JSON schema.

```python
schema = Ticket.model_json_schema()
```

The schema is included in the system prompt to guide the model toward producing valid JSON.

---

### 3. System Prompt

The system prompt instructs the LLM to follow the generated schema.

```python
system_prompt = f"""
Extract the personal information of the customer
strictly based on the following schema:

{schema}

Return only valid JSON.
"""
```

---

### 4. JSON Output

The Groq API is instructed to return JSON using:

```python
response_format = {
    "type": "json_object"
}
```

---

### 5. Parsing JSON

The JSON response is converted into a Python dictionary.

```python
parsed_json = json.loads(answer)
```

---

### 6. Pydantic Validation

The parsed JSON is validated using the Pydantic model.

```python
ticket = Ticket(**parsed_json)
```

Now each field can be accessed like a normal Python object.

```python
print(ticket.name)
print(ticket.email)
print(ticket.issue)
```

---

## Technologies Used

- Python
- Groq Python SDK
- Pydantic
- python-dotenv
- JSON

---

## Folder Structure

```text
day4-structured-output/
│
├── json_pydantic.py
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Sample Input

```
I purchased a SmartX Bluetooth speaker last month, but it frequently disconnects from my phone...

My name is Aarav Mehta.

My email address is aarav.mehta482@example.com.
```

---

##  Sample JSON Output

```json
{
  "name": "Aarav Mehta",
  "email": "aarav.mehta482@example.com",
  "issue": "SmartX Bluetooth speaker frequently disconnects from the phone and its battery drains within an hour despite a full charge."
}
```
