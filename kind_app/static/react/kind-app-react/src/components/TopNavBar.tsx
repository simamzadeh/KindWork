import {
  AppBar,
  Box,
  Toolbar,
  Button,
  Divider,
  Typography
} from "@mui/material";
import { useState, useEffect } from "react";

export default function TopNavBar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState<string | null>(null); // State for username

  // Fetch authentication status and username from Django
  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const response = await fetch("/api/check-auth/");
        const data = await response.json();
        setIsLoggedIn(data.isAuthenticated);
        setUsername(data.username || null); // Set the username if authenticated (and null if undefined)
      } catch (error) {
        console.error("Error checking authentication status", error);
      }
    };

    checkAuthStatus();
  }, []);

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" sx={{ backgroundColor: '#657d6a' }}>
        <Toolbar>
          <Button color='inherit' href={"/kudos/"}>Give Kudos</Button>
          <Divider orientation='vertical' variant="middle" flexItem />
          <Button color='inherit' href={"/satisfaction/"}>Satisfaction</Button>
          <Divider orientation='vertical' variant="middle" flexItem />
          <Button color='inherit' href={"/kind-acts/"}>Kind Acts</Button>
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
              {isLoggedIn ? `Welcome to KindWork, ${username}` : 'Welcome to KindWork'}
            </Typography>
          </Box>

          <Box sx={{ flexGrow: 1 }} />

          {/* Conditionally render the Login or Logout button */}
          {isLoggedIn ? (
            <Button color="inherit" href="/logout/">Logout</Button>
          ) : (
            <Button color="inherit" href="/login/">Login</Button>
          )}
        </Toolbar>
      </AppBar>
    </Box>
  );
}
