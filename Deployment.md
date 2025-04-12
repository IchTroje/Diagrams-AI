# Guide how to build and deploy app

### 1. Move to ```backend/``` directory in the project directory
```bash
cd backend/
```


### 2. Build Django server Docker image
```bash
docker build -t diagrams-backend-django .
```

### 3. Run newly created Docker image 
```bash
docker run -p 8000:8000 diagrams-backend-django
```

### 4. Combined commands
```bash
cd backend/ && docker build -t diagrams-backend-django . && docker run -p 8000:8000 diagrams-backend-django
```