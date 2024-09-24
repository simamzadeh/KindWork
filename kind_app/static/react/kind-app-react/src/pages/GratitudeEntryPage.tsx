import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';
import GratitudeEntryTable from '../components/GratitudeEntryTable';  // Import the table component

const GratitudeEntryPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4}> {/* Adds vertical margin */}

        <Box mt={4}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <GratitudeEntryTable />  {/* Render the GratitudeEntries table here */}
            </Box>
          </Paper>
        </Box>
      </Box>
    </Container>
  );
};

export default GratitudeEntryPage;
