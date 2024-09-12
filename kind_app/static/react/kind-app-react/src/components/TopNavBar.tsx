import MenuIcon from '@mui/icons-material/Menu';
import {
  AppBar,
  Box,
  Toolbar,
  Button,
  IconButton,
  Divider,
  Typography
} from "@mui/material"

export default function TopNavBar() {

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: '#657d6a' }}>
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
          <Button color='inherit' href={"gratitude/"}>Gratitude</Button>
          <Divider orientation='vertical' variant="middle" flexItem />
          <Button color='inherit'>Mood Log</Button>
          <Divider orientation='vertical' variant="middle" flexItem />


          <Box 
            sx={{
              position: 'absolute',
              left: '50%',
              top: '50%',
              transform: 'translate(-50%, -50%)',
              display: 'flex',
              alignItems: 'center',
            }}
          >
            <Typography variant="h6" sx={{ color: 'inherit' }}>
              Welcome to Kind
            </Typography>
          </Box>

          <Box sx={{ flexGrow: 1 }} />
          <Button color='inherit' href={"login/"}>Login</Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}