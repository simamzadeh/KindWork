import React, { useState } from 'react';
import { Dialog, DialogTitle, DialogContent, DialogActions, TextField, Button } from '@mui/material';

interface KudosEntryFormProps {
  open: boolean;
  onClose: () => void;
  onSubmit: (content: string) => void;
}

const KudosEntryForm: React.FC<KudosEntryFormProps> = ({ open, onClose, onSubmit }) => {
  const [content, setContent] = useState<string>('');

  const handleSubmit = () => {
    onSubmit(content);
    setContent(''); // Clear the input field
    onClose(); // Close the dialog
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Add Entry</DialogTitle>
      <DialogContent>
        <TextField
          autoFocus
          margin="dense"
          label="Content"
          fullWidth
          variant="outlined"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="primary">
          Cancel
        </Button>
        <Button onClick={handleSubmit} color="primary">
          Submit
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default KudosEntryForm;
