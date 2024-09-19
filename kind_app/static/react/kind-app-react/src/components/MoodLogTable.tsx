import React, { useEffect, useState } from 'react';
import {
  Box,
  Container,
  Checkbox,
  Typography,
  CircularProgress,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from '@mui/material';
import AddButton from './AddButton';
import ActionButton from './ActionButton';
import MoodLogForm from './MoodLogForm';
import { useAuth } from '../context/AuthContext';

interface MoodLog {
  id: number
  mood: string;
  created_at: string;
}

const moodLabelMap: { [key: string]: string } = {
    'very unpleasant': 'Very Unpleasant',
    'unpleasant': 'Unpleasant',
    'neutral': 'Neutral',
    'pleasant': 'Pleasant',
    'very pleasant': 'Very Pleasant',
};

const MoodLogTable: React.FC = () => {
  const { csrfToken } = useAuth(); // Use the CSRF token from context
  const [entries, setEntries] = useState<MoodLog[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [showForm, setShowForm] = useState<boolean>(false);
  const [selectedIds, setSelectedIds] = useState<Set<number>>(new Set());
  const [editingEntry, setEditingEntry] = useState<MoodLog | null>(null); // To track which entry is being edited

  useEffect(() => {
    const fetchEntries = async () => {
      try {
        const response = await fetch('/api/mood-log/');
        if (!response.ok) {
          throw new Error('Failed to fetch entries');
        }
        const data = await response.json();
        setEntries(data); // Set the fetched entries in the state
      } catch (err) {
        setError((err as Error).message); // Set any errors
      } finally {
        setLoading(false); // Mark the loading as complete
      }
    };

    fetchEntries();
  }, []);

  const handleAddClick = () => {
    setShowForm(true);
  };

  const handleFormClose = () => {
    setShowForm(false);
  };

  const handleFormSubmit = async (mood: string) => {
    try {
      if (editingEntry) {
        // Update existing entry (Edit case)
        const response = await fetch(`/api/mood-log/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken || '',
          },
          body: JSON.stringify({ 
            id: editingEntry.id,
            mood, 
          }),
        });

        if (!response.ok) {
          throw new Error('Failed to update entry');
        }

        const updatedEntry = await response.json();
        setEntries((prevEntries) =>
          prevEntries.map((entry) =>
            entry.id === updatedEntry.id ? updatedEntry : entry
          )
        );
      } else {
        // Add new entry (Add case)
        const selectedMood = mood.toLowerCase().replace(/\s/g, ''); // Format mood to match the backend
        const response = await fetch('/api/mood-log/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken || '',
          },
          body: JSON.stringify({ mood }),
        });

        if (!response.ok) {
          throw new Error('Failed to add entry');
        }

        const newEntry = await response.json();
        setEntries((prevEntries) => [...prevEntries, newEntry]);
      }
    } catch (err) {
      console.error(err);
    }

    handleFormClose();
  };

  const handleDeleteEntry = async (id: number) => {
    try {
      const response = await fetch(`/api/mood-log/`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken || '',
        },
        body: JSON.stringify({
          ids: Array.from(selectedIds),  // Send selectedIds as an array
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to delete entry');
      }

      setEntries((prevEntries) => prevEntries.filter((entry) => entry.id !== id));
    } catch (err) {
      console.error(err);
    }
    setSelectedIds(new Set()); // Clear selection after delete
  };

  const handleEditAction = () => {
    const selectedEntry = entries.find((entry) => selectedIds.has(entry.id));
    if (selectedEntry) {
      setEditingEntry(selectedEntry); // Set the selected entry for editing
      setShowForm(true); // Open the form
    }
  };

  const handleDeleteAction = () => {
    const selectedEntry = entries.find((entry) => selectedIds.has(entry.id));
    if (selectedEntry) {
      handleDeleteEntry(selectedEntry.id);
    }
  };

  const handleSelectAllClick = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.checked) {
      setSelectedIds(new Set(entries.map((entry) => entry.id)));
    } else {
      setSelectedIds(new Set());
    }
  };

  const handleRowClick = (id: number) => {
    const newSelectedIds = new Set(selectedIds);
    if (newSelectedIds.has(id)) {
      newSelectedIds.delete(id);
    } else {
      newSelectedIds.add(id);
    }
    setSelectedIds(newSelectedIds);
  };

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
      <Box mb={2} display="flex" alignItems="center" justifyContent="space-between">
        <Typography variant="h4" gutterBottom>
          Mood Log
        </Typography>
        <Box>
            <AddButton onClick={handleAddClick} />
            <ActionButton
              onEdit={handleEditAction}
              onDelete={handleDeleteAction}
              disableEdit={selectedIds.size !== 1}    // Disable Edit if not exactly one item is selected
              disableDelete={selectedIds.size === 0}  // Disable actions if no items are selected
            />
        </Box>
      </Box>
      
      
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell padding="checkbox">
                <Checkbox
                  checked={entries.length > 0 && selectedIds.size === entries.length}
                  onChange={handleSelectAllClick}
                />
              </TableCell>
              <TableCell>ID</TableCell>
              <TableCell>Mood</TableCell>
              <TableCell>Created At</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {entries.map((entry) => (
              <TableRow 
                key={entry.id}
                hover
                onClick={() => handleRowClick(entry.id)}
                selected={selectedIds.has(entry.id)}
              >
                <TableCell padding="checkbox">
                  <Checkbox
                    checked={selectedIds.has(entry.id)}
                    onChange={() => handleRowClick(entry.id)}
                  />
                </TableCell>
                <TableCell>{entry.id}</TableCell>
                <TableCell>{moodLabelMap[entry.mood] || entry.mood}</TableCell>
                <TableCell>
                  {new Date(entry.created_at).toLocaleString()}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <MoodLogForm
        open={showForm}
        onClose={handleFormClose}
        onSubmit={handleFormSubmit}
      />
    </Container>
  );
};

export default MoodLogTable;
