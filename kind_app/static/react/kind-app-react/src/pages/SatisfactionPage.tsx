import React from 'react';
import { Container, Box, Paper } from '@mui/material';
import InfoCard from '../components/InfoCard';
import SatisfactionTable from '../components/SatisfactionTable';

const SatisfactionPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4} display="flex" alignItems="flex-start"> {/* Adds vertical margin */}
        <Box flex={1} mr={1}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <SatisfactionTable />  {/* Render the GratitudeEntries table here */}
            </Box>
          </Paper>
        </Box>
        <Box width={300}> {/* Adds margin below the InfoCard */}
          <InfoCard 
            title="Daily Satisfaction Logger" 
            content="Keep track of how satisfied you feel each day. This can be insightful when looked back on in hindsight." 
          />
        </Box>
      </Box>
    </Container>
  );
};

export default SatisfactionPage;
