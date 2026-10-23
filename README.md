# retail-pulse: Real-time Retail Lakehouse + LLM Personalization

> End-to-end retail data platform on GCP Free Tier - GCS + Pub/Sub + BigQuery + Vertex AI

## Architecture
Local Producer -> GCS Raw -> Pub/Sub -> BigQuery Bronze/Silver/Gold -> Vertex AI Embeddings -> Vector Search

## Tech Stack
- Ingestion: Python, GCS, Pub/Sub
- Processing: PySpark, Delta Lake, BigQuery, SCD2
- LLM: Vertex AI Embeddings, RAG, Text-to-SQL
- Cost: $0 - GCP Free Tier

## How to Run
```bash
python producer/gcs_producer.py

Author
Anjali - Data Engineer

```