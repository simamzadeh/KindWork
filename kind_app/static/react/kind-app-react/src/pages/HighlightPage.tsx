import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';
import HighlightTable from '../components/HighlightTable';  // Import the table component
import InfoCard from '../components/InfoCard';

const HighlightPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4} display="flex" alignItems="flex-start"> {/* Adds vertical margin */}
        <Box flex={1} mr={1}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <HighlightTable />  {/* Render the highlight table here */}
            </Box>
          </Paper>
        </Box>
        <Box width={300}> {/* Adds margin below the InfoCard */}
          <InfoCard 
            title="Weekly Highlights" 
            content="Reflect on some highlights from the past week." 
          />
        </Box>
      </Box>
    </Container>
  );
};

export default HighlightPage;
