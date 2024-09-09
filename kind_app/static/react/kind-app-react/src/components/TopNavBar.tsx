import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { Divider } from '@mui/material';

export default function TopNavBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: '#9CBA9B' }}>
        <Toolbar>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
          <Button color='inherit'>Gratitude Entries</Button>
          <Divider orientation='vertical' variant="middle" flexItem />
          <Button color='inherit'>Mood Log</Button>
          <Divider orientation='vertical' variant="middle" flexItem />
          <Button color='inherit' >Login</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}