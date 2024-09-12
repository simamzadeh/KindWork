import React from 'react';
import { Card, CardContent, Typography, Button, Box } from '@mui/material';

interface QuestionLogCardProps {
  title: string;
  buttonText: string;
}

const QuestionLogCard: React.FC<QuestionLogCardProps> = ({ title, buttonText }) => {
  return (
    <Card sx={{ maxWidth: 345, margin: 'auto', mt: 4 }}>
      <CardContent>
        <Typography variant="h6" component="div">
          {title}
        </Typography>
        <Box mt={2} display="flex" justifyContent="center">
          <Button variant="contained" color="primary">
            {buttonText}
          </Button>
        </Box>
      </CardContent>
    </Card>
  );
};

export default QuestionLogCard;
