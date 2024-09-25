import React from 'react';
import { Container, Box, Paper } from '@mui/material';
import MoodLogTable from '../components/MoodLogTable';
import InfoCard from '../components/InfoCard';

const MoodLogPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4} display="flex" alignItems="flex-start"> {/* Adds vertical margin */}
        <Box flex={1} mr={1}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <MoodLogTable />  {/* Render the GratitudeEntries table here */}
            </Box>
          </Paper>
        </Box>
        <Box width={300}> {/* Adds margin below the InfoCard */}
          <InfoCard 
            title="Mood Logger" 
            content="Keep track of how you feel overall each day. This can be insightful when looked back on in hindsight." 
          />
        </Box>
      </Box>
    </Container>
  );
};

export default MoodLogPage;
