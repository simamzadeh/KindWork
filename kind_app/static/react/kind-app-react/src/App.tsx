import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import './App.css';
import KindHeader from './components/KindHeader';
import TopNavBar from './components/TopNavBar';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import GratitudeEntryBox from './components/GratitudeEntryBox';
import { AuthProvider } from './context/AuthContext';
import GratitudeEntriesTest from './components/test_component';
import QuestionButtonCard from './components/QuestionButtonCard'
import { BrowserRouter } from 'react-router-dom';

const theme = createTheme({
  palette: {
    background: {
      default: '#f2f5f3',
    },
  },
});

function App() {
  return (
    <div className="App">
      <AuthProvider>
      <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <TopNavBar />
      </BrowserRouter>
      <Stack direction="row" spacing={1} sx={{justifyContent: "center"}}>
        <Container maxWidth="sm">
          <KindHeader />
          <QuestionButtonCard />
          {/* <GratitudeEntryBox /> */}
          <GratitudeEntriesTest />
        </Container>
      </Stack>
      </ThemeProvider>
      </AuthProvider>
    </div>
  );
}

export default App;
