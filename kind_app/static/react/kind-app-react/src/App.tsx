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

const theme = createTheme({
  palette: {
    background: {
      default: '##F5F5DC',
    },
  },
});

function App() {
  return (
    <div className="App">
      <AuthProvider>
      <ThemeProvider theme={theme}>
      <CssBaseline />
      <TopNavBar />
      <Stack direction="row" spacing={1} sx={{justifyContent: "center"}}>
        <Container maxWidth="sm">
          <KindHeader />
          <GratitudeEntryBox />
          <GratitudeEntriesTest />
        </Container>
      </Stack>
      </ThemeProvider>
      </AuthProvider>
    </div>
  );
}

export default App;
