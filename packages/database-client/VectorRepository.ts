import { Pool } from 'pg';

export class VectorRepository {
  /** Raw SQL integration for high-performance HNSW search (1536D) */
  constructor(private pool: Pool) {}

  async findSimilarAgents(queryVector: number[]) {
    const vectorStr = `[${queryVector.join(',')}]`;
    // Operator <=> to Cosine Distance w pgvector
    return this.pool.query(
      'SELECT id, 1 - (embedding <=> $1) as ARI_Sim FROM agents ORDER BY embedding <=> $1 LIMIT 5',
      [vectorStr]
    );
  }
}
