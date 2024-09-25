import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';
import KindActTable from '../components/KindActTable';  // Import the table component
import InfoCard from '../components/InfoCard';

const KindActPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4} display="flex" alignItems="flex-start"> {/* Adds vertical margin */}
        <Box flex={1} mr={1}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <KindActTable />  {/* Render the GratitudeEntries table here */}
            </Box>
          </Paper>
        </Box>
        <Box width={300}> {/* Adds margin below the InfoCard */}
          <InfoCard 
            title="Acts of Kindness" 
            content="What can you do for someone in your life that will take a load off their shoulders?" 
          />
        </Box>
      </Box>
    </Container>
  );
};

export default KindActPage;
