import * as React from 'react';
import Box from '@mui/material/Box';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import { Stack } from '@mui/material';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material';

// const theme = createTheme({
//   palette: {
//       primary: {
//           main: '#8A9EA1',
//       },
//   },
// });

// export default function GratitudeEntryBox() {
  //   return (
  //     <ThemeProvider theme={theme}>
  //       <Box
  //         component="form"
  //         sx={{
  //           width: 300, 
  //           height: 300,
  //           borderRadius: 1,
  //           bgcolor: 'primary.main',
  //         }}
  //       >
  //         <Stack>
  //           <Typography variant="h6" component="div">
  //             What are you grateful for?
  //           </Typography>
  //           <TextField
  //             id="outlined-basic"
  //             placeholder="I am grateful for..."
  //             multiline
  //             minRows={3}
  //             sx={{ width: '100%', backgroundColor: '#fff' }}
  //           />
  //         </Stack>
  //       </Box>
  //     </ThemeProvider>
  //   );
  // }


const GratitudeEntryCard = (
  <React.Fragment>
    <CardContent>
      <Typography gutterBottom sx={{ color: 'text.secondary', fontSize: 14 }}>
        Gratitude Entry
      </Typography>
      <Typography variant="h5" component="div">
        What are you grateful for?
      </Typography>
      <TextField
            id="outlined-basic"
            placeholder="I am grateful for..."
            multiline
            minRows={5}
            maxRows={5}
            sx={{ width: '100%', backgroundColor: '#fff' }}
      />
    </CardContent>
    {/* <CardActions>
      <Button size="small">Save Entry</Button>
    </CardActions> */}
  </React.Fragment>
);

export default function OutlinedCard() {
  return (
    <Box sx={{ 
      minWidth: 275, 
    }}>
      <Card variant="outlined">{GratitudeEntryCard}</Card>
    </Box>
  );
}