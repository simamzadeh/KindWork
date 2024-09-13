import React, { useState } from 'react';
import { Button, Menu, MenuItem, IconButton } from '@mui/material';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';


interface ActionButtonProps {
    onEdit: () => void;
    onDelete: () => void;
    disableEdit: boolean;
    disableDelete: boolean;
  }

const ActionButton: React.FC<ActionButtonProps> = ({ onEdit, onDelete, disableEdit, disableDelete }) => {
  const [anchorElement, setAnchorElement] = useState<null | HTMLElement>(null);

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorElement(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorElement(null);
  };

  const handleEdit = () => {
    onEdit();
    handleClose();
  };

  const handleDelete = () => {
    onDelete();
    handleClose();
  };

  return (
    <>
      <Button
        variant="contained"
        endIcon={<ArrowDropDownIcon />}
        onClick={handleClick}
      >
        Actions
      </Button>
      <Menu
        anchorEl={anchorElement}
        open={Boolean(anchorElement)}
        onClose={handleClose}
      >
        <MenuItem onClick={onEdit} disabled={disableEdit}>Edit</MenuItem>
        <MenuItem onClick={onDelete} disabled={disableDelete}>Delete</MenuItem>
      </Menu>
    </>
  );
};

export default ActionButton;
