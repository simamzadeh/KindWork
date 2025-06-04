import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';
import InfoCard from '../components/InfoCard';
import KudosEntryTable from '../components/KudosEntryTable';

const KudosPage: React.FC = () => {
  return (
    <Container maxWidth="lg"> {/* Sets the max width of the container */}
      <Box mt={4} mb={4} display="flex" alignItems="flex-start">
        <Box flex={1} mr={1}>
          <Paper elevation={3}> {/* Adds a shadowed paper effect to the table */}
            <Box p={2}> {/* Adds padding around the table */}
              <KudosEntryTable />  {/* Render the GratitudeEntries table here */}
            </Box>
          </Paper>
        </Box>

        <Box width={300}> {/* Adds margin below the InfoCard */}
          <InfoCard 
            title="Give Kudos!" 
            content="Give kudos to someone who you appreciate." 
          />
        </Box>

      </Box>
    </Container>
  );
};

export default KudosPage;
