'use client';

import { useState } from 'react';
import axios from 'axios';

type Round = {
  p1: 'C' | 'D';
  p2: 'C' | 'D';
  s1: number;
  s2: number;
};

export default function Home() {
  const [rounds, setRounds] = useState<Round[]>([]);
  const [players] = useState(['GPT', 'Mistral']);
  const [loading, setLoading] = useState(false);
  const [scores, setScores] = useState({ GPT: 0, Mistral: 0 });

  const playMatch = async () => {
    setLoading(true);
    setRounds([]);
    setScores({ GPT: 0, Mistral: 0 });
    const game = await axios.post('http://localhost:8000/api/new_game/');
    const game_id = game.data.game_id;

    let currentScores = { GPT: 0, Mistral: 0 };
    for (let i = 0; i < 10; i++) {
      const res = await axios.post('http://localhost:8000/api/next_round/', { game_id });
      const roundData = res.data;
      console.log(roundData);
      setRounds((prev) => [...prev, {
        p1: roundData.p1,
        p2: roundData.p2,
        s1: roundData.scores.GPT - scores.GPT,
        s2: roundData.scores.Mistral - scores.Mistral,
      }]);

      currentScores = {
        GPT: roundData.scores.GPT,
        Mistral: roundData.scores.Mistral,
      };
      setScores(currentScores);

      await new Promise((resolve) => setTimeout(resolve, 400));
      if (roundData.finished) break;
    }
    setLoading(false);
  };

  return (
    <main className="p-6 font-mono">
      <h1 className="text-3xl font-bold mb-4">Dilemme du Prisonnier - Match IA</h1>

      <button
        className="bg-blue-600 text-white px-4 py-2 rounded disabled:opacity-50"
        onClick={playMatch}
        disabled={loading}
      >
        {loading ? 'Match en cours...' : 'Lancer le match'}
      </button>

      <div className="mt-6">
        <h2 className="text-xl font-semibold mb-2">Scores</h2>
        <p>GPT: {scores.GPT}</p>
        <p>Mistral: {scores.Mistral}</p>
      </div>

      <div className="mt-6">
        <h2 className="text-xl font-semibold mb-2">Rounds</h2>
        <table className="w-full text-left border">
          <thead>
            <tr>
              <th className="border px-2">#</th>
              <th className="border px-2">GPT</th>
              <th className="border px-2">Mistral</th>
              <th className="border px-2">+GPT</th>
              <th className="border px-2">+Mistral</th>
            </tr>
          </thead>
          <tbody>
            {rounds.map((r, i) => (
              <tr key={i}>
                <td className="border px-2">{i + 1}</td>
                <td className="border px-2">{r.p1}</td>
                <td className="border px-2">{r.p2}</td>
                <td className="border px-2">{r.s1}</td>
                <td className="border px-2">{r.s2}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </main>
  );
}
