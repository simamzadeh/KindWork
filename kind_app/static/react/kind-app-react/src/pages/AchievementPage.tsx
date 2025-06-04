import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';
import KindActTable from '../components/AchievementTable';  // Import the table component
import InfoCard from '../components/InfoCard';

const AchievementPage: React.FC = () => {
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
            title="Achievements" 
            content="What is something you achieved that you're proud of? Celebrating small wins is key to improving our mental health. " 
          />
        </Box>
      </Box>
    </Container>
  );
};

export default AchievementPage;
