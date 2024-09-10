import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import './App.css';
import KindHeader from './components/KindHeader';
import TopNavBar from './components/TopNavBar';
import Container from '@mui/material/Container';
import Stack from '@mui/material/Stack';
import GratitudeEntryBox from './components/GratitudeEntryBox';
import { AuthProvider } from './context/AuthContext';
import QuestionButtonCard from './components/QuestionButtonCard'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import GratitudeList from './pages/GratitudeEntryPage';

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
      <Router>
        <TopNavBar />
      </Router>
      <Stack direction="row" spacing={1} sx={{justifyContent: "center"}}>
        <Container maxWidth="sm">
          <KindHeader />
          <QuestionButtonCard />
          {/* <GratitudeEntryBox /> */}
          <Routes>
            <Route path="gratitude/" element={<GratitudeList />} />
          </Routes>
          <GratitudeList />
        </Container>
      </Stack>
      </ThemeProvider>
      </AuthProvider>
    </div>
  );
}

export default App;
