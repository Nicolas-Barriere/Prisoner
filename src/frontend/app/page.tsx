'use client'
import axios from "axios";
import { useState } from "react";

type Round = {
  p1: string;
  p2: string;
  s1: number;
  s2: number;
};

type GameResult = {
  players: [string, string];
  rounds: Round[];
  score: { [key: string]: number };
};

export default function Home() {
  const [result, setResult] = useState<GameResult | null>(null);
  const [loading, setLoading] = useState(false);

  const play = async () => {
    setLoading(true);
    const res = await axios.post("http://localhost:8000/api/play/");
    setResult(res.data);
    setLoading(false);
  };

  return (
    <main style={{ padding: 32, fontFamily: "sans-serif" }}>
      <h1>Dilemme du Prisonnier — IA vs IA</h1>
      <button onClick={play} disabled={loading}>
        {loading ? "Simulation..." : "Lancer un match"}
      </button>

      {result && (
        <>
          <h2>Résultat final</h2>
          <p>
            {result.players[0]}: {result.score[result.players[0]]} pts |
            {result.players[1]}: {result.score[result.players[1]]} pts
          </p>

          <ul>
            {result.rounds.map((r, i) => (
              <li key={i}>
                Tour {i + 1}: {r.p1} vs {r.p2} → {r.s1}-{r.s2}
              </li>
            ))}
          </ul>
        </>
      )}
    </main>
  );
}
