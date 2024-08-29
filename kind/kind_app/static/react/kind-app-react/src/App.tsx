import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import './App.css';
import KindHeader from './components/KindHeader';
import TopNavBar from './components/TopNavBar';
import Container from '@mui/material/Container';
import Skeleton from '@mui/material/Skeleton';
import Stack from '@mui/material/Stack';
import GratitudeEntryBox from './components/GratitudeEntryBox';

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
      <ThemeProvider theme={theme}>
      <CssBaseline />
      <TopNavBar />
      <Stack direction="row" spacing={1} sx={{justifyContent: "center"}}>
        <Container maxWidth="sm">
        <Skeleton variant="text" sx={{ fontSize: '1rem' }} />
          <KindHeader />
          <GratitudeEntryBox />
        </Container>
      </Stack>
      </ThemeProvider>
    </div>
  );
}

export default App;
