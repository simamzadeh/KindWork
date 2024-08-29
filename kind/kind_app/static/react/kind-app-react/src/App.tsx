import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import './App.css';
import { Box } from '@mui/material';
import KindHeader from './components/KindHeader';
import TopNavBar from './components/TopNavBar';
import Container from '@mui/material/Container';

const theme = createTheme({
  palette: {
    background: {
      default: '#d2d2c0', // Light sage green color
    },
  },
});

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
      <CssBaseline />
        <TopNavBar />
        <Box></Box>
        <Container maxWidth="sm">
          <KindHeader />
        </Container>
      </ThemeProvider>
    </div>
  );
}

export default App;
