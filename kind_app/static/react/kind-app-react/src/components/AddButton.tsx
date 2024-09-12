import React from 'react';
import { Fab } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

interface AddButtonProps {
  onClick: () => void; // Define a callback for the button click
}

const AddButton: React.FC<AddButtonProps> = ({ onClick }) => {
  return (
    <Fab
      color="primary"
      aria-label="add"
      onClick={onClick}
    >
      <AddIcon />
    </Fab>
  );
};

export default AddButton;
