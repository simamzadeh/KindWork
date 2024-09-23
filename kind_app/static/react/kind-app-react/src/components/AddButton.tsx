import React from 'react';
import { Button } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

interface AddButtonProps {
  onClick: () => void; // Define a callback for the button click
}

const AddButton: React.FC<AddButtonProps> = ({ onClick }) => {
  return (
    <Button
      variant="contained"
      color="primary"
      startIcon={<AddIcon />} // Add the icon as a start icon
      onClick={onClick}
    >
      New Entry
    </Button>
  );
};

export default AddButton;
