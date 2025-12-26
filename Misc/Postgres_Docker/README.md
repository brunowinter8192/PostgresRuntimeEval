# PostgreSQL Docker Setup for TPC-H

## Prerequisites
- Docker installed
- TPC-H data generated (see main repo README)

## Setup

1. **Create `.env` file**
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` file**
   ```bash
   # Set your repository base path
   REPO_BASE_PATH=/absolute/path/to/2025_2026
   
   # Set PostgreSQL credentials
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_secure_password
   POSTGRES_DB=tpch
   ```

3. **Start the container**
   ```bash
   docker-compose up -d
   ```

4. **Verify connection**
   ```bash
   docker exec -it tpch-postgres psql -U <your_username> -d tpch -c "\dt"
   ```

## Configuration

The PostgreSQL instance is configured for data warehouse workloads with:
- 48GB RAM system
- 14 CPUs
- SSD storage
- Optimized for analytical queries (TPC-H)

Configuration based on [PGTune](https://pgtune.leopard.in.ua/) recommendations.

## Container Management

```bash
# Start container
docker-compose up -d

# Stop container
docker-compose down

# View logs
docker logs -f tpch-postgres

# Access PostgreSQL CLI
docker exec -it tpch-postgres psql -U <your_username> -d tpch
```
