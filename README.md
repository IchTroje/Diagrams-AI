# Diagrams-AI

### External BPMN rendering
```mermaid
sequenceDiagram
BPMN.js <<-->> User: Request to external service to render BPMN chart
User ->> Django Server: Description of BPMN chart (text or PDF)
Django Server ->> LLM: Pre-processed text user input
LLM ->> Django Server: BPMN chart in XML format
Django Server ->> User: BPMN chart in XML format
```

### In-app BPMN rendering with separate front-end server
```mermaid
sequenceDiagram
User ->> Frontend Server: All frontend interactions
Frontend Server ->> Django Server: Description of BPMN chart (text or PDF)
Django Server ->> LLM: Pre-processed text user input
LLM ->> Django Server: BPMN chart in XML format
Django Server ->> Frontend Server: BPMN chart in XML format
Frontend Server ->> User: Rendering of BPMN chart
```

## Tech Stack
 - Backend:
    - Python
    - Flask/Django
    - Pytest, Unittest
    - Docker
 - Frontend:
    - HTML
    - CSS
    - JavaScript
    - BPMN.js

 ## Roles in the project:
  - Dawid Stasiński:
    - Project Manager
    - IT Architekt
    - Developer
    - Tester
 - Bruno Maruwka:
    - Test Manager
    - Developer
    - Tester
 - Mateusz Wójcicki:
    - Business Analyst
    - Developer
    - Tester

## Rescources:
 - [Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources)
 - [BPMN.js](https://bpmn.io/toolkit/bpmn-js/)