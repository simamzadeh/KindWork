import * as React from 'react';
import Box from '@mui/material/Box';
import { ThemeProvider } from '@mui/material/styles';

export default function GratitudeEntryBox() {
    return (
      <ThemeProvider
        theme={{
          palette: {
            primary: {
              main: '#E4D7CF',
            },
          },
        }}
      >
        <Box
          sx={{
            width: 100,
            height: 100,
            borderRadius: 1,
            bgcolor: 'primary.main',
          }}
        />
      </ThemeProvider>
    );
  }
