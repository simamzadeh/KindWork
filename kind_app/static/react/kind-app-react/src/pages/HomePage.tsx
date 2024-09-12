import React from 'react';
import CardComponent from '../components/QuestionCard';
import ButtonComponent from '../components/LogButton';
import { Container, Box } from '@mui/material';
import QuestionCard from '../components/QuestionCard';
import LogButton from '../components/LogButton';
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