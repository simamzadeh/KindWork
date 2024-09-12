import { createTheme, ThemeProvider } from '@mui/material/styles';
import './App.css';
import TopNavBar from './components/TopNavBar';
import { AuthProvider } from './context/AuthContext';
import QuestionButtonCard from './components/QuestionButtonCard'
import { RouterProvider } from 'react-router-dom';
import Router from './Router';

const theme = createTheme({
  palette: {
    background: {
      default: '#f2f5f3',
    },
  },
});

function App() {
  return (
    <AuthProvider>
      <ThemeProvider theme={theme}>
        <TopNavBar />
        <RouterProvider router={Router} />
      </ThemeProvider>
    </AuthProvider>
  );
}

export default App;
