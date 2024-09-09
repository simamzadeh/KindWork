// GratitudeEntries.tsx
import React, { useEffect, useState } from 'react';
import { useApi } from '../hooks/useApi';

interface User {
  username: string;
}

interface GratitudeEntry {
  id: number;
  content: string;
  user_id: User;
  created_at: string; // or Date if you parse it to a Date object
}

const GratitudeEntriesTest: React.FC = () => {
//   const { fetchWithTokens } = useApi();
  const [entries, setEntries] = useState<GratitudeEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  // Fetch the gratitude entries from the API
  useEffect(() => {
    const fetchEntries = async () => {
      try {
        const response = await fetch('/api/gratitude/');
        if (!response.ok) {
          throw new Error('Failed to fetch entries');
        }
        const data = await response.json();
        setEntries(data); // Set the fetched entries in the state
      } catch (err) {
        setError(error); // Set any errors
      } finally {
        setLoading(false); // Mark the loading as complete
      }
    };

    fetchEntries();
  }, []); // The empty array ensures the effect runs only once, similar to componentDidMount


  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error.message}</p>;

  return (
    <div>
      <h1>Gratitude Entries</h1>
      <ul>
        {entries.map(entry => (
          <li key={entry.id}>
          <strong>Content:</strong> {entry.content} <br />
          <strong>Created at:</strong> {new Date(entry.created_at).toLocaleString()}
        </li>
        ))}
      </ul>
    </div>
  );
};

export default GratitudeEntriesTest;
