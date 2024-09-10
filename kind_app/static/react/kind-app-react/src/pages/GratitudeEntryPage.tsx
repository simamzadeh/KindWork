import React, { useEffect, useState } from 'react';
import { List, ListItem, ListItemText, Typography, Container, CircularProgress } from '@mui/material';

interface GratitudeEntry {
  id: number;
  content: string;
  created_at: string;
}

const GratitudeList: React.FC = () => {
  const [entries, setEntries] = useState<GratitudeEntry[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

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
  }, []);

  if (loading) {
    return (
      <Container>
        <CircularProgress />
        <Typography variant="h6">Loading...</Typography>
      </Container>
    );
  }

  if (error) {
    return (
      <Container>
        <Typography color="error">{error}</Typography>
      </Container>
    );
  }

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Gratitude Entries
      </Typography>
      <List>
        {entries.map((entry) => (
          <ListItem key={entry.id}>
            <ListItemText
              primary={entry.content}
              secondary={`Created at: ${new Date(entry.created_at).toLocaleString()}`}
            />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default GratitudeList;
