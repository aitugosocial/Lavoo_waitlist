# Stage 1: Build Frontend
FROM node:18-alpine AS frontend-builder

WORKDIR /app

# Copy frontend configuration files
COPY package.json package-lock.json ./
COPY tsconfig.json tsconfig.node.json tsconfig.app.json vite.config.ts ./

# Install dependencies and build
RUN npm ci
COPY src ./src
COPY index.html ./
COPY postcss.config.ts tailwind.config.ts eslint.config.ts ./
RUN npm run build

# Stage 2: Setup Backend
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed (e.g. for psycopg2)
# libpq-dev is often needed for psycopg2, though psycopg2-binary usually avoids this. 
# We'll stick to basic slim for now.

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY api ./api
COPY db ./db
COPY main.py .

# Copy built frontend assets from previous stage to 'out' directory
COPY --from=frontend-builder /app/out ./out

# Expose port (Railway will override this with $PORT, but good for documentation)
EXPOSE 8000

# Start command
# Using shell form to properly expand $PORT provided by Railway
CMD uvicorn api:app --host 0.0.0.0 --port $PORT
