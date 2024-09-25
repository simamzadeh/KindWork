import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';
import GratitudeEntryTable from '../components/GratitudeEntryTable';  // Import the table component
import InfoCard from '../components/InfoCard';

const GratitudeEntryPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4} display="flex" alignItems="flex-start">
        <Box flex={1} mr={1}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <GratitudeEntryTable />  {/* Render the GratitudeEntries table here */}
            </Box>
          </Paper>
        </Box>

        <Box width={300}> {/* Adds margin below the InfoCard */}
          <InfoCard 
            title="Gratitude Journal" 
            content="Keep track of things you are grateful for each day. Reflecting on gratitude can improve your mental well-being." 
          />
        </Box>

      </Box>
    </Container>
  );
};

export default GratitudeEntryPage;
