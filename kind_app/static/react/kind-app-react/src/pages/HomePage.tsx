import React from 'react';
import { Container } from '@mui/material';
import QuestionLogCard from '../components/QuestionLogCard';

const HomePage: React.FC = () => {
  return (
    <Container>
      <QuestionLogCard 
        title="What are you grateful for today?" 
        buttonText="Log Entry" 
      />
    </Container>
  );
};

export default HomePage;